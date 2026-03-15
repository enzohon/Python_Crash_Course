"""
文件名: glossary.py
描述: 练习 6.3 - 创建一个编程术语词汇表并格式化输出
"""

# --- 练习 6.3: 词汇表 ---

# 1. 数据准备: 存储编程术语及其含义
# 💡 逻辑: 键是术语，值是该术语的解释
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
}

# 2. 打印术语 'string'
# 💡 技巧: 使用 \n (换行符) 在输出中插入空行，保持整洁
print(f"\nString: \n{glossary['string']}")

# 3. 打印术语 'comment'
print(f"\nComment: \n{glossary['comment']}")

# 4. 打印术语 'list'
print(f"\nList: \n{glossary['list']}")

# 5. 打印术语 'loop'
print(f"\nLoop: \n{glossary['loop']}")

# 6. 打印术语 'dictionary'
print(f"\nDictionary: \n{glossary['dictionary']}")

# 作者: Enzo
# 日期: 2026-01-13