

def getNum(tab1,num):
    while num!=0:
        tab1.append(num)
        num=int(input('dose arithmo an thes na stamatisis dose 0: '))
    return tab1

#main

tab1=[]
num=int(input('dose arithmo an thes na stamatisis dose 0: '))
getNum(tab1,num)
print('i lista su ine avti: ',tab1)
x=len(tab1)
res=int(tab1[x-1])
for i in range(1,x):
    res=res**tab1[x-i]

print(str(res)[-1])
