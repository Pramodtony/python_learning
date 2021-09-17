# program to check if the two strings are anagrams

str1=input("enter the string1")
str2=input("enter the string2")

for i in str1:
	if i in str2 and len(str1)==len(str2):
		continue
	else:
		print("not anagrams")
		break
else:
    print("anagrams")