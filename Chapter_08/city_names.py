"""
文件名: city_names.py
描述: 练习 8.6 - 编写 city_country() 函数，演示如何通过 return 语句返回格式化后的文本。
"""

# --- 练习 8.6: 城市名 ---

# 1. 函数定义: 接收城市和国家，返回格式化好的字符串
# 💡 技巧: 使用 return 返回值，能让函数具有更高的复用性，不仅限于直接向终端打印
def city_country(city, country):
    """返回格式如 'Santiago, Chile' 的字符串"""
    return f'"{city.title()}, {country.title()}"'

# 2. 调用函数并接收返回值: 分别传入三个不同的城市-国家对
result1 = city_country('santiago', 'chile')
result2 = city_country('tokyo', 'japan')
result3 = city_country('paris', 'france')

# 3. 打印接收到的返回值
print("--- 城市-国家格式化输出 ---")
print(result1)
print(result2)
print(result3)

# 作者: Enzo
# 日期: 2026-05-25