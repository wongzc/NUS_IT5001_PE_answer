# Part1

def BMI(w,h):
    return w/(h**2)

def BMI_test_i(data):
    ans=[]
    for w,h in data:
        bmi=w/(h**2)
        if bmi<18.5:
            ans.append(1)
        elif bmi<25:
            ans.append(2)
        elif bmi<30:
            ans.append(3)
        else:
            ans.append(4)
    return ans

def BMI_test_r(data):
    if not data:
        return []
    bmi=data[0][0]/(data[0][1]**2)
    if bmi<18.5:
        curr=1
    elif bmi<25:
        curr=2
    elif bmi<30:
        curr=3
    else:
        curr=4
    return [curr] + BMI_test_r(data[1:])

def BMI_test_o(data):
    return [1 if w/(h**2)<18.5 else ( 2 if w/(h**2)<25 else (3 if w/(h**2)<30 else 4)) for w,h in data]


# Part2
def gen_board(r,c, mines):
    ans=[[0]*c for _ in range(r)]
    for r,c in mines:
        ans[r][c]='*'
    return ans

def hint_board(r,c,mines):

    ans=[[0]*c for _ in range(r)]

    def addRow(rr,cc):
        if cc>0:
            ans[rr][cc-1]+=1
        ans[rr][cc]+=1
        if cc<c-1:
            ans[rr][cc+1]+=1

    for rr,cc in mines:
        if rr>0:
            addRow(rr-1,cc)
        addRow(rr,cc)
        if rr<r-1:
            addRow(rr+1,cc)
    return ans
            

def play_ms(r,c,mines,moves):
    ans=[['#']*c for _ in range(r)]
    board=gen_board(r,c, mines)
    hint=hint_board(r,c,mines)
    def open(rr,cc):
        
        if rr<0 or rr>r-1 or cc<0 or cc>c-1:
            return 
        curr=hint[rr][cc]
        if board[rr][cc]=='*':
            ans[rr][cc]='X'
            return False
        elif curr>0:
            ans[rr][cc]=curr
            return True
        elif ans[rr][cc]==' ':
            return True
        else:
            ans[rr][cc]=' '
            open(rr+1,cc+1)
            open(rr+1,cc)
            open(rr+1,cc-1)
            open(rr,cc+1)
            open(rr,cc-1)
            open(rr-1,cc+1)
            open(rr-1,cc)
            open(rr-1,cc-1)
            return True
    for rr,cc in moves:
        if not open(rr,cc):
            break
    return ans
        
def m_tight_print(m): # You should not submit this function     
    for row in m:         
        print(''.join(map(str,row))) 

    
# m_tight_print(gen_board(6,11,((4,6),(1,2),(3,3)))) 
# print(' ')
# m_tight_print(hint_board(6,11,((4,6),(1,2),(3,3)))) 
# print(' ')
# m_tight_print(play_ms(6,11,((4,6),(1,2),(3,3)), ((0,0),))) 
# print(' ')
# m_tight_print(play_ms(6,11,((4,6),(1,2),(3,3)), ((0,0),(0,2),(0,3),(0,4)))) 
# print(' ')
# m_tight_print(play_ms(6,11,((4,6),(1,2),(3,3)), ((0,0),(0,2),(1,2),(0,4))))      


# Part3
def original_schedule(n,reduced_schedule): 
    rest=[]
    j=0
    lj=len(reduced_schedule)
    for i in range(n):
        if i+1 in reduced_schedule:
            continue
        while j<lj and reduced_schedule[j]<i+1:
            rest.append(reduced_schedule[j])
            j+=1
        rest.append(i+1)
    return tuple(rest)
    
# print(original_schedule(7,(6,4,2,1)))
# print(original_schedule(5,(1,4,2))) 
# print(original_schedule(3,(1,2))) 