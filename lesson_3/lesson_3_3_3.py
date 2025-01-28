# 辞書(dict)
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])  # 結果: Alice
person["age"] = 26
print(person)  # 結果: {'name': 'Alice', 'age': 26, 'city': 'New York'}
person["email"] = "alice@example.com"
print(person)  # 結果: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
del person["city"]
print(person)  # 結果: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
