# вводится число и границы диаппазона 
a = int(input("Start"))
b = int(input("End"))
c = int(input("Number")) 
if a>=b:
    print("Error")
else: 
    while True: 
        c = int(input("Number")) 
        if c>b or c<a:
            print("Error")
        else:
            False
for i in range(a, b):
    if (i!=c):
        print(i, " ") 
    else:
        print("!", i, "! ") 


# если число не входит в него, то выводится сообщение об ошибке и просьба ввести заново(  пока не будет правильно)
# после чего все числа диапазона выводятся, а введеное число выделяется знаками