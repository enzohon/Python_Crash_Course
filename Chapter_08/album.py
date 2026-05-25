"""
文件名: album.py
描述: 练习 8.7 - 编写 make_album() 函数，演示如何构建并返回字典，同时支持默认值为 None 的可选形参。
"""

# --- 练习 8.7: 专辑 ---

# 1. 函数定义: 接收歌手名、专辑名，以及可选的歌曲数量 (song_count)
# 💡 技巧: 将可选形参的默认值设为 None。在条件测试中，None 被视为 False
def make_album(artist_name, album_title, song_count=None):
    """创建一个描述音乐专辑的字典"""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    # 如果调用时指定了歌曲数，则将该键值对动态添加到字典中
    if song_count:
        album_dict['songs'] = song_count
    return album_dict

# 2. 基础调用: 创建三个不包含歌曲数量的专辑字典并打印
print("--- 1. 创建不包含歌曲数的常规专辑 ---")
album1 = make_album('jay chou', 'jay')
album2 = make_album('taylor swift', '1989')
album3 = make_album('michael jackson', 'thriller')
print(album1)
print(album2)
print(album3)

# 3. 带可选参数的调用: 创建一个包含歌曲数量的专辑字典
print("\n--- 2. 创建包含歌曲数的完整专辑 ---")
album_full = make_album('eason chan', 'u87', song_count=10)
print(album_full)

# 作者: Enzo
# 日期: 2026-05-25