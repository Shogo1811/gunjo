#クラス
class Dog:

    # 初期化メソッド（コンストラクタ）
    def __init__(self, name, age):
        self.name = name  # オブジェクトの属性
        self.age = age

    # メソッド
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)  # Dogクラスのインスタンス（オブジェクト）を作成

print(my_dog.name)  # 結果: Buddy
print(my_dog.age)   # 結果: 3


my_dog.bark()  # 結果: Buddy says woof!


# コンストラクタ__init__メソッド(例えの文)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # 結果: 2020 Toyota Corolla
