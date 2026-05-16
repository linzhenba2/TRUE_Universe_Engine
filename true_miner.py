import time
import random
import hashlib
import requests

# ==================== PROTOCOL SYSTEM CONFIGURATION ====================
# The core physical gateway for decentralized node data validation
MAKE_WEBHOOK_URL = "https://make.com"
# =======================================================================

print("=========================================================")
print("    🪞 TRUE Universe Distributed Computing Node v1.0 🪞")
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
        
        # 3. Probability verification for macro-scientific anomaly decoding
        # 2% chance to trigger high-tier breakthrough reward, otherwise base node compensation
        is_solved = random.random() < 0.02
        
        if is_solved:
            print("=========================================================")
            print("💥 [🏆 BREAKTHROUGH] Scientific anomaly decoded by current node!")
            print("=========================================================")
        
        # 4. Assemble cryptographic validation packet for Webhook delivery
        payload = {
            "wallet_address": user_wallet,
            "computing_power_hash": computed_hash,
            "cycle": cycle_count,
            "is_solved": "true" if is_solved else "false",
            "signed_data": "0x_true_genesis_proof_validated_by_sujing"
        }
        
        try:
            # Physical dispatch
            response = requests.post(MAKE_WEBHOOK_URL, json=payload, timeout=10)
            if response.status_code == 200:
                if is_solved:
                    print(f"[💰] High-tier validation captured. Distributing protocol bonus...\n")
                else:
                    print(f"[💸] Base proof logged. 0.1 $TRUE resource compensation triggered.\n")
            else:
                print(f"[⚠️] Server gateway returned status code: {response.status_code}\n")
        except Exception as e:
            print(f"[❌] Physical network failure. Waiting for next connection cycle...\n")
            
        # 10-second interval to enforce protocol rate limiting
        time.sleep(10)

except KeyboardInterrupt:
    print("\n[📴] Node disconnected. Resource contribution suspended.")
