n1 = int(input())
action = input()
n2 = int(input())
if action == "+":
    print(n1 + n2)
elif action == "-":
    print(n1 - n2)
elif action == "*":
    print(n1 * n2)
elif action == "/":
    if n2 == 0:
        print('На ноль делить нельзя! \n Введите другое число:')
        print(n1 / int(input()))
    else:
        print(n1 / n2)
else:
    print("Ошибка ввода. Проверьте введенные значения.")
