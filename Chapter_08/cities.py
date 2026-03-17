"""
文件名: cities.py
描述: 练习 8.5 - 进一步演示函数默认参数的使用
"""

# --- 练习 8.5: 城市 ---

# 1. 定义函数: 接受城市和国家，给国家设置默认值
# 💡 提示: 带有默认值的形参（country）必须放在没有默认值的形参（city）后面
def describe_city(city, country='Iceland'):
    print(f"{city.title()} is in {country.title()}.")

# 2. 调用函数: 为三座不同的城市调用这个函数
print("--- 城市描述 ---")

# 💡 逻辑: 前两个调用只提供城市名，国家使用默认的 'Iceland'
describe_city('reykjavik')
describe_city('kópavogur')

# 💡 技巧: 提供第二个实参来覆盖默认的国家值
describe_city('shanghai', 'china')

# 作者: Enzo
# 日期: 2026-03-17