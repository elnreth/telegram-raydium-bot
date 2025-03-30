# Main entry point
from telegram_handler import TelegramBot
import asyncio

def main():
    print("🔹 Starting Telegram bot...")
    bot = TelegramBot()
    asyncio.run(bot.run())

if __name__ == "__main__":
    main()