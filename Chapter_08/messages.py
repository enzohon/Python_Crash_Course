"""
文件名: messages.py
描述: 练习 8.9 - 编写 show_messages() 函数，演示如何向函数传递列表，并实现列表元素的遍历打印。
"""

# --- 练习 8.9: 消息 ---

# 1. 函数定义: 接收一个包含文本消息的列表
def show_messages(messages):
    """打印列表中的每条文本消息"""
    for message in messages:
        print(message)

# 2. 数据准备: 创建简短的文本消息列表
text_messages = [
    "Hello Python!",
    "Functions make code clean.",
    "Keep coding, keep growing."
]

# 3. 调用函数
print("--- 开始展示列表中的文本消息 ---")
show_messages(text_messages)

# 作者: Enzo
# 日期: 2026-05-25