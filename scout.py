import asyncio
import csv
import os
from datetime import datetime
from playwright.async_api import async_playwright
from playwright_stealth import Stealth  # Use the Class, not the function
from telegram import Bot
import config
from brain import evaluate_job

def log_to_csv(role, target_name, category):
    """Saves findings with category metadata."""
    file_exists = os.path.isfile('found_jobs.csv')
    with open('found_jobs.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Date', 'Category', 'Site', 'Title', 'Score', 'Reason'])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            category,
            target_name,
            role['title'],
            role['score'],
            role['reason']
        ])

async def send_alert(role, url, category):
    """Sends immediate Telegram notifications."""
    bot = Bot(token=config.TELEGRAM_TOKEN)
    msg = f"🎯 **{category} Signal!**\n\n**{role['title']}**\nScore: {role['score']}/10\n\n🔗 [Link]({url})"
    await bot.send_message(chat_id=config.CHAT_ID, text=msg, parse_mode="Markdown")

async def run_scout():
    async with async_playwright() as p:
        print("🚀 Launching Spatial Scout Engine (v2025.12)...")
        browser = await p.chromium.launch(headless=True)
        
        # Create a context with a clean User-Agent
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # APPLY STEALTH CORRECTLY FOR 2025
        stealth_plugin = Stealth()
        await stealth_plugin.apply_stealth_async(page)

        # Define scouting clusters
        all_tasks = [
            (config.TARGETS, "Standard Job"),
            (config.AI_INTERN_TARGETS, "AI Internship")
        ]

        for target_list, cat in all_tasks:
            for target in target_list:
                print(f"📡 Scanning {target['name']}...")
                try:
                    # Extended timeout for slower research site portals
                    await page.goto(target['url'], wait_until="networkidle", timeout=60000)
                    content = await page.inner_text("body")
                    
                    matches = evaluate_job(content)
                    for role in matches:
                        if role.get("is_compliant") and role['score'] >= 7:
                            log_to_csv(role, target['name'], cat)
                            await send_alert(role, target['url'], cat)
                    
                    # Anti-throttling delay
                    await asyncio.sleep(10)
                except Exception as e:
                    print(f"❌ Site Error ({target['name']}): {e}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scout())