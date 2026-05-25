"""
文件名: sending_messages.py
描述: 练习 8.10 - 编写 send_messages() 函数，在函数内修改传递进来的列表（出队与入队操作）。
"""

# --- 练习 8.10: 发送消息 ---

# 1. 函数定义: 从待发送列表循环弹出消息，并追加到已发送列表
# 💡 逻辑: 使用 while 循环配合 list.pop(0) 从列表头部开始处理，可以确保消息按原序发送
def send_messages(unprinted_messages, sent_messages):
    """模拟打印并移动消息到已发送列表"""
    print("🚀 开始发送文本消息...")
    while unprinted_messages:
        current_message = unprinted_messages.pop(0)
        print(f"正在向服务器发送: {current_message}")
        sent_messages.append(current_message)
    print("✅ 所有的消息均已发送完毕。\n")

# 2. 数据准备: 定义一个原始消息列表以及一个空的目标存储列表
text_messages = ["Hello Python!", "Functions are power.", "Data science is fun."]
completed_messages = []

# 3. 调用函数
send_messages(text_messages, completed_messages)

# 4. 验证状态: 检查原列表是否为空，目标列表是否完整
print("--- 检查两个列表的最终状态 ---")
print(f"原始消息列表 (text_messages): {text_messages}")
print(f"已发消息列表 (completed_messages): {completed_messages}")

# 作者: Enzo
# 日期: 2026-05-25