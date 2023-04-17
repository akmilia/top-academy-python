# f = open('test.txt', 'r+')
# strin = f.read()
# stringi = list(strin)
#
# for i in range(len(stringi)):
#     if stringi[i].isupper() and i!=0:
#         im = stringi[i].lower()
#         ind = stringi.index(stringi[i])
#         stringi[ind]=im
#
#         stringi.insert(i,'_')
#
# f.truncate()
# f.write(''.join(stringi))
# f.close()
#
# f = open('test.txt', 'r')
# print("\n", f.read())
#
#
# flag = True
# while flag:
#     a = input("Enter the date ")
#     arr = list(a)
#     print("Arr", arr)
#     if len(arr)!=10:
#         print("Error, to long or to short")
#         break
#     for i in arr:
#         if i.isalpha():
#             print("Error, any text")
#             break
#
#     for i in range(len(arr)):
#             if i==2 and arr[i].isdigit():
#                 print("Error, i==2 ")
#                 break
#             if i==5 and arr[i].isdigit():
#                 print("Error, i==5 ")
#                 break
#             else:
#                 arr2=a.split('.')
#                 print(arr2, "arr2")
#
#                 if int(arr2[2]) % 4== 0:
#                     if arr2[1]=="02":
#                         if int(arr2[0])>29 or int(arr2[0])<0:
#                             print("Error, february is dead")
#                             break
#                 else:
#                     if arr2[1]=="02":
#                         if int(arr2[0])>28 or int(arr2[0])<0:
#                             print("Error, february is dead 2 ")
#                             break
#
#                 if int(arr2[1])>12 or int(arr2[1])<0:
#                     print("Error, monthes are out")
#                     break
#                 elif int(arr2[1])==1 or int(arr2[1])==3 or int(arr2[1])==5 or int(arr2[1])==7 or int(arr2[1])==8 or int(arr2[1])==10 or int(arr2[1])==12:
#                         if int(arr2[0])>31 or int(arr2[0])<0:
#                             print("Days are out")
#                             break
#                 elif int(arr2[1])==4 or int(arr2[1])==6 or int(arr2[1])==9 or int(arr2[1])==11:
#                         if int(arr2[0])>30 or int(arr2[0])<0:
#                             print("Error, february is dead")
#                             break
#
#                 print("You survived, ok")
#                 flag = False
#                 break
#
#





mas = [1, 7, 2, 8, 9 ] 
# mas = [1, 2, 7, 8 . 9 ] 

mas_pos = [1,3,4,2,0]
tmp = [0, 0, 0, 0, 0]

j=0

for i in  range(len(mas)):
        tmp[mas_pos[j]] = mas[i]
        j+=1
print(tmp)

