"""
文件名: cars.py
描述: 练习 8.14 - 编写 make_car() 函数，将位置实参与任意数量关键字形参完美结合。
"""

# --- 练习 8.14: 汽车 ---

# 1. 函数定义: 总是接受制造商(manufacturer)和型号(model)，还可以接受任意数量的关键字参数
def make_car(manufacturer, model, **car_info):
    """将一辆汽车的信息存储在字典中并返回"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# 2. 按照题目所给的规范格式，使用位置和关键字实参进行调用
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# 3. 打印返回的字典，确认识别并正确处理了所有的车辆配置信息
print("--- 生成的汽车配置字典信息 ---")
print(car)

# 作者: Enzo
# 日期: 2026-05-25