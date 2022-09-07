## Lab-2 Intelligent Algo
## Date- 6 Sept 2022
## Reg No- 22-27-04
## Insertion Sort in Python

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1

arr=[5,4,2,1,3]
insertion_sort(arr)
print(arr)

