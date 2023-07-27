# 可把列表传递给函数
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


users = ["hannah", "ty", "margot"]
greet_users(users)


# 先定义函数显示输出
# 可输入print_models(unprinted_models[:], completed_models)
# 这样可把列表副本传输给函数，而不是更改原列表内容
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


# 定义函数显示最后结果
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_models = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
