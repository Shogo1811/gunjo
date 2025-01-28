# スコープ(ローカルスコープ、グローバルスコープ)
def example():
    x = 10  # xはローカル変数
    print(x)

example()  # 結果: 10
# print(x)  # エラー: NameError: name 'x' is not defined

x = 5  # xはグローバル変数

def example():
    print(x)  # グローバル変数xを参照

example()  # 結果: 5

x = 5

def modify_global():
    global x
    x = 10

modify_global()
print(x)  # 結果: 10
