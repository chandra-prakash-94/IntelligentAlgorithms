## Lab-2 Intelligent Algo
## Date- 8 Sept 2022
## Reg No- 22-27-04
## Merge Sort in Python

import time
import random
list1 = [random.randint(1,1000) for i in range(1000)]

def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            list1[k]=left_list[i]
            i=i+1
            k=k+1
        while j<len(right_list):
            list1[k]=right_list[j]
            j=j+1
            k=k+1

start = time.time()
mergesort(list1)
stop= time.time()
print(list1)
print("Total time taken: ", round((stop-start),6))
