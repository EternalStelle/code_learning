class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_descriptive_name())


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 此处odometer_reading为默认值0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")


my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 可直接修改值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 可定义方法来修改值
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 此处odometer_reading为默认值0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        # 判断mileage是否大于原值，否则不更新
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")


my_new_car = Car("audi", "a4", "2019")
my_new_car.update_odometer(24)
print(f"This car has {my_new_car.odometer_reading} miles on it")
my_new_car.update_odometer(23)


# 可定义方法对属性的值递增
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 此处odometer_reading为默认值0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        # 判断mileage是否大于原值，否则不更新
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", "2019")
my_new_car.increment_odometer(23)
my_new_car.read_odometer()
