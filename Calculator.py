x = int(input())
y = int(input())
z = str(input())
if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "pow":
    print(z ** y)
elif (z == "mod" or z == "div" or z == "/") and x == 0 or y == 0:
    print("Деление на 0")
elif z == "mod":
    print(z % y)
elif z == "div":
    print(z // y)
elif z == "/":
    print(z / y)