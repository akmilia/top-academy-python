#написать программу конвертер валют, сделать общение с пользователем через меню 
print("Hello, Im the currency converter \n Lets get to business! \n Chooose your currency")
flag = True
while (flag):
    #print("1.RUB \n 2.DOL \n 3.EUR \n 4.UAN \n 5.Exit" )
    a = int(input("1.RUB \n 2.DOL \n 3.EUR \n 4.UAN \n 5.Exit")) 
    if a==5:
        break
    print("Then choose a desired currency")
    b = int(input("1.RUB \n 2.DOL \n 3.EUR \n 4.UAN \n 5.Exit"))  
    if b==5:
        break
    c = int(input("Enter the sum "))

