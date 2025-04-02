# Part1
def digitProductI(n):
    ans=1
    while n:
        ans*=max(n%10,1)
        n=n//10
    return ans

def digitProductR(n):
    if not n:
        return 1
    return  max(n%10,1)* digitProductR(n//10)


def finalDPI(n):
    while n>9:
        n=digitProductI(n)
    return n

def finalDPR(n):
    if n>9:
        n=finalDPR(digitProductR(n))
    return n

# print(digitProductI(808)) 
# print(digitProductI(2**200-1)) 

# print(digitProductR(808)) 
# print(digitProductR(2**200-1)) 

# print(finalDPI(808)) 
# print(finalDPI(2**200-1)) 

# print(finalDPR(808)) 
# print(finalDPR(2**200-1)) 

# Part2
def createFilledMatrix(r,c,char):
    return [[char]*c for _ in range(r)]

def thickening(pic):
    m=len(pic)
    n=len(pic[0])
    def check(i,j):
        if i<0 or i>=m or j<0 or j>=n:
            return False
        if pic[i][j]=='#':
            return True
        return False
    for i in range(m):
        for j in range(n):
            if pic[i][j]=='#':
                continue
            if (check(i,j-1) or check(i,j+1) 
                or check(i+1,j+1) or check(i+1,j) or check(i+1,j-1) 
                or check(i-1,j+1) or check(i-1,j) or check(i-1,j-1)):
                pic[i][j]='X'
    pic=[['#' if i=='X' else i for i in row] for row in pic]
    return pic

def thinning(pic):
    m=len(pic)
    n=len(pic[0])
    def check(i,j):
        if i<0 or i>=m or j<0 or j>=n:
            return True
        if pic[i][j]=='.':
            return True
        return False
    for i in range(m):
        for j in range(n):
            if pic[i][j]=='.':
                continue
            if (check(i,j-1) or check(i,j+1) 
                or check(i+1,j+1) or check(i+1,j) or check(i+1,j-1) 
                or check(i-1,j+1) or check(i-1,j) or check(i-1,j-1)):
                pic[i][j]='X'
    pic=[['.' if i=='X' else i for i in row] for row in pic]
    return pic

# pic0 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
# pic = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.'], ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.'], ['.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
# def mTightPrint(m):
#     for r in m:
#         print(''.join(r))

# tpic = thickening(pic) 
# mTightPrint(tpic)

# ttpic = thickening(tpic)
# mTightPrint(ttpic) 

# pic2 = thinning(ttpic) 
# mTightPrint(pic2) 

# pic3 = thinning(pic2) 
# mTightPrint(pic3) 

# pic4 = thinning(pic3) 
# mTightPrint(pic4)

# pic5 = thinning(pic4)
# mTightPrint(pic5)

# Part3
import math

def LCM(S):
    result = S[0]
    for i in range(1, len(S)):
        result = result * S[i] // math.gcd(result, S[i])
    return result

def LCM(S):
    def prime_factors(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = factors.get(i, 0) + 1
                n //= i
            i += 2
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors


    return 


l= [i for i in range(3,250000,5)]
print(LCM(l)%(10**10))
import sys
sys.set_int_max_str_digits(60000)
print(len(str(LCM(l))))

import math
import time
import sys
sys.set_int_max_str_digits(60000)

m=[0]*12

def check(res,fac):
    count=0
    while res%fac==0:
        res=res//fac
        count+=1
    c=m[fac]
    if count>c:
        m[fac]=count
    return res
    
def lcm(a, b):
    if a%b==0:
        return a
    return a * b // math.gcd(a, b)

def list_lcm(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        curr=lst[i]
        result=check(result,2)
        result=check(result,3)
        result=check(result,7)
        # result=check(result,11)

        
        curr=check(curr,2)
        curr=check(curr,3)
        curr=check(curr,7)
        # curr=check(curr,11)

        result = lcm(result, curr)
    return result*(2**m[2])*(3**m[3])*(7**m[7])*(11**m[11])

start = time.time()
l = [i for i in range(3, 250000, 5)]
print("Computing LCM...")
result = list_lcm(l)
print("LCM:", len(str(result)))
print("Time taken:", time.time() - start, "seconds")
print(l[:30])
print(m)