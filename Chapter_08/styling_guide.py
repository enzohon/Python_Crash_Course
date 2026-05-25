"""
文件名: styling_guide.py
描述: 练习 8.17 - 编写符合 Python PEP 8 函数设计编写指南的代码范例。
"""

# --- 练习 8.17: 函数编写指南规范演示 ---

# 💡 规范 1: 函数名应只包含小写字母和下划线，具备清晰的描述性。
# 💡 规范 2: 每个函数定义下方应紧跟包含文档字符串的注释。
# 💡 规范 3: 给形参指定默认值或使用关键字实参时，等号 `=` 两边不要留有空格。
def calculate_total_price(price, tax_rate=0.08, discount=0.0):
    """
    计算商品的最终含税优惠总价。
    每个函数的代码行长度不应超过 79 字符。
    """
    discounted_price = price * (1 - discount)
    final_price = discounted_price * (1 + tax_rate)
    return round(final_price, 2)


# 💡 规范 4: 不同的函数定义之间，需要用两个空行隔开，以便于视线分离。
def display_bill(item_name, final_cost):
    """优雅地向用户展示账单"""
    print(f"项目: {item_name} | 最终应付金额: ￥{final_cost}")


# 代码调用示例
total = calculate_total_price(100, tax_rate=0.1, discount=0.2)
display_bill("Python 编程进阶课", total)

# 作者: Enzo
# 日期: 2026-05-25