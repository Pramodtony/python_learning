#program to find the missing number in an array from 1 to 10
arr=[1,2,3,4,5,6,8,9,10]
n=int(input("enter the last number in the array"))
sum=n*(n+1)//2

s=0
for i in arr:
	s=s+i
print("missing number is ",sum-s)
