###################################################################### 
#Part 1  
def next_pos(pos,m):    
    c=[0,0,0]
    c[pos-1]=1
    if m=='A':
        c[0],c[1]=c[1],c[0]
    elif m=='B':
        c[1],c[2]=c[2],c[1]
    else:
        c[0],c[2]=c[2],c[0] 
    for i,v in enumerate(c):
        if v==1:
            return i+1
 
def final_pos_i(pos,seq):
    c=[0,0,0]
    c[pos-1]=1
    for m in seq:
        if m=='A':
            c[0],c[1]=c[1],c[0]
        elif m=='B':
            c[1],c[2]=c[2],c[1]
        else:
            c[0],c[2]=c[2],c[0]
    for i,v in enumerate(c):
        if v==1:
            return i+1

def final_pos_r(pos,seq): 
    if not seq:
        return pos   
    n=next_pos(pos,seq[0]) 
    return final_pos_r(n,seq[1:])

###################################################################### 
#Part 2  #you can use this for your test 
def tight_print(m):     
    for row in m:         
        print(''.join(row))  
        
def splash(no_r,no_c,radius,actions):   
    ans=[]
    for r in range(no_r):
        row=[]
        for c in range(no_c):
            curr=which_paint(no_r,no_c,radius,r,c,actions)
            row.append(curr)
        ans.append(row)

    return   ans

def which_paint(no_r,no_c,radius,r,c,actions): 
    ans='.'
    for color,i,j in actions:
        if (r-i)**2+(c-j)**2<=radius**2:
            ans=color
    return  ans 

def P2T4_answer():
    return 'H'  


###################################################################### 
#Part 3  #you can use this for your test 
def max_profit(lst):     
    ans=0
    min_=lst[0]
    for p in lst:
        if p<min_:
            min_=p
        ans=max(ans,p-min_)
    return ans   
A1 = [6, 11, 4, 1, 4, 9, 11, 12, 8, 5, 2, 3, 8, 13, 15, 14]
print(max_profit(A1)) 
A2 = [6, 11, 18, 1, 4, 3, 8, 13, 14]
print(max_profit(A2)) 

A3 = [i%1007 for i in range(1,10000)] 
print(max_profit(A3))
# end of template 