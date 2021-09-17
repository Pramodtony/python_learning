# program to determine the factors of a number
number=int(input('enter your number'))
list=[]
for i in range(1,number+1):
    if number%i==0:
        list.append(i)
print("factors of {} is {}".format(number,list))
