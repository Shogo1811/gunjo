import os

if os.path.exists("util/example.txt"):
    print("ファイルが存在します。")
else:
    print("ファイルが存在しません。")
try:
    file = open("util/example.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("ファイルが見つかりませんでした。")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")
