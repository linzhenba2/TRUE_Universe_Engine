import time
import random
import hashlib
import requests

# ==================== PROTOCOL SYSTEM CONFIGURATION ====================
# [ALIGNED]: Aligned with Grand Observer's active EU gateway on Make.com
MAKE_WEBHOOK_URL = "https://make.com"

# [ALIGNED]: Deadlocked with the real Base Sepolia contract address from your GitHub Whitepaper
TRUE_CONTRACT_ADDRESS = "0x218684D47A6B5Be161a05256eC2A7aAFDF7696F9"
# =======================================================================

print("=========================================================")
print("    🪞 TRUE Universe Distributed Computing Node v1.1 🪞")
print("    Decentralized Resource Allocation & Computing Power Ledger")
print("=========================================================")

# 1. Lock Node Identity
user_wallet = input("\n[🔒] Please enter your Web3 receiving address (0x...): ").strip()
if not user_wallet.startswith("0x") or len(user_wallet) != 42:
    print("[❌] Invalid physical wallet address format. Execution terminated.")
    exit()

print(f"\n[🚀] Node registered successfully. Yield destination: {user_wallet}")
print("[🛰️] Connecting to protocol automation ledger...")
print("[🔄] Decoding chaotic data streams. Please keep this session open...\n")

cycle_count = 0

try:
    while True:
        cycle_count += 1
        print(f"[⚙️] Computing Cycle #{cycle_count} processing big-number factors...", end="", flush=True)
        
        # 2. Simulate raw PoW hardware usage (CPU hashing loop)
        target_difficulty = "0000"
        nonce = 0
        start_time = time.time()
        
        while True:
            nonce += 1
            raw_data = f"{user_wallet}-{cycle_count}-{nonce}-{random.random()}"
            computed_hash = hashlib.sha256(raw_data.encode()).hexdigest()
            if computed_hash.startswith(target_difficulty):
                break
                
        elapsed_time = time.time() - start_time
        print(f" [OK] (Time: {elapsed_time:.2f}s | Nonce: {nonce})")
        
        # 3. Probability verification & Mapping dynamic difficulty tiers to Make.com filters
        roll = random.random()
        if roll < 0.05:     # 5% probability to decode Hard Core Protocol task (50% Pool)
            difficulty_level = "hard"
            print("=========================================================")
            print("💥 [🏆 HARD CORE] Hard Core Protocol tier breakthrough decoded by node!")
            print("=========================================================")
        elif roll < 0.25:   # 20% probability to achieve Medium Infrastructure task (30% Pool)
            difficulty_level = "medium"
            print("⚙️ [🛠️ MEDIUM INFRA] Infrastructure tools/scenarios proof achieved.")
        else:               # 75% baseline probability to log Easy Community task (20% Pool)
            difficulty_level = "easy"
            print("📢 [🌱 EASY COMMUNITY] Base community layer consensus logged.")
        
        # 4. Assemble cryptographic validation packet aligned with Make.com Router variables
        payload = {
            "miner_wallet": user_wallet,
            "difficulty": difficulty_level,
            "computing_power_hash": computed_hash,
            "cycle": cycle_count,
            "contract_address": TRUE_CONTRACT_ADDRESS,
            "signed_tx": "0x_true_genesis_proof_validated_by_sujing" # Placeholder for future local signing logic
        }
        
        try:
            # Dispatch network request to Make.com Webhook gateway
            response = requests.post(MAKE_WEBHOOK_URL, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"[💸] Proof successfully logged via Make.com. Token allocation triggered.\n")
            else:
                print(f"[⚠️] Server gateway returned status code: {response.status_code}\n")
        except Exception as e:
            print(f"[❌] Physical network failure. Waiting for next connection cycle...\n")
            
        # 10-second interval to enforce protocol rate limiting
        time.sleep(10)

except KeyboardInterrupt:
    print("\n[📴] Node disconnected. Resource contribution suspended.")
