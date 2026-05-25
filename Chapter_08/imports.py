"""
文件名: imports.py
描述: 练习 8.16 - 演示 Python 官方支持的 5 种不同的模块与函数导入方法。
"""

# --- 练习 8.16: 导入的五种方式 ---

print("=== 方式 1: import module_name ===")
import pizza
pizza.make_pizza(12, 'pepperoni')

print("\n=== 方式 2: from module_name import function_name ===")
from pizza import make_pizza
make_pizza(16, 'mushrooms', 'green peppers')

print("\n=== 方式 3: from module_name import function_name as fn ===")
from pizza import make_pizza as mp
mp(14, 'extra cheese')

print("\n=== 方式 4: import module_name as mn ===")
import pizza as p
p.make_pizza(10, 'seafood')

print("\n=== 方式 5: from module_name import * ===")
# ⚠️ 提示：在大型项目中不建议使用这种方法，容易引发当前作用域内变量和函数名冲突
from pizza import *
make_pizza(8, 'onions')

# 作者: Enzo
# 日期: 2026-05-25