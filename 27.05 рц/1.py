li = [word.strip(".,!?:;-").lower() for word in input().split()]
di = {word: li.count(word) for word in li}
m = min(di.values())

for k, v in sorted(di.items(), key=lambda t: t[0]):
    if v == m:
        print(k)
        break

d, l = {}, []
# ----------------------------------------------------------------------------------------

n = int(input()) 
mas = []
while n>0: 
    b = input()
    bn = int(input()) 
    while bn>0:
        mas.append(b) 
        bn = bn-1
    n=n-1
print(mas)