# kassa =0 
# a5 = 5
# a10 = 10 
# a20 =20


# queue = [5, 10, 10, 20, 5]  
# queue = [5,5,5,10,20]
# kassa = queue[0] 
# flag = True

# for i in range(1, len(queue)): 
#     if queue[i]==5: 
#         kassa+=5 
#     elif kassa>=queue[i]-5 :
#         kassa= kassa + 5 - (queue[i]-5) 
#     else: 
#         print("Impossible\n") 
#         print("Thats the end", i)
#         flag = False
#         break 
# if flag: 
#     print("Success!") 



kassa = []  

a5 = 5
a10 = 10 
a20 =20 

queue = [5, 10, 10, 20, 5]  
kassa.append(queue[0])
flag = True

for i in range(1, len(queue)):
    if (queue[i]==5): 
        kassa.append(5)
    elif sum(kassa)>=queue[i]-5: 
        if  (queue[i]==a10) and (a5 in kassa): 
            kassa.remove(a5) 
            kassa.append(a10)
        elif (queue[i]==a20) and (a5 in kassa) and (a10 in kassa): 
            kassa.remove(a10)
            kassa.remove(a5) 
            kassa.append(a20) 
        else: 
            print("Impossible\n") 
            print("Thats the end", i)
            flag = False
            break  
    else:
        print("Impossible\n") 
        print("Thats the end", i)
        flag = False
        break 
if flag: 
    print("Success!") 

