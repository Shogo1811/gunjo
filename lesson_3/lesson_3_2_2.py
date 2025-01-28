# リスト
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # 結果: apple
fruits.append("orange")
print(fruits)  # 結果: ['apple', 'banana', 'cherry', 'orange']
fruits[0] = "kiwi"
print(fruits)  # 結果: ['kiwi', 'cherry', 'orange']

# for文
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
