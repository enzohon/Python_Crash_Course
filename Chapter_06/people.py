"""
文件名: people.py
描述: 练习 6.7 - 在列表中存储多个字典，并遍历打印所有信息
"""

# --- 练习 6.7: 人们 ---

# 1. 数据准备: 创建三个表示不同人的字典
# 💡 每个字典都包含相同的键 (first_name, last_name, age, city)
person_1 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': 76,
    'city': 'princeton',
}

person_2 = {
    'first_name': 'marie',
    'last_name': 'curie',
    'age': 66,
    'city': 'paris',
}

person_3 = {
    'first_name': 'isaac',
    'last_name': 'newton',
    'age': 84,
    'city': 'london',
}

# 2. 列表嵌套: 将三个字典存储到一个名为 people 的列表中
people = [person_1, person_2, person_3]

# 3. 遍历列表: 访问列表中的每个字典
# 逻辑: 循环变量 person 依次代表列表里的每一个字典对象
for person in people:
    # 4. 格式化输出: 将姓名组合并打印详细信息
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")

# 作者: Enzo
# 日期: 2026-01-13