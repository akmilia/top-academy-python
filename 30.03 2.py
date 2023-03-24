from random import randint
# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/ 

operation = input("Enter operation using space as separator: ")
oper = operation.split()  
if len(oper) != 3: 
    print("Invalid")
else:
    num1 = int(oper[0])
    operator = oper[1]
    num2 = int(oper[2])

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid operator. Please enter a valid operator (+, -, *, /).")
# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран. 
rd = [] 
for i in range(20): 
    rd.append(randint(0, 20))

print(rd)
count_pos = 0
count_pos = sum(True for i in rd if i > 0)
count_neg = 0
count_neg = sum(True for i in rd if i < 0)
count_zero= 0
count_zero = sum(True for i in rd if i == 0) 

maxx = max(rd)
minn = min(rd)

print(
    "pos:",count_pos, 
    "neg:",count_neg, 
    "zero:",count_zero, 
    "max", maxx,
    "min", minn
)