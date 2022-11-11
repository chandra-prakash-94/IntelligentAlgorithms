## Name    - Chandra Prakash
## Reg No  - 22-27-04
## Date    - 20 Oct 2022
## Program - Knapsack

def knapsack(Cp,weights,values):
    ratios= [v/w for v,w in zip(values,weights)]
    n=len(weights)
    #index = list(range(n))
    max_value=0
    fractions=[0]*n
    for i in range(n):
        if weights[i]<=Cp:
            max_value+=values[i]
            Cp-=weights[i]
            fractions[i]=1
        else:
            fractions[i]=Cp/weights[i]
            max_value+=values[i]*fractions[i]

    print(fractions)
    print(max_value)


weights=[10,20,30]
values=[60,100,120]
Cp=50
knapsack(Cp,weights,values)





