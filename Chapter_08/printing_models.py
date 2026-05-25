"""
文件名: printing_models.py
描述: 练习 8.15 - 主程序文件。演示使用 from...import 语法导入特定函数并执行。
"""

# --- 练习 8.15: 打印模型 ---

# 1. 从刚才编写的独立模块中导入特定函数
from printing_functions import print_models, show_completed_models

# 2. 准备基础数据
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []

# 3. 执行导入的函数
print_models(unprinted, completed)
show_completed_models(completed)

# 作者: Enzo
# 日期: 2026-05-25