def make_pizza(size, *toppings):
    print(f"Making a size of {size} -inch, with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")