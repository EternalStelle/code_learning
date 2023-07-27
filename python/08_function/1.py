# def 定义函数，缩进部分为函数体
def greet_user():
    print("Hello!")


greet_user()


def greet_user(username):
    print(f"Hello, {username.title()}")


greet_user("jesse")


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet("hamster", "harry")
describe_pet("dog", "Willie")


# 在调用时，可直接使用关键字，此时与顺序无关
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")


# 定义函数时，可指定默认值，默认值放后
def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")


# describe_pet(pet_name='willie')亦可，此时无需提供animal_type内容
describe_pet("willie")
