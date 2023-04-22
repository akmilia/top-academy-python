
from random import randint
# Задание 1
# Два списка целых заполняются случайными
# числами. 


import numpy as np 
arrn =[]
arrm=[] 

for i in arrn:
    arrn.append(randint(0,50)) 
for i in arrm:
    arrm.append(randint(0,50))


# Необходимо:
# • Сформировать третий список, содержащий элементы обоих списков; 
arr1 = np.arrn()
arr2 = np.arrm()

print(np.concatenate ((arr1, arr2))) 
# • Сформировать третий список, содержащий элементы обоих списков без повторений;  
arr5=[]
for i in np.concatenate ((arr1, arr2)): 
    if i in arr5==False: 
        arr5.append(i)
print("arr5 ", arr5)
# • Сформировать третий список, содержащий элементы общие для двух списков;
arr4=[]
for i in arr1: 
    if i in arr2:
        arr4.append(i) 
print("arr4 ", arr4)
# • Сформировать третий список, содержащий
# только уникальные элементы каждого из списков; 
arr3=[]
for i in arr1: 
    if i in arr2==False:
        arr3.append(i) 
for j in arr2:
    if j in arr1==False:
        arr3.append(i) 
print("arr3 ", arr3)
# • Сформировать третий список, содержащий
# только минимальное и максимальное значение
# каждого из списков 
minn = min(arr1) 
minnn = min(arr2) 
maxx = max(arr1) 
maxxx=max(arr2) 
last_task=[minn, minnn, maxx, maxxx] 
print("last_task", last_task)