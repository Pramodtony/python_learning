#program to swap two numbers without using third variable
num1,num2=input("enter the values of two numbers").split(",")
print("before swapping",num1,num2)
num1=int(num1)
num2=int(num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("after swapping ",num1,num2)