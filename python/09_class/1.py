# Python中首字母大写代表类，类中的函数称为方法
# __init__方法在每次根据类创建新实例时可自动执行
# self形参可自动传递，只需给name和age提供值
# self.后的获取与形参self相关的值
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")


my_dog = Dog("willie", 6)
print(f"My dog 's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()
your_dog = Dog("lucy", 3)
print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()