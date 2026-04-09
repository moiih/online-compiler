t = int(input())
result = []

for i in range(t):
    N = int(input())
    monkeys = list(map(int,input().split()))
    b = []
    c = []
    d = []
    
    for i in range(len(monkeys)):
        b.append(chr(i+97))
        c.append('1')
        d.append(chr(i+97))

    count = 0
    while True:
        for j in range(len(monkeys)):
            c[monkeys[j]-1] = b[j]

        for j in range(len(monkeys)):
            b[j] = c[j]

        count = count + 1
        if b == d:
            break
    result.append(count)

    b.clear()
    c.clear()
    d.clear()
    monkeys.clear()
    
for i in range(t):
    print(result[i])
