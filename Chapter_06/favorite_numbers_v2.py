"""
文件名: favorite_numbers_v2.py
描述: 练习 6.10 - 修改练习 6.2，让每个人可以有多个喜欢的数字
"""

# --- 练习 6.10: 喜欢的数 (升级版) ---

# 1. 数据定义: 值现在是一个列表 [...]，而不是单个数字
favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    'hank': [3, 99, 101], 
}

# 2. 遍历字典: 获取人名和数字列表
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    
    # 3. 遍历列表: 将该人的所有数字逐个打印
    # 💡 技巧: 这种结构非常适合处理 "一对多" 的关系
    for number in numbers:
        print(f"  > {number}")

# 作者: Enzo
# 日期: 2026-01-13