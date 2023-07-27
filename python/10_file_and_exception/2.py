#使用'w'即以写入模式打开文件，先清空原有内容
filename='programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
#使用'a'即以附加模式打开文件，将内容附在原内容后
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
