#program to find factorial of a number

n=number=int(input('enter the number '))
fact=1
if number==0 :
    print('factorial of {} is {}'.format(n,fact))
elif number>0 :
    while number>0:
        fact =fact*number
        number=number-1
    print('factorial of {} is {}'.format(n,fact))
else: 
    print('the number you have entered is invalid')