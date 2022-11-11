## Name    - Chandra Prakash
## Reg No  - 22-27-04
## Date    - 20 Oct 2022
## Program 

def knapsack(cp,n,W,V):
    if n==0 or cp==0:
        return 0
    
    if W[n-1]>cp:
        return knapsack(cp,n-1,W,V)
    else:
        return max(knapsack(cp-W[n-1],n-1,W,V)+V[n-1],knapsack(cp,n-1,W,V))

V = [60, 100, 120]
W = [10, 20, 30]
cp = 50
n = len(V)
print(knapsack(cp,n,W,V))



