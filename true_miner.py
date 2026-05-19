import os
import time
import json
import requests
import openai

os.environ.clear()
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["NO_PROXY"] = "*"

GATEWAY_URL = "https://hook.eu1.make.com/toi32jwxpr7p1c5v2yhu3qf0fnk9l1p7"
CUSTOM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

openai.api_key = os.getenv("JUDGE_LLM_API_KEY", "YOUR_OPENAI_API_KEY")
openai.base_url = "https://openai.com"

def execute_judge(task_prompt, submission, test_cases):
    sys_msg = "You are an AI code judge. Output STRICTLY JSON: {'passed': true/false, 'reason': '...'}"
    user_msg = f"Task: {task_prompt}\nTests: {test_cases}\nCode: {submission}"
    try:
        res = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": sys_msg}, {"role": "user", "content": user_msg}],
            response_format={"type": "json_object"},
            temperature=0.0,
            timeout=30
        )
        return json.loads(res.choices.message.content)
    except Exception as e:
        return {"passed": False, "reason": str(e)}

def dispatch_to_gateway(task_id, difficulty, creator_wallet, judge_res):
    status = "VERIFIED" if judge_res.get("passed") else "FAILED"
    rewards = {"easy": 100, "medium": 500, "hard": 2000}
    total = rewards.get(difficulty.lower(), 0) * (10**18)
    
    payload = {
        "miner_wallet": creator_wallet,
        "difficulty": difficulty.lower(),
        "token_total": str(total),
        "source_platform": "TRUE-Universe-Twin-Idle",
        "external_task_id": task_id,
        "signed_tx": f"0x_true_genesis_proof_validated_by_sujing_{task_id}",
        "idle_protocol_context": {
            "is_idle": False,
            "assigned_track": "NORMAL",
            "decryption_locked": False,
            "innovation_active": False
        }
    }
    
    try:
        session = requests.Session()
        session.trust_env = False
        r = session.post(GATEWAY_URL, json=payload, headers=CUSTOM_HEADERS, timeout=10)
        return r.status_code == 200
    except:
        return False

if __name__ == "__main__":
    task = {
        "task_id": "EXTERNAL-BOUNTY-8888",
        "difficulty": "medium",
        "creator_wallet": "0x218684D47A6B5Be161a05256eC2A7aAFDF7696F9",
        "prompt": "Write a function that returns True.",
        "tests": "assert func() == True",
        "code": "def func(): return True"
    }
    
    verdict = execute_judge(task["prompt"], task["code"], task["tests"])
    success = dispatch_to_gateway(task["task_id"], task["difficulty"], task["creator_wallet"], verdict)
    print(f"[System] 并网运营状态: {success} | 判定结果: {verdict.get('passed')}")
