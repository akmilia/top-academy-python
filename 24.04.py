# #должна быть рекурсия
# def fill(mat, new_val, x, y):
#
#     if  (x>3 or x<0) or (y>3 or y<0) or mat[y][x] == new_val:
#         return
#     mat[y][x] = new_val
#     fill(mat, new_val, x-1, y)
#     fill(mat, new_val, x+1, y)
#     fill(mat, new_val, x, y-1)
#     fill(mat, new_val, x, y+1)
#
# matrix = [
#     [1,0,0,1],
#     [1,1,0,1],
#     [0,1,1,1],
#     [0,0,0,0]
# ]
# print(matrix)
# fill(matrix, 1, 2,0)
#
# print(matrix)
# expect = [
#     [1,1,1,1],
#     [1,1,1,1],
#     [0,1,1,1],
#     [0,0,0,0]
# ]
#


mas = [0, 1, 0, 3, 12]
l = len(mas)-1
#l=4
for i in mas:
    if i==0:
        if mas[l]==0:
            l=l-1
        i, mas[l] = mas[l], i
        print(mas)

        #mas = [12, 1, 0, 3, 0]
        # mas = [12, 1, 3, 0, 0]
# for i in range(l-1):
#     if mas[i]>mas[i+1]:
#         buf = mas[i]
#         mas[i] = mas[i+1]
#         mas[i + 1] = buf

print(mas)

# i=0
# for j in range(len(mas)):
#     if mas[j]==0:
#         i==j
#


