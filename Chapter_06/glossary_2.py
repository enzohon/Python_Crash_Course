"""
文件名: glossary_2.py
描述: 练习 6.4 - 使用循环来改进词汇表，避免重复的 print 调用
"""

# --- 练习 6.4: 词汇表 2 ---

# 1. 数据准备: 创建包含编程术语的字典
# 💡 这是一个键值对结构，存储术语及其定义
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one by one.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean': 'A value that is either True or False.',
}

# 2. 遍历输出: 使用循环替代重复的 print 语句
# 逻辑: .items() 方法同时返回键 (word) 和值 (meaning)
for word, meaning in glossary.items():
    print(f"\nWord: {word.title()}")
    print(f"Meaning: {meaning}")

# 作者: Enzo
# 日期: 2026-01-13