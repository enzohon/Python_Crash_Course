"""
文件名: person.py
描述: 练习 6.1 - 使用字典存储并打印一个人的信息
"""

# --- 练习 6.1: 人 ---

# 1. 数据准备: 创建一个字典来存储个人信息
# 💡 逻辑: 字典使用花括号 {} 定义，包含键值对
person = {
    'first_name': 'Elon',
    'last_name': 'Musk',
    'age': 52,
    'city': 'Austin'
}

# 2. 打印信息: 访问字典中的值并输出
# 💡 技巧: 使用 f-string 可以方便地将字典的值嵌入字符串中
print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")

# 3. 处理不同类型的数据
# 注意: age 是整数类型 (int)，print 时会自动转换为字符串显示
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# 作者: Enzo
# 日期: 2026-01-13