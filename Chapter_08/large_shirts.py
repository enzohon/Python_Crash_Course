"""
文件名: large_shirts.py
描述: 练习 8.4 - 演示在函数中使用默认参数值 (Default Values)
"""

# --- 练习 8.4: 大号 T 恤 ---

# 1. 修改函数: 为尺码和字样添加默认值
# 💡 技巧: 这样在调用函数时，如果省略了对应的实参，Python 就会使用默认值
def make_shirt(size='大号', message='I love Python'):
    print(f"\n制作了一件 {size} 的 T 恤，上面印着的字样是: '{message}'。")

# 2. 制作默认的大号 T 恤
# 💡 逻辑: 不传递任何实参，全部使用默认值
print("--- 默认的大号 T 恤 ---")
make_shirt()

# 3. 制作默认字样的中号 T 恤
# 💡 逻辑: 只通过位置实参覆盖尺码，字样依然使用默认值
print("\n--- 中号 T 恤 ---")
make_shirt('中号')

# 4. 制作其他字样的 T 恤 (尺码无关紧要)
# 💡 逻辑: 覆盖了默认的尺码和字样
print("\n--- 其他字样的 T 恤 ---")
make_shirt(size='小号', message='Coding is Fun')

# 作者: Enzo
# 日期: 2026-03-17