# 🦾 Solana Telegram Swap Bot

This bot retrieves token addresses from Telegram channels and automatically performs swaps on Raydium.

## 🚀 Features
✅ Monitors specific Telegram channels for token addresses  
✅ Automatically executes swaps using Raydium DEX on Solana  
✅ Sends a Telegram notification after each successful swap  
✅ Secure wallet management using Solana CLI  

---

## 🛠️ Installation

### **1️⃣ Clone the repository**
```sh
git clone git@github.com:elnreth/telegram-raydium-bot.git
cd telegram-raydium-bot
```

### **2️⃣ Install Solana CLI**
The bot requires the Solana CLI to interact with the Solana blockchain.
Install it with:
```sh
sh -c "$(curl -sSfL https://release.anza.xyz/install)"
```
After installation, verify it:
```sh
solana --version
```

### **3️⃣ Create and Configure a Solana Wallet**
👉 If you don’t have a wallet, create one:
```sh
solana-keygen new --outfile id.json
```
🔄 If you already have a wallet, import it:
```sh
solana-keygen recover --outfile id.json
```
Then, set your wallet as the default:
```sh
solana config set --keypair id.json
```
To check your wallet balance:
```sh
solana balance
```

### **4️⃣ Install Python Dependencies**
Ensure you have Python 3 installed, then run:
```sh
pip install -r requirements.txt
```

### **5️⃣ Configure config.py**
Edit the config.py file to set up:

- Telegram API credentials

- Solana wallet details

- Swap parameters (amount, slippage, etc.)

### **6️⃣ Run the bot**
```sh
python bot.py
```

##

### 📝 Configuration
Modify config.py to include:
```python
# Telegram API credentials
API_ID = "your_api_id"
API_HASH = "your_api_hash"
CHANNEL_ID = "your_channel_id"

# Solana wallet and RPC settings
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
PRIVATE_KEY_PATH = "id.json"

# Swap parameters
SOL_AMOUNT = 0.1  # Amount of SOL to swap
SLIPPAGE = 0.01    # Max slippage (1%)
```

##

### 🛠️ Troubleshooting
❌ Bot fails to connect to Solana?\
✔️ Check if your RPC URL in config.py is correct.

❌ Transaction fails?\
✔️ Ensure your wallet has enough SOL for transactions.

❌ No messages detected from Telegram?\
✔️ Check if your bot has access to the correct channel.

##

### ⚖️ License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

##

### 🌟 Contributing
Feel free to fork this repository and submit pull requests for improvements! 🎉