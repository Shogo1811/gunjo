# f文字列(f-string)
name = "Bob"
print(f"こんにちは、私の名前は{name}です。")

# 三項演算子

x = 10
result = "大きい" if x > 5 else "小さい"
print(result)  # 結果: 大きい

# 以下の文を二行で書ける
x = 10
if x > 5:
   result = "大きい"
else:
   result = "小さい"
print(result)
#結果　大きい

# リスト内包表記
numbers = [1, 2, 3, 4]
squares = [n for n in numbers]
print(squares)
# 1 2 3 4

# 以下の文を三行で書ける
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
       squares.append(n)
print(squares)

# 以下はifとの組み合わせ
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers) # 結果: [0, 2, 4, 6, 8]

# 型アノテーション

# 型を明示してコードを読みやすく(引数、戻り値がstr intなど)
def add(x: int, y: int) -> int:
        return x + y

print(add(3, 5))
