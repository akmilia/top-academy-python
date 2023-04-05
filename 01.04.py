import random 
import numpy as np

# Задание 1
# Два списка целых заполняются случайными
# числами. 
def ran(items, n):
    items = [random.randint(0, 100) for i in range(n)]
    return items
k =5
mas_1=[]
mas_2=[] 

print(ran(mas_1,k)) 
print(ran(mas_2,k))

# Необходимо:
# • Сформировать третий список, содержащий элементы обоих списков; 

mas_3 = [] 

#create two arrays
mas_11 = np.mas_1
mas_22 = np.mas_2

#concatentate the two arrays
print(np.concatenate ((mas_11, mas_22)))

# • Сформировать третий список, содержащий элементы обоих списков без повторений; 

in_first = set(mas_1)
in_second = set(mas_2)

in_second_but_not_in_first = in_second - in_first

result = mas_1 + list(in_second_but_not_in_first)
print(result)  
# • Сформировать третий список, содержащий элементы общие для двух списков;  
k=0 
mas_t=[]
for i in mas_1:
    for j in mas_2:
        if i==j:
            mas_t[k] = i
            k+=1 
print("Together without dif ", mas_t)
# • Сформировать третий список, содержащий
# только уникальные элементы каждого из списков; 
k=0 
r=0
mas_r=[]
for i in mas_1:
    for j in mas_2:
        if i==j:
            k+=1 
    if k==0:
        mas_r[r] = i
        r+=1
print("Together smth else ", mas_r)
# • Сформировать третий список, содержащий
# только минимальное и максимальное значение
# каждого из списков. 

min_1=min(mas_1)
min_2=min(mas_2) 
max_1=max(mas_1)
max_2=max(mas_2) 

massssss = [min_1, min_2, max_1, max_2] 
print("MAsssss", massssss)