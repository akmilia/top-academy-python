
print("1 ")
print("enter day")
print(1,2,3,4,5,6,7)
q=int(input())
if(q==1):
    print("M")
elif(q==2):
    print("T")
elif(q==3):
    print("W")
elif(q==4):
    print("TH")
elif(q==5):
    print("F")
elif(q==6):
    print("S")
elif(q==7):
    print("Su")
else:
    print("ОШИБКА, введите нужную цифру")

print("2 ")
print("enter month")
print(1,2,3,4,5,6,7,8,9,10,11,12)
w=int(input())
if(w==1):
    print("J")
elif(w==2):
    print("F")
elif(w==3):
    print("M")
elif(w==4):
    print("A")
elif(w==5):
    print("May")
elif(w==6):
    print("June")
elif(w==7):
    print("July")
elif(w==8):
    print("A")
elif(w==9):
    print("S")
elif(w==10):
    print("O")
elif(w==11):
    print("N")
elif(w==12):
    print("D")
else:
    print("you are wrong")

print("3 ")
print("enter")
y=int(input())
if(y>0):
    print("Number is positive")
elif(y<0):
    print("Number is negative")
else:
    print("Number is equal to zero")

print("4 ")
print("enter 2 numbers")
a=int(input())
b=int(input())
if(a==b):
    print("Они равны")
elif(a>b):
    print(a,b)
else:
    print(b,a)