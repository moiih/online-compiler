'''  TEST CASE:
5
5,1
1,1,3,1,5,1
0,0
1,1,3,1,5,1
1,1
5
ACNE
PLEAS
EVEN
CALVE
EVADE


5
1,1
1,1,3,2
0,0
1,1,3,2
0,0
5
ASIAN
RISEN
FEAR
CLAWS
FALLS  '''

N = int(input())
c = []
cross = []
for i in range(N):
  c = []
  c = input().split(",")
  cross.append(list(map(lambda x:int(x)-1, c)))


M = int(input())
word = []
d = {}
for i in range(M):
  word.append(input())
  d[word[i]] = len(word[i])
  

# Beta
print("\n")
print(d)


print("\n")
board = []
board_2 = []
for i in range(N):
    inc = 0
    ele = []
    ele_2 = []
    for j in range(N):
        
        ele_2.append(0)
        if inc < len(cross[i]) and j == cross[i][inc]:
            s = 0
            for k in range(0,cross[i][inc+1]+1):
                ele.append('X')
            s = s + 1
            inc = inc + 2
        else:
            ele.append(0)
    board.append(ele)  # For Actual Board
    board_2.append(ele_2)  # For transpose of "board"
      

# Beta
for i in range(N):
  print (end = '\n')
  for j in range(N):
    print(board[i][j], end = ' ')
# Beta
print("\n")
for i in range(N):
  print (end = '\n')
  for j in range(N):
    print(board_2[i][j], end = ' ')


# For Direction Recording
direction = {}
flag_A = 0
flag_D = 0
flag = 1
inc = 1
for i in range(N):
    for j in range(N):
        if board[i][j] != 'X':
            
            if ( (j == 0 and board[i][j+1] == 0) or (j+1 < N and board[i][j-1] == 'X' and board[i][j+1] == 0) ):
                board[i][j] = inc
                temp_inc = inc
                inc = inc + 1
                #flag = 1
                flag_A = 1
            if ( (i == 0 and board[i+1][j] == 0)  or (i+1 < N and board[i-1][j] == 'X' and board[i+1][j] == 0) ):
                if flag_A != 1:
                    board[i][j] = inc
                    temp_inc = inc
                    inc = inc + 1
                    #flag = 1
                flag_D = 1

            if flag_A == 1 and flag_D ==0:
                direction[ board[i][j] ] = 'A'
                flag_A = 0
            if flag_D == 1 and flag_A == 0:
                direction[ board[i][j] ] = 'D'
                flag_D = 0
            if flag_A == 1 and flag_D == 1:
                direction[ board[i][j] ] = 'AD'
                flag_A = 0
                flag_D = 0

        board_2[j][i] = board[i][j] # For storing transpose of "board"




# Now For Length Of Each Solution Number
length = {}
temp_len = []
flag_A = 0
flag_D = 0
flag_AD = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != 'X' and board[i][j] != 0:
            if direction[ board[i][j] ] == 'A':
                flag_A = 1
                #flag_M = 0
            if direction[ board[i][j] ] == 'D':
                flag_D = 1
                #flag_M = 0

            #if flag_A == 1 and flag_D == 1:
            if direction[ board[i][j] ] == 'AD':
                flag_AD = 1
                

            if flag_A == 1 or flag_AD == 1:
                count = 0
                for k in range(j,N):
                    if board[i][k] == 'X':
                        break
                    else:
                        count = count + 1
                    
                if flag_AD == 1:
                    temp_len.append(count)
                else:
                    length[ board[i][j] ] = count


            if flag_D == 1 or flag_AD == 1:
                count = 0
                k = 0
                for k in range(i,N):
                    if board_2[j][k] == 'X':
                        break
                    else:
                        count = count + 1
                        
                if flag_AD == 1:
                    temp_len.append(count)
                else:
                    length[ board[i][j] ] = count


            if flag_AD == 1:
                length[ board[i][j] ] = temp_len
                
                    
        flag_A = 0
        flag_D = 0
        flag_AD = 0
                    
                
# For Beta Test
print("\n")
for i in range(N):
  print (end = '\n')
  for j in range(N):
    print(board[i][j], end = ' ')


print("\n")
print(direction)  # [  'A ', 'D', 'AD' ] 
print("\n")
    
for i in range(N):
    print(end = '\n')
    for j in range(N):
        print(board_2[i][j],end=' ')

print("\n")
print(length) 



for i in range(N):
    for j in range(N):
        if board[i][j] != 'X' and board[i][j] == 0:
            
            if direction[i][j] == 'A':
                for 
            








