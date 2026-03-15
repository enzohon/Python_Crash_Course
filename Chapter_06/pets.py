"""
文件名: pets.py
描述: 练习 6.8 - 创建多个宠物字典并存储在列表中遍历
"""

# --- 练习 6.8: 宠物 ---

# 1. 数据准备: 创建多个表示宠物的字典
# 💡 每个字典包含宠物的类型 (kind) 和主人 (owner)
pet_1 = {'kind': 'dog', 'owner': 'john'}
pet_2 = {'kind': 'cat', 'owner': 'sarah'}
pet_3 = {'kind': 'hamster', 'owner': 'mike'}
pet_4 = {'kind': 'parrot', 'owner': 'lisa'}

# 2. 列表存储: 将字典放入 pets 列表
pets = [pet_1, pet_2, pet_3, pet_4]

# 3. 遍历输出: 打印关于每个宠物的信息
print("=== 🐾 Pet Registry ===")
for pet in pets:
    # 技巧: 使用 .title() 让输出更美观
    print(f"\nType of animal: {pet['kind'].title()}")
    print(f"Owner's name: {pet['owner'].title()}")

# 作者: Enzo
# 日期: 2026-01-13