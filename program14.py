# program to count the particular character in a string

name=input("enter the string : ")
count=0
ch=input("enter the single character you want to search in string : ")
for i in name:
    if i==ch:
        count+=1
print(count)