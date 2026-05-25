"""
文件名: user_albums.py
描述: 练习 8.8 - 在练习 8.7 的基础上结合 while 循环，接收用户交互式输入，动态创建并展示字典。
"""

# --- 练习 8.8: 用户的专辑 ---

def make_album(artist_name, album_title):
    """创建一个描述音乐专辑的字典"""
    return {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }

# 1. 数据交互: 开启 while 循环并提供退出途径 ('q')
print("--- 欢迎来到专辑创建系统（随时输入 'q' 退出程序） ---")

while True:
    artist = input("\n请输入歌手名称: ")
    if artist.lower() == 'q':
        print("程序安全退出，再见！")
        break
        
    title = input("请输入专辑名称: ")
    if title.lower() == 'q':
        print("程序安全退出，再见！")
        break
        
    # 2. 逻辑处理: 调用函数处理用户输入的数据，并打印生成的字典
    album = make_album(artist, title)
    print(f"💡 成功为您生成字典: {album}")

# 作者: Enzo
# 日期: 2026-05-25