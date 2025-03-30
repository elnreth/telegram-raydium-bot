# Swap logic on Raydium
from solana.rpc.api import Client
from solders.transaction import Transaction
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solders.system_program import transfer, TransferParams
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed
from config import SOLANA_RPC_URL, PRIVATE_KEY, SOL_AMOUNT, SLIPPAGE
from utils import fetch_json

class SolanaTrader:
    def __init__(self):
        self.client = Client(SOLANA_RPC_URL)
        self.wallet = Keypair.from_secret_key(bytes.fromhex(PRIVATE_KEY))

    def get_best_pool(self, token_address):
        try:
            pools = fetch_json("https://api.raydium.io/pairs")
            if pools:
                for pool in pools:
                    if pool['baseMint'] == token_address or pool['quoteMint'] == token_address:
                        return pool
        except Exception as e:
            print(f"Error retrieving liquidity pool: {e}")
        return None

    def execute_trade(self, token_address):
        print(f"Searching for the best liquidity pool for {token_address}...")
        pool = self.get_best_pool(token_address)
        if not pool:
            print("❌ No pool found, swap cannot be executed.")
            return None
        expected_out = float(pool['price']) * SOL_AMOUNT
        min_out = expected_out * (1 - SLIPPAGE)
        print(f"Swap: {SOL_AMOUNT} SOL -> Min {min_out} {token_address} (Slippage {SLIPPAGE*100}%)")
        try:
            tx = Transaction()
            swap_ix = transfer(TransferParams(
                from_pubkey=self.wallet.pubkey(),
                to_pubkey=Pubkey(pool['id']),
                lamports=int(SOL_AMOUNT * 1e9),
            ))
            tx.add(swap_ix)
            tx_result = self.client.send_transaction(tx, self.wallet, opts=TxOpts(skip_preflight=True, preflight_commitment=Confirmed))
            print(f"✅ Transaction completed: {tx_result['result']}")
            return tx_result['result']
        except Exception as e:
            print(f"❌ Swap error: {e}")
            return None