# program to get matching characters in a string

name=input("enter the string")
len=len(name)
s=[]

for i in range(0,len-1):
    count=1
    for j in range(i+1,len):
        if name[i]==name[j] :
            s.append(name[i])  
li=set(s)
print(li)        


'''
matchingchar=[]
for i in name:
    name.count(i)>1
    matchingchar.append(i)
print("matchingchar")
'''