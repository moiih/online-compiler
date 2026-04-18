                       # Seating Conginent Problem

S = int(input("Enter The No. Of Seats >>> "))
N = int(input("Enter The Size Of Contingent >>> "))
K = int(input("Enter People For Wet Seats >>> "))
M = int(input("Enter Blocks OF Seats >>> "))

block = []
for i in range(M):
    element = int(input())
    block.append(element)

n1 = N-K
k1 = K
temp = 0
count1 = 1

for i in range(M):
    c = 0
    flag = 0
    count2 = count1
    for j in range(temp,M):

        if n1 <=0 and k1 <= 0:
            print("~~~~~~Hye")
            flag = 1
            break

        if j%2 == 0:

            if n1 != 0:
                if n1 >= block[j]:
                    n1 = n1 - block[j]
                    c = c + block[j]
                    count2 = count2 + block[j]
                else:
                    c = c + n1
                    n2 = n1
                    n1 = 0
                    if k1 == 0: 
                        count2 = count2 + n2
                    elif k1 != 0:
                        count2 = count2 + block[j] 
                        
            elif n1 == 0:
                count2 = count2 + block[j]
                
        if j%2 != 0:

            if k1 != 0:
                if k1 >= block[j]:
                    k1 = k1 - block[j]
                    c = c + block[j]
                    count2 = count2 + block[j]
                else:
                    c = c + k1
                    k2 = k1
                    k1 = 0
                    if n1 == 0: 
                        count2 = count2 + k2
                    elif n1 != 0:
                        count2 = count2 + block[j] 
                    
            elif k1 == 0:
                count2 = count2 + block[j]

    temp = temp + 1
    n1 = N-K
    k1 = K

    if flag == 1:
        print("~~~~~~~~~count2 = ",count2-1)
        print("~~~~~~~~~count1 = ",count1)
        if i == 0:
            smallest = count2-count1-1
        else:
            if smallest > count2-count1-1:
                smallest = count2-count1-1
        print("\n\tDifference = ",count2-count1-1)
    #print("\n\tc = ",c)
    #print("\n\tcount1 = ",count1)
    #print("\n\tcount2 = ",count2)
    count1 = count1 + block[i]

print("\n\n**************************************************************")
print("\t\tResult = ",smallest)
print("**************************************************************")
