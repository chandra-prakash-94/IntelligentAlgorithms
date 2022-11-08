## Name   -  Chandra Prakash
## Reg No -  22-27-04
## Date   -  05 Nov 2022
## Python Program - Simple QuickSort           

def quick_sort(sequence):
    length = len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    items_greater=[]
    items_lower=[]
    for item in sequence:
        if item>pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

arr=[2,5,6,3,4]
sorted_lst=quick_sort(arr)
print(sorted_lst)


