# 引数と返り値
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 結果: Hello, Alice!

def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 結果: 30
# ※結果の確認だけなら以下でもOK
print(add(10, 20))

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # 結果: Hello, Guest!
greet("Alice")  # 結果: Hello, Alice!
