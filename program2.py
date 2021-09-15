# program to reverse a string

str1=input("enter the string")
length=len(str1)
print("The string you have entered is '{}' ".format(str1))
'''while length>=0:
    print(str1[length-1], end='')
    length=length-1 '''
    
'''print('reverse og entered string is ',str1[::-1])'''

reverse =""
for i in str1:
    reverse=i+reverse
print(reverse)