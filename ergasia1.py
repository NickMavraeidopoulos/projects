from __future__ import division
import random



def setTable(m):
    tabNum = []
    
    for i in range(100):
        tabNum.append(random.sample(m,5))
    return tabNum
    
def findNum(tabNum):
    athr=[0]*100
    k=False
    sumy=0
    while k==False:
        x=random.randint(0,80)
        sumy=sumy+1
        for i in range(100):
            if x in tabNum[i]:
                athr[i]+=1
                if athr[i]==5:
                    k=True
    return sumy
    
         
sumx=0
for k in range(1000):
    m=range(1,81)
    sumx=sumx+findNum(setTable(m))
print (sumx/1000)

