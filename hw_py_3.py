
# Задание 1
# Пользователь вводит с клавиатуры три цифры.
# Необходимо создать число, содержащее эти цифры. Например, если с клавиатуры введено 1, 5, 7,
# тогда нужно сформировать число 157. 
n = input("1st number")
n1 = input("2nd number")
n2 = input("3rd number")  
nn = (n+n1+n2) 
mn = (n, n1, n2) 
print(nn, mn)

# Задание 2
# Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр. Например, если с клавиатуры введено
# 1324, тогда результат произведения 1*3*2*4 = 24.
# Задание 3
# Пользователь вводит с клавиатуры количество метров. Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили. 
metres = double(input()) 
print("сантиметры", metres/100,  "дециметры", metres/10, "миллиметры", metres/1000,  "мили", )
# Задание 4
# Напишите программу, вычисляющую площадь
# треугольника. Пользователь с клавиатуры вводит размер основания треугольника и размер
# высоты.  
a = int(input()) 
h = int(input()) 

print("Square ", a*h/2)

# Задание 5
# Пользователь с клавиатуры вводит четырёхзначное число. Необходимо перевернуть число и отобразить результат. Например, если введено 4512, 

a = input() 
print(a.reverse())