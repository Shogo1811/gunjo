# 応用(組み合わせ)
for i in range(5):
    if i % 2 == 0:
        print(f"{i}は偶数")
    else:
        print(f"{i}は奇数")

for i in range(5):
    if i == 2:
        continue  # iが2のときはスキップ
    print(i)
