# program to print  fibonacci series
print("program to print fibonacci series upto n ")
start=1
nex=0
n=int(input("enter the value of n"))
number=0
while number<n:
    number=start+nex
    if number<n:
        print(number)
    nex=start
    start=number