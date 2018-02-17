def rot13(i,text):
    text2 = []
    for k in range(i):
        num=ord(text[i-(i-k)])
        num2=num
        if (num>=65 and num<=90):
            num2=num+13
            if(num2>90):
                num2=65+((num+12)-90)
        if (num>=97 and num<122):
            num2=num+13
            if(num2>122):
                num2=97+((num+12)-122)
        print(chr(num2),end='')
        #text2.append(chr(num2))
    
        
#main
text=[]
text=input('dose kimeno: ')
i=len(text)
rot13(i,text)
