#program to find no of numerical digits in the string

name=input("enter the string : ")
count=0
num=['0','1','2','3','4','5','6','7','8','9']
for i in name:
    if i in num :
        count+=1
print(count)