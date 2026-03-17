"""
文件名: t_shirt.py
描述: 练习 8.3 - 演示如何向函数传递位置实参和关键字实参
"""

# --- 练习 8.3: T恤 ---

# 1. 定义函数: 接受尺码和字样
def make_shirt(size, message):
    # 💡 提示: 使用 f-string 格式化输出，让打印结果更易读
    print(f"\n制作了一件 {size} 码的 T 恤，上面印着的字样是: '{message}'。")

# 2. 使用位置实参调用函数
# 💡 注意: 位置实参必须严格按照形参定义的顺序传递（先尺码，后字样）
print("--- 使用位置实参 ---")
make_shirt('M', 'Hello World')

# 3. 使用关键字实参调用函数
# 💡 技巧: 关键字实参允许打乱传递顺序，只要明确指定参数名即可
print("\n--- 使用关键字实参 ---")
make_shirt(message='Python Rocks', size='S')

# 作者: Enzo
# 日期: 2026-03-17