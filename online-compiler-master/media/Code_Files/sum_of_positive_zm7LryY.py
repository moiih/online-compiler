val=[1,3,-9,3,-2,5]
i=0
sum=0
while True:
    if val[i] > 0:
        sum+=val[i]
    if i == len(val)-1:
        break
    i+=1
print("\n\tSum Of All Positive Numbers =",sum)
