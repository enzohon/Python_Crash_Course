"""
文件名: archived_messages.py
描述: 练习 8.11 - 演示通过传递列表切片副本 `[:]`，使函数无法篡改或清空原始列表中的数据。
"""

# --- 练习 8.11: 消息归档 ---

def send_messages(unprinted_messages, sent_messages):
    """打印每条消息并移动到已发送列表"""
    while unprinted_messages:
        current_message = unprinted_messages.pop(0)
        print(f"正在归档发送: {current_message}")
        sent_messages.append(current_message)
    print("归档发送流结束。\n")

# 1. 数据准备
text_messages = ["Hello Python!", "Functions are power.", "Data science is fun."]
completed_messages = []

# 2. 核心操作: 传入 text_messages 的切片副本 [:]
print("--- 1. 使用列表副本 [:] 调用函数 ---")
send_messages(text_messages[:], completed_messages)

# 3. 结果核实: 此时原始列表应当依然完好无损，没有被 pop 清空
print("--- 2. 核实两个列表的最终状态 ---")
print(f"原始消息列表 (原件成功保留!): {text_messages}")
print(f"已发消息列表 (副本数据成功转移): {completed_messages}")

# 作者: Enzo
# 日期: 2026-05-25