"""
文件名: dream_vacation.py
描述: 练习 7.10 - 梦想的度假胜地。调查用户并存储在字典中。
"""

# --- 练习 7.10: 梦想的度假胜地 ---

# 1. 初始化空字典
responses = {}

# 设置循环标志
polling_active = True

while polling_active:
    # 2. 获取名字和回答
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    # 3. 将答案存储在字典中
    # 💡 语法: 字典名[键] = 值
    responses[name] = response

    # 4. 询问是否还有其他人要参与
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 5. 调查结束，显示结果
print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")

# 作者: Enzo
# 日期: 2026-02-04