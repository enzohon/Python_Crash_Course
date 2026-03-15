"""
文件名: favorite_book.py
描述: 练习 8.2 - 演示向函数传递形参和实参 (Function Arguments)
"""

# --- 练习 8.2: 喜欢的书 ---

# 1. 定义带参数的函数: 包含一个名为 title 的形参
def favorite_book(title):
    # 💡 技巧: 使用 f-string (格式化字符串) 可以很方便地将形参变量插入到打印的消息中
    print(f"One of my favorite books is {title}.")

# 2. 调用函数并传递实参: 将一本书的书名作为实参传递给它
favorite_book('Alice in Wonderland')

# 如果你想尝试其他的书，可以再次调用：
# favorite_book('The Little Prince')

# 作者: Enzo
# 日期: 2026-03-15