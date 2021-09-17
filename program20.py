# program to find second largest element of an array

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

s_large=lst[0]
for i in lst:
        if i>=s_large and i<large:
            s_large=i
print("second largest element in the given array is",s_large)