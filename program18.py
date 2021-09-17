#delete the repeated elemets in an integer array

l=[]
n=int(input("enter the no of  elements you want to insert"))
for i in range(0, n):
        a=input("enter the {} value :".format(i))
        l.append(a)
lst=set(l)
l=list(lst)
print("Final list of elemets ",l)