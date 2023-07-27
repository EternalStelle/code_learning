# func(*x)可将任意的实参传递到函数，形成列表
def make_pizza(*toppings):
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("mushrooms", "green peppers", "extra cheese")
