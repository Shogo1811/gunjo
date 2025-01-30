# 継承
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Animalクラスを継承
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):  # Animalクラスを継承
    def speak(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # 結果: Buddy barks
cat.speak()  # 結果: Whiskers meows
