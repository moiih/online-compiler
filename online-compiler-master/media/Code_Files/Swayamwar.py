N = int(input())
st1 = str(input())
st2 = str(input())
temp = N
n = N
flag = 0

for i in range(N):
    for j in range(N):
        if st1[i] == st2[j]:
            print(i)
            temp -= 1
            flag = 1
            #st1.remove(st1[i])
            st2.remove(st2[j])
            break

    if flag == 0:
        break

print(temp)
