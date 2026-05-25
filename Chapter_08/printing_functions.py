"""
文件名: printing_functions.py
描述: 练习 8.15 - 存放 3D 打印模型相关逻辑的独立公共函数模块。
"""

def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"正在打印 3D 模型: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示所有印刷好的 3D 模型"""
    print("\n--- 以下模型已成功印刷完成 ---")
    for model in completed_models:
        print(f" ✨ {model}")