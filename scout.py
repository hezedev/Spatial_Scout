import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth # 2025 class-based syntax
from telegram import Bot
import config
from brain import evaluate_job

async def send_alert(role, url):
    bot = Bot(token=config.TELEGRAM_TOKEN)
    msg = f"🎯 **Job Signal!**\n\n**{role['title']}**\nScore: {role['score']}/10\nReason: {role['reason']}\n\n🔗 [Link]({url})"
    await bot.send_message(chat_id=config.CHAT_ID, text=msg, parse_mode="Markdown")

async def run_scout():
    async with async_playwright() as p:
        print("🚀 Starting Cloud Scout...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        # Apply 2025 Stealth to Context
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
                        await send_alert(role, target['url'])
                await asyncio.sleep(10) # Small delay
            except Exception as e:
                print(f"❌ Site Error: {e}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scout())