from module1 import *
name = input("Введите ваше имя: ")
name_number, name_values = calculate_name_number(name)
print(f"Число вашего имени: {name_number}")

print("Расшифровка имени:")
for c in name_values:
    print(f"{c}: {name_values[c]}")
   
filename=str(name_number) +".txt"