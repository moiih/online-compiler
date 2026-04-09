N = int(input())
a = list(map(int,input().split()))
digit = []
bits = []
for i in range(N):
  n = a[i]
  for r in range(3):
    temp = n % 10
    n = n // 10
    digit.append(temp)
    if r == 0:
      small = digit [r]
      large = digit [r]
    else:
      if digit[r] < small:
        small = digit[r]
      if digit[r] > large:
        large = digit[r]
  digit.clear()
  large = large * 11
  small = small * 7
  total = small + large
  if len(str(total)) > 2:
    total = total % 100
  bits.append(total)
  
count = 0
for i in range(N):
    j = i+2
    while j < N:
      if  bits[i] // 10 == bits[j] // 10:
        count = count + 1
        break
      j = j + 2
      
print(count)
