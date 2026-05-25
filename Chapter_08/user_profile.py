"""
文件名: user_profile.py
描述: 练习 8.13 - 编写接受任意数量关键字实参的函数，演示双星号 `**kwargs` 字典打包机制。
"""

# --- 练习 8.13: 用户简介 ---

# 1. 函数定义: 使用 **user_info 接收未知数量的任意名-值对
# 💡 核心: 形参开头的两个星号让 Python 创建一个名为 user_info 的空字典，将所有的附加实参装入其中
def build_profile(first, last, **user_info):
    """构建一个包含我们已知的一切用户信息的字典"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

# 2. 调用函数: 传入固定的姓氏、名字，并自由附加 3 个用来描述自己的键值对
my_profile = build_profile(
    'kris', 'wu',
    location='Tokyo',
    field='Artificial Intelligence',
    hobby='Guitar'
)

# 3. 打印返回的字典
print("--- 成功生成个人简介字典 ---")
print(my_profile)

# 作者: Enzo
# 日期: 2026-05-25