from module1 import *
name = input("Введите ваше имя: ")
name_number, = calculate_name_number(name)
print(f"Число вашего имени: {name_number}")


   
filename = str(name_number) + ".txt"
with open(filename, 'r', encoding="utf-8-sig") as file:
    contents = loe_failist(filename)
    print(contents)

   