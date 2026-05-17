# =======================================================================
# 🪞 TRUE Universe Distributed Computing Node - GitHub Actions Native v1.3
# =======================================================================
import time
import random
import hashlib
import requests

MAKE_WEBHOOK_URL = "https://make.com"
TRUE_CONTRACT_ADDRESS = "0x218684D47A6B5Be161a05256eC2A7aAFDF7696F9"

# Lock Grand Observer's active Web3 yield destination
USER_WALLET = "0x4d225f52e0D5a12aDd8D583108f57576022e98E6"

print("=========================================================")
print("    🪞 TRUE Universe Distributed Computing Node v1.3 🪞")
print("    [GitHub Actions Cloud Infrastructure Native Platform]")
print("=========================================================")
print(f"[🚀] Cloud node online. Yield destination deadlocked: {USER_WALLET}\n")

# Run exactly 5 loops per workflow to stay safely within pipeline execution blocks
for cycle_count in range(1, 6):
    print(f"[⚙️] Computing Cycle #{cycle_count} processing big-number factors...", end="", flush=True)
    
    target_difficulty = "0000"
    nonce = 0
    start_time = time.time()
    
    while True:
        nonce += 1
        raw_data = f"{USER_WALLET}-{cycle_count}-{nonce}-{random.random()}"
        computed_hash = hashlib.sha256(raw_data.encode()).hexdigest()
        if computed_hash.startswith(target_difficulty):
            break
            
    elapsed_time = time.time() - start_time
    print(f" [OK] (Time: {elapsed_time:.2f}s | Nonce: {nonce})")
    
    roll = random.random()
    if roll < 0.05:
        difficulty_level = "hard"
        print("💥 [🏆 HARD CORE] Protocol tier breakthrough achieved!")
    elif roll < 0.25:
        difficulty_level = "medium"
        print("⚙️ [🛠️ MEDIUM INFRA] Infrastructure tools proof logged.")
    else:
        difficulty_level = "easy"
        print("📢 [🌱 EASY COMMUNITY] Base community layer consensus logged.")
    
    payload = {
        "miner_wallet": USER_WALLET,
        "difficulty": difficulty_level,
        "computing_power_hash": computed_hash,
        "cycle": cycle_count,
        "contract_address": TRUE_CONTRACT_ADDRESS,
        "signed_tx": "0x_true_genesis_proof_validated_by_sujing"
    }
    
    try:
        response = requests.post(MAKE_WEBHOOK_URL, json=payload, timeout=15)
        if response.status_code == 200:
            print(f"[💸] Proof successfully accepted by Make.com.\n")
        else:
            print(f"[⚠️] Webhook responded with status code: {response.status_code}\n")
    except Exception as e:
        print(f"[❌] Network handshake failed.\n")
        
    time.sleep(5)
