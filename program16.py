#program to find the first character of string that is not repeated

name=input("enter the string : ")
l=len(name)

for i in name:
        if name.count(i)>1:
            pass
        else:
            print(i)
            break
	
	