# with構文
with open("util/example.txt", "r") as file:
    content = file.read()
    print(content)

# withブロックを抜けると自動でfile.close()が呼ばれる

#　ファイルの書き込み
with open("util/example.txt", "w") as file:
    file.write("This is written using with statement.")
