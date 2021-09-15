# program to print prime numbers between 1 and n
n=int(input('enter the value of n'))
print("The prime numbers between 1 and {} are ".format(n))
for i in range (2,n):
    count=0
    for j in range (2,i+1):
        if i%j ==0:
            count=count+1
    if count==1:
        print(i,end =" ")
    
        