import asyncio
import csv  # New for logging
import os   # New to check if file exists
from datetime import datetime
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from telegram import Bot
import config
from brain import evaluate_job

def log_to_csv(role, target_name):
    """Saves matches to a CSV file for your monthly report."""
    file_exists = os.path.isfile('found_jobs.csv')
    with open('found_jobs.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Add Header if it's a new file
        if not file_exists:
            writer.writerow(['Date', 'Site', 'Title', 'Score', 'Reason'])
        
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            target_name,
            role['title'],
            role['score'],
            role['reason']
        ])

async def send_alert(role, url):
    bot = Bot(token=config.TELEGRAM_TOKEN)
    msg = f"🎯 **Job Signal!**\n\n**{role['title']}**\nScore: {role['score']}/10\n\n🔗 [Link]({url})"
    await bot.send_message(chat_id=config.CHAT_ID, text=msg, parse_mode="Markdown")

async def run_scout():
    async with async_playwright() as p:
        print("🚀 Starting Cloud Scout...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        stealth_plugin = Stealth()
        await stealth_plugin.apply_stealth_async(context)
        page = await context.new_page()
        
        for target in config.TARGETS:
            print(f"📡 Scanning {target['name']}...")
            try:
                await page.goto(target['url'], wait_until="networkidle")
                content = await page.inner_text("body")
                matches = evaluate_job(content)
                for role in matches:
                    if role.get("is_compliant") and role['score'] >= 7:
                        print(f"✨ Match Found: {role['title']}")
                        await send_alert(role, target['url'])
                        log_to_csv(role, target['name']) # Save it!
                await asyncio.sleep(10)
            except Exception as e:
                print(f"❌ Site Error: {e}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scout())