import random 

items = [random.randint(-50, 100) for i in range(10)]  

mas_1=[]
mas_2=[] 
mas_3 = [] 
mas_4 = [] 

# • Сформировать  список, содержащий олько четные 
for i in items:
    if i%2==0:
        mas_1.append(i)
    else:
        mas_2.append(i) 
    if i<0:
        mas_3.append(i)
    else:
        if i>0:
            mas_4.append(i)
# • Сформировать  список, содержащий олько нечетные 
# • Сформировать  список, содержащий олько отрицательные 
# # • Сформировать  список, содержащий олько полож  
print("Origin", items)
print("1 ", mas_1)
print("2 ", mas_2)
print("3 ", mas_3)
print("4 ", mas_4)
