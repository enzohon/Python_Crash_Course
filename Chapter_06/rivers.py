"""
文件名: rivers.py
描述: 练习 6.5 - 演示遍历字典的三种不同方式 (.items, .keys, .values)
"""

# --- 练习 6.5: 河流 ---

# 1. 数据准备: 创建河流与国家的映射字典
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

# 2. 任务一: 打印完整句子 (使用 .items)
# 💡 技巧: 需要同时用到河流名和国家名
print("=== The Sentences ===")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 3. 任务二: 只打印河流名字 (使用 .keys)
# 逻辑: 只需要字典的键
print("\n=== The Rivers ===")
for river in rivers.keys():
    print(river.title())

# 4. 任务三: 只打印国家名字 (使用 .values)
# 逻辑: 只需要字典的值
print("\n=== The Countries ===")
for country in rivers.values():
    print(country.title())

# 作者: Enzo
# 日期: 2026-01-13