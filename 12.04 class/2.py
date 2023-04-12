mas = [1,2,1,4,3,2,1,4] 

s = 0 
i=0
j = len(mas)-1  


while j>i:
    s=max(s, min(mas[i], mas[j])*(j-i))
    if mas[i]<mas[j]:
        i+=1 
    else: 
        j-=1 


print("Max sq = ", s) 

#3*3 
#2*2
#