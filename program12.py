#program to calculate no of vowels and consonants in a string

name=input("enter the string")
c_cnt=v_cnt=0

for i in name:
	if i in ['a','e','i','o','u']:
		v_cnt+=1
	else:
		c_cnt+=1
print("Total vowels count and consonants count in the given string '{}' is {} and {} respectively".format(name,v_cnt,c_cnt))