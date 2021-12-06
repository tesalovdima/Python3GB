n = int(input("Enter the number:"))
m = 0
while n != 0:
    i = n % 10
    if m < i:
        m = i
    n = n // 10
print(m)
