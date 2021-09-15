# program to check whether string is a palindrome or not

str1=input("enter the string")
print("The string you have entered is '{}' ".format(str1))
str2=str1[::-1]
if str1==str2 :
    print('palindrome')
else:
    print('not a palindrome')

