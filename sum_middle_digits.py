## Date- 9 Sept 2022
## Reg No- 22-27-04
## Python program to print sum of Middle digits of given number

num = int(input("Enter the number: "))
n=str(num)
i=len(n)//2
if(len(n)%2==0):
    sum=int(n[i])+int(n[i-1])
else:
    sum=int(n[i])

print("Sum of middle digits: ", sum)


 