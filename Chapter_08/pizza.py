"""
文件名: pizza.py
描述: 练习 8.16 - 用于演示各种不同 import 语法的比萨制作功能模块。
"""

def make_pizza(size, *toppings):
    """概述要制作的比萨信息"""
    print(f"\n正在制作一个 {size} 英寸的比萨，配料包含：")
    for topping in toppings:
        print(f" - {topping}")