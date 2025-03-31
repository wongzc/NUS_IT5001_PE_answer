#part 1
def dial_i(start,seq): 
    for dir, deg in seq:
        if dir=='CCW':
            start-=deg
        else:
            start+=deg
        
    return start%360 

def dial_r(start,seq): 
    if not seq:
        return start%360
    if seq[0][0]=='CCW':
        start-=seq[0][1]
    else:
        start+=seq[0][1]

    return dial_r(start,seq[1:])

def dial_u(start,seq): 
    return (start + sum([i[1] for i in filter(lambda x: x[0]=='CW',seq)])- sum([i[1] for i in filter(lambda x: x[0]=='CCW',seq)]))%360

# print(dial_u(45,[('CCW',135),('CW',45)]))

# seq1 = [('CW',40),('CW',100),('CCW',10),('CW',30),('CCW',20),('CW',180)] 
# print(dial_u(70,seq1))
# print(dial_u(350,seq1)) 

#part 2
def prefix(s1,s2):
    l=min(len(s1),len(s2))
    for i in range(l):
        if s1[i]!=s2[i]:
            return False
    return True

def check_prefix(seq):
    d={}
    for word in seq:
        curr=d
        for w in word:
            check=curr.get(w)
            if check:
                if '#' in check:
                    return True
            else:
                check={}
                curr[w]=check
            curr=check
        curr[w]='#'

    return False
            
def check_prefix(seq):
    seq.sort()
    l=len(seq)
    for i in range(l-1):
        m=min(len(seq[i]),len(seq[i+1]))
        check=True
        for j in range(m):
            if seq[i][j]!=seq[i+1][j]:
                check=False
                break
        if check:
            return True

    return False


# print(prefix('abc','abcdz'))
# print(prefix('abc','kkkabc'))
# print(prefix('xyzabc','xyz')) 
# passwords1 = ['abc','assfs','asfjl','xy987x','12312','jxljb','11515'] 
# print(check_prefix(passwords1)) 
# print(check_prefix(passwords1+['abcdk'])) 
# from itertools import permutations as perm 
# from time import time 
# passwords2 = list(perm(['a','b','c','d','e','f','g','h','i'])) 
# print(len(passwords2))  
# print(passwords2[:10])
# st = time() 
# print(check_prefix(passwords2)) 
# print("Time: ",time()-st)  
# st = time() 
# print(check_prefix(passwords2+[passwords2[-1]*2])) 
# print("Time: ",time()-st) 

# part3

def checkered_flag(r,c,s):
    ans=[]
    for rr in range(r):
        row=[]
        for cc in range(c):
            divR=rr//s%2
            divC=cc//s%2
            if divC==divR:
                row.append('#')
            else:
                row.append(' ')
        ans.append(row)
    return ans


def black_area(r,c,s):
    col=[0,0]
    
    for cc in range(c):
        col[cc//s%2]+=1
    ans=0
    for rr in range(r):
        for cc,c in enumerate(col):
            divR=rr//s%2
            divC=cc%2
            if divC==divR:
                ans+=c
    return ans


# from pprint import pprint
# pprint(checkered_flag(5,7,2)) 
# pprint(checkered_flag(8,10,3)) 
# print(black_area(5,7,2)) 
# print(black_area(8,10,3)) 
# print(black_area(21073,31171,8)) 
# print(black_area(723847,1213111,114)) 