a = int(input("Сколько спортсмен пробегает км сейчас?"))
b = int(input("Сколько спортсмен должен пробежать?"))
i = 1
print(f"{i} день: {a}")
while a < b:
    i += 1
    a = a * 1.1
    print(f"{i} день: {a:.2f}")
print(f"Количество дней = {i}")