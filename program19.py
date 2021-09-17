# determine the largest and smallest element in an array

lst=[]
n=int(input("enter the no of  elements you want to insert"))
for i in range(1, n+1):
        a=input("enter the value no {} :".format(i))
        lst.append(a)
large=lst[0]
for i in lst:
        if i>=large:
            large=i
print("largest element in the given array is",large)
small=lst[0]
for i in lst: 
        if i<=small:
            small=i
print("smallest element in the given array is",small)
