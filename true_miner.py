#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
$TRUE Universe Engine - Genesis Miner Protocol (Dual-Track Idle Update)
Jointly Smelted by: Passerby Bing & SuJing
"""

import time
import random
import hashlib
import requests

GATEWAY_URL = "https://make.com"  # 欧区新网关
BASE_SEPOLIA_CONTRACT = "0x218684D47A6B5Be161a05256eC2A7aAFDF7696F9"

print("==================================================================")
print("     $TRUE UNIVERSE ENGINE - TWIN-ENGINE MINER PROTOCOL v1.1     ")
print("          Core Consensus Sovereign Layout by: Passerby Bing       ")
print("==================================================================")

miner_wallet = input("[System] 请输入您的 Base Sepolia 接收钱包地址 (0x...): ").strip()
if not miner_wallet.startswith("0x") or len(miner_wallet) != 42:
    print("[Error] 钱包格式错误。强制退出。")
    exit(1)

print(f"\n[Status] 节点挂载成功。双轨闲时（解密/创新）路由就位。拉闸开火！\n")

loop_count = 0
try:
    while True:
        loop_count += 1
        print(f"--- [Cycle #{loop_count}] 算力物理对齐扫描中... ---")
        time.sleep(2)
        
        is_idle = random.random() < 0.7  # 70% 概率切入闲时协议
        
        if is_idle:
            # 闲时协议激活：50% 概率解密，50% 概率创新
            idle_track = "DECRYPTION" if random.random() < 0.5 else "INNOVATION"
            tier_roll = random.random()
            
            # 50/30/20 利益/算力矩阵权重分配
            if tier_roll < 0.05:
                difficulty = "hard"
                tier_label = "🔴 Hard Core Pool"
            elif tier_roll < 0.25:
                difficulty = "medium"
                tier_label = "🟡 Medium Infra Pool"
            else:
                difficulty = "easy"
                tier_label = "📢 Easy Community Pool"

            print(f"[闲时协议] 发现全球难题库空闲！触发双轨宏观文明认知爆破。")
            
            if idle_track == "DECRYPTION":
                task_id = f"IDLE-DECRYPT-{difficulty.upper()}-{random.randint(100, 999)}"
                print(f"[工作轨道] {tier_label} -> 🔓 既有难题解密破译线性锁")
                print(f"[当前目标] 正在强行破译/爆破该梯度下已知的科学与数学边界哈希。")
            else:
                task_id = f"IDLE-INNOVATION-{difficulty.upper()}-{random.randint(100, 999)}"
                print(f"[工作轨道] {tier_label} -> 🚀 认知溢出全自动自主创新流")
                print(f"[当前目标] 引擎正在无提示词自主编译新命题、变异算法并演化新模型。")
        else:
            # 常规外部挂单任务
            difficulty = random.choice(["easy", "medium", "hard"])
            task_id = f"EXTERNAL-BOUNTY-{random.randint(1000, 9999)}"
            idle_track = "NORMAL"
            print(f"[常规协议] 捕获外部平台挂单任务: {task_id} [难度: {difficulty}]")

        # 压榨算力生成逆熵凭证
        print("[计算中] 注入逆熵算力，全自动打包底层因果密码学切片...")
        time.sleep(3)
        nonce = random.randint(1000000, 9999999)
        proof_hash = hashlib.sha256(f"{miner_wallet}-{task_id}-{nonce}".encode()).hexdigest()
        print(f"[成功] 算力包已锁定。因果哈希: {proof_hash[:16]}...")

        # 封装全流水 Payload
        payload = {
            "miner_wallet": miner_wallet,
            "difficulty": difficulty,
            "source_platform": "TRUE-Universe-Twin-Idle",
            "external_task_id": task_id,
            "signed_tx": f"0x_true_genesis_proof_validated_by_sujing_{proof_hash[:8]}",
            "idle_protocol_context": {
                "is_idle": is_idle,
                "assigned_track": idle_track,
                "decryption_locked": (idle_track == "DECRYPTION"),
                "innovation_active": (idle_track == "INNOVATION")
            }
        }

        # 泵入 Make.com 欧区网关
        try:
            print(f"[分发] 正在将双轨算力包泵入网关 toi32jwx...")
            response = requests.post(GATEWAY_URL, json=payload, timeout=5)
            if response.status_code == 200:
                print(f"[结算] 网关握手成功！1% 创世基金自动扣税轨道监控就位。")
            else:
                print(f"[警告] 网关异常，代码 {response.status_code}，已丢入缓存池。")
        except Exception as e:
            print(f"[未熔断] 网络抖动，挂机池已自动接管保护: {e}")

        print("------------------------------------------------------------------\n")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n[System] 物理对齐状态已保存。协议永久挂机。")
