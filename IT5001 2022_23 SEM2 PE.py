#part1

def plinko_i(seq,b,m,s):
    if not b or not m or not s:
        return 0
    for i,p in enumerate(seq):
        if p==0:
            b-=1
        elif p==1:
            m-=1
        elif p==2:
            s-=1
        if not b or not m or not s:
            return i+1
    return len(seq)
        
def plinko_r(seq,b,m,s):
    if not b or not m or not s:
        return 0
    if not seq:
        return 0
    p=seq[0]
    if p==0:
        b-=1
    elif p==1:
        m-=1
    elif p==2:
        s-=1
    return 1+plinko_r(seq[1:],b,m,s)

def plinko_general(seq,prizes):
    prizeList=list(prizes)
    for i,p in enumerate(seq):
        prizeList[p]-=1
        if prizeList[p]==0:
            return i+1
    return len(seq)

# print(plinko_r((1, 1, 2, 2, 0, 2, 0, 1, 2, 1),2,3,5))
# print(plinko_r((0,0,0,0,0,1,0,1,2),6,2,2))
# print(plinko_r((0,1,2,0,1,2),3,3,2))
# print(plinko_general((0,1,2,0,1,2),(99,99,99))) 
# print(plinko_general((0,1,2,0,1,2,0,1,2,2,2,1,1,0,1),(4,3,4))) 
# print(plinko_general((0,1,3,2,1,2,3,4,5,4),(2,3,3,3,1,5))) 

#part2

def fragment(filename,word):
    with open(filename) as f:
        frag=set([i.strip() for i in f.readlines()])
    ans=[]
    for i in range(1,len(word)):
        if (word[:i] in frag) and (word[i:] in frag):
            ans.append((word[:i],word[i:]))
    return ans
# print(fragment('fragment_simple.txt','umbrella'))
# print(fragment('fragment1.txt','python')) 
# print(fragment('fragment_all2.txt','board')) 
# print(fragment('fragment_all3.txt','board')) 


#part3

def total_perimeter(mp):
    m=len(mp)
    n=len(mp[0])
    mp=[[i for i in j] for j in mp]
    def bfs(i,j):
        curr=0
        mp[i][j]='X'
        if i<=0 or mp[i-1][j]==0:
            curr+=1
        elif mp[i-1][j]==1:
            curr+=bfs(i-1,j)
        
        if i>=m-1 or mp[i+1][j]==0:
            curr+=1
        elif mp[i+1][j]==1:
            curr+=bfs(i+1,j)
        
        if j<=0 or mp[i][j-1]==0:
            curr+=1
        elif mp[i][j-1]==1:
            curr+=bfs(i,j-1)
        
        if j>=n-1 or mp[i][j+1]==0:
            curr+=1
        elif mp[i][j+1]==1:
            curr+=bfs(i,j+1)
        return curr
    ans=0
    for i in range(m):
        for j in range(n):
            if mp[i][j]==1:
                ans+=bfs(i,j)
    return ans
    
def max_island_perimeter(mp):
    m=len(mp)
    n=len(mp[0])
    mp=[[i for i in j] for j in mp]
    def bfs(i,j):
        curr=0
        mp[i][j]='X'
        if i<=0 or mp[i-1][j]==0:
            curr+=1
        elif mp[i-1][j]==1:
            curr+=bfs(i-1,j)
        
        if i>=m-1 or mp[i+1][j]==0:
            curr+=1
        elif mp[i+1][j]==1:
            curr+=bfs(i+1,j)
        
        if j<=0 or mp[i][j-1]==0:
            curr+=1
        elif mp[i][j-1]==1:
            curr+=bfs(i,j-1)
        
        if j>=n-1 or mp[i][j+1]==0:
            curr+=1
        elif mp[i][j+1]==1:
            curr+=bfs(i,j+1)
        return curr
    ans=0
    for i in range(m):
        for j in range(n):
            if mp[i][j]==1:
                ans=max(ans,bfs(i,j))
                
    return ans


# map0 = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]] 
# print(total_perimeter(map0))
# map1 = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]] 
# print(total_perimeter(map1))
# map2a =[[1, 1, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1]]
# print(total_perimeter(map2a))