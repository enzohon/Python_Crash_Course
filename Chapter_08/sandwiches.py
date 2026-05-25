"""
文件名: sandwiches.py
描述: 练习 8.12 - 编写接受任意数量实参的函数，演示星号 `*args` 元组打包机制。
"""

# --- 练习 8.12: 三明治 ---

# 1. 函数定义: 使用 *toppings 收集任意数量的食材
# 💡 核心: 形参名开头的星号让 Python 创建一个名为 toppings 的空元组，将收到的所有值都封装进去
def make_sandwich(*toppings):
    """概述顾客点的一系列三明治食材"""
    print("\n正在为您精心制作三明治，添加的食材如下：")
    for topping in toppings:
        print(f" 🥪 {topping}")

# 2. 调用函数三次，每次传递不同数量的实参
make_sandwich('cheese', 'tomato', 'lettuce')
make_sandwich('beef', 'mustard_sauce')
make_sandwich('bacon')

# 作者: Enzo
# 日期: 2026-05-25