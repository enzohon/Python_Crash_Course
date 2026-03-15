"""
文件名: slices.py
描述: 练习 4.10 - 演示 Python 列表的切片操作 (Slicing)
"""

# --- 练习 4.10: 切片 ---

# 1. 数据准备：创建一个包含多个元素的列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 2. 头部切片：获取前三个元素
# 💡 注意: [:3] 实际上取的是索引 0, 1, 2，不包含索引 3
print("The first three items in the list are:")
print(players[:3])

# 3. 中部切片：获取中间三个元素
# 逻辑: 列表长度为5，中间索引为 1, 2, 3，因此切片范围是 [1:4]
print("\nThree items from the middle of the list are:")
print(players[1:4])

# 4. 尾部切片：获取末尾三个元素
# 💡 技巧: 使用负数索引 [-3:] 是最通用的写法，无论列表多长都能取到最后3个
print("\nThe last three items in the list are:")
print(players[-3:])

# 作者: Enzo
# 日期: 2026-1-11