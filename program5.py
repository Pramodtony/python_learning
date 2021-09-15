# program to find whether number is armstrong number 

num=n=number=int(input('enter the number'))
count=0
sum=0
while number>0:
    number =number//10
    count=count+1
print('number of digits entered is  ',count) 
while n>0:
    sum=sum + (n%10) ** count
    n=n//10
if num==sum:
    print('armstrong number')
else:
    print('not a armstrong number')


    