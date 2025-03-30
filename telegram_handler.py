# Telegram handling
from telethon import TelegramClient, events
import re
from config import API_ID, API_HASH, CHANNEL_ID, USER_ID
from solana_trader import SolanaTrader

class TelegramBot:
    def __init__(self):
        self.client = TelegramClient('bot_session', API_ID, API_HASH)
        self.trader = SolanaTrader()

    async def run(self):
        await self.client.start()
        print("✅ Telegram bot started!")
        self.client.add_event_handler(self.handle_message, events.NewMessage(chats=CHANNEL_ID))
        await self.client.run_until_disconnected()

    async def handle_message(self, event):
        message = event.raw_text
        match = re.search(r'([1-9A-HJ-NP-Za-km-z]{32,44})', message)
        if match:
            token_address = match.group(1)
            print(f"Found token: {token_address}")
            tx_id = self.trader.execute_trade(token_address)
            await self.send_notification(f"✅ Swap completed!\n\n🔹 Token: {token_address}\n🔹 Transaction: https://solscan.io/tx/{tx_id}")

    async def send_notification(self, message):
        await self.client.send_message(USER_ID, message)