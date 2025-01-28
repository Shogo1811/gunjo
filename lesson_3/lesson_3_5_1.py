# TODO こちらのファイルは実行できません
# エラーとは
# 括弧の閉じ忘れ
print("Hello, World!"  # SyntaxError
# ゼロで割ろうとする
result = 10 / 0  # ZeroDivisionError

try:
    # エラーが発生する可能性のあるコード
    result = 10 / 0
except ZeroDivisionError:
    # エラー発生時の処理
    print("ゼロで割ることはできません。")
