"""
文件名: restaurant_seating.py
描述: 练习 7.2 - 餐馆订位。根据人数判断是否有空桌。
"""

# --- 练习 7.2: 餐馆订位 ---

# 1. 询问用餐人数
# 💡 注意: input() 返回的是字符串，需要用 int() 转换为数字才能比较大小
number = input("How many people are in your dinner group? ")
number = int(number)

# 2. 进行条件判断
if number > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")

# 作者: Enzo
# 日期: 2026-02-04