# // Задание 1
# // Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# // остатка) нужно вывести слово Fizz. Если число кратно 5
# // нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# // вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# // вывести само число. 
# // Если пользователь ввел значение не в диапазоне от 1
# // до 100 требуется вывести сообщение об ошибке. 

a = int(input("Between 1 and 100"))  

if a>100 or a<1: 
    print("Poshel nafig tupoi chitst ne umeet")
else:
    if a%3==0: 
        print("Fizz")
    elif a%5==0: 
        print("Buzz")
    elif a%5==0 and a%3==0: 
        print("Fizz Buzz") 
    elif a%5!=0 and a%3!=0: 
        print(a) 


# // Задание 2
# // Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# // до седьмой включительно.
# // Задание 3
# // Написать программу подсчета стоимости разговора
# // для разных мобильных операторов. Пользователь вводит
# // стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.
# // Домашнее задание
# // 1
# // Задание 4
# // Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# // 1000 — 8%. Пользователь вводит с клавиатуры уровень
# // продаж для трех менеджеров. Определить их зарплату,
# // определить лучшего менеджера, начислить ему премию
# // 200$, вывести итоги на экран.