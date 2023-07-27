# 可从文件中导入类，此处从car.py中导入Car类
from car import Car

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
# 一个car.py文件中可包含多个类
from car import ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2019)
my_tesla.battery.describe_battery()
# 可从一个文件中导入多个类
from car import Car, ElectricCar

my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())
# 可导入整个文件，即导入整个模块
import car

my_beetle = car.Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())
# 可导入模块中的所有类，与前文类似，此时不必输入模块名调用类，不建议使用
from car import *

my_beetle = Car("volkswagen", "beetle", 2019)
# 可在模块中导入其他模块
# 可使用别名
from car import ElectricCar as ec

my_tesla = ec("tesla", "model s", 2019)
