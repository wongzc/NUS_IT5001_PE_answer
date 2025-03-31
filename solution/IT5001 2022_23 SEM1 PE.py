# part1
def fizz_i(factor1,n):
    ans=[]
    for i in range(1,n+1):
        if i%factor1==0:
            ans.append('Fizz')
        else:
            ans.append(i)
    return ans

def fizz_r(factor1,n):
    if n==0:
        return []
    if n%factor1==0:
        return fizz_r(factor1,n-1)+['Fizz']
    return fizz_r(factor1,n-1)+[n]

fizz_l = lambda factor1,n: [i if i%factor1 else 'Fizz' for i in range(1,n+1)]

def fizzbuzz(factor1,factor2,n):
    ans=[]
    for i in range(1,n+1):
        curr=''
        if i%factor1==0:
            curr+='Fizz'
        if i%factor2==0:
            curr+='Buzz'
        if curr=='':
            ans.append(i)
        else:
            ans.append(curr)
    return ans

# part2
# hmmm, TBD again
def clean_text(filename,minlen):
    ans=[]
    capWord=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    smallWord=list('abcdefghijklmnopqrstuvwxyz')
    d={capWord[i]:smallWord[i] for i in range(26)}
    with open(filename) as file:
        lines=file.readlines()
        for line in lines:
            word_list=line.split() # this will fail testcase if we use split(' '), not sure why though....
            for word in word_list:
                updated_word=''
                for char in word:
                    if char in capWord:
                        updated_word+=d[char]
                    elif char not in smallWord:
                        if len(updated_word)>minlen:
                            ans.append(updated_word)
                        updated_word=''
                    else:
                        updated_word+=char
                if len(updated_word)>minlen:
                    ans.append(updated_word)
    return ans


def text_analytics(clean_text_list,n):
    if not clean_text_list:
        return {0:{}}
    d={}
    for w in clean_text_list:
        if w in d:
            d[w]+=1
        else:
            d[w]=1
    dd={}

    for k,v in d.items():
        if v in dd:
            dd[v].add(k)
        else:
            dd[v]={k}
        
    c=list(dd.keys())
    c.sort(reverse=True)

    ans={}

    for i in c[:n]:
        ans[i]=dd[i]
    return ans

# part3
def str_to_two_d(pic):
    return [[c for c in row] for row in pic]

def two_d_to_str(pic):
    return [''.join(c) for c in pic]


def pic_diff(pic1,pic2):
    m1=len(pic1)
    m2=len(pic2)
    n1=len(pic1[0])
    n2=len(pic2[0])
    m=max(m1,m2)
    n=max(n1,n2)
    ans=[]
    for i in range(m):
        row=''
        for j in range(n):
            if i>=m1 and j>=n2:
                row+='0'
            elif i>=m2 and j>=n1:
                row+='0'
            elif i>=m1 or j>=n1:
                row+='2'
            elif i>=m2 or j>=n2:
                row+='1'
            elif pic1[i][j]==pic2[i][j]:
                row+='='
            else:
                row+='X'
        ans.append(row)
    return ans

def count_cells(pic):
    pic=[[j for j in i] for i in pic]
    m=len(pic)
    n=len(pic[0])
    def bfs(i,j):
        if i<0 or i>=m or j<0 or j>=n or pic[i][j]=='#':
            return
        pic[i][j]='#'
        bfs(i-1,j)
        bfs(i+1,j)
        bfs(i,j-1)
        bfs(i,j+1)
        
    ans=0
    for i in range(m):
        for j in range(n):
            if pic[i][j]=='.':
                ans+=1
                bfs(i,j)
    return ans