# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы. 
a = int(input("Start"))  
b = int(input("End"))  
sch=0 
sch_count =0 
sn =0  
sn_count =0 
k=0  
s_nine =0 
for i in range(a,b): 
    if i%2==0: 
        sch +=i 
        sch_count+=1
    elif i%2!=0: 
        sn +=i 
        sn_count+=1 

    if i%9==0 :
        s_nine +=i
        k+=1 

print("Sum of even", sch, " their average", sch/sch_count) 
print("Sum of odd", sch, " their average", sn/sn_count) 
print("Sum of %9==0", s_nine, " their average", s_nine/k) 
# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины. 
l = int(input("String length")) 
s = input("Symbol") 
for i in range(0, l):
    print(s, "\n")
# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!» 
c = int(input("Enter the number"))  
def some_function():
    if c==7: 
        print("Bye")
        return
    elif c<0: 
        print("Number is negative")
    elif c==0: 
        print("Number is equal to zero")
    elif c>0: 
        print("Number is positive")
    
# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!» 
sot=[]
for i in range(0, 3):
    pr = int(input("Enter the number")) 
    def some_function1():
        if c==7: 
            print("Bye")
            return 
    
maxx = max(sot)
mminn = min(sot) 
s= sum(sot)
print("Max", maxx, "\nMin", mminn, "\nSum", s)

