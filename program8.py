# program to reverse a number
num=number=int(input("enter the number"))
count=0
sum=0
while number>0:
    number =number//10
    count=count+1
print('number of digits entered is  ',count) 
while count>=1:
    a=num%10
    sum=sum+(a*10**(count-1))
    num=num//10
    count-=1
print('reverse of entered number is ',sum)