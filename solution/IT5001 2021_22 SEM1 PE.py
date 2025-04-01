# Part1

def compareDNA_I(dna1,dna2):
    ans=''
    l1,l2=len(dna1),len(dna2)
    l=min(l1,l2)
    for i in range(l):
        if dna1[i]==dna2[i]:
            ans+='*'
        else:
            ans+='.'
    return ans+'.'*abs(l1-l2)

def compareDNA_R(dna1,dna2):
    if not dna1 or not dna2:
        return '.'*max(len(dna1),len(dna2))
    d1=dna1[0]
    d2=dna2[0]
    return ('*' if d1==d2 else '.')+compareDNA_R(dna1[1:],dna2[1:])

# print(compareDNA_R('AGTCATATAC','ACTCATGTAA'))

# Part2

def local_peak_array_version(survey):
    s=[-1]+survey+[-1]
    l=len(s)
    for i in range(1,l-1):
        if s[i-1]<s[i]>s[i+1]:
            return i-1

def local_peak_function_version(a,b,survey):
    last=-1
    for i in range(a,b+1):
        curr=survey(i)
        if curr<last:
            return i-1
        last=curr
    return i



# print(local_peak_array_version([4,5,2,7,8,2,1,2,3,4,8])) 
# print(local_peak_array_version([1,2,3,4,5,6])) 

# survey1 = lambda i: [4,5,2,7,8,2,1,2,3,4,2][i] 
# print(local_peak_function_version(0,10,survey1))
# survey3 = lambda i: [1,2,3,4,5,6,5,4,3,2][i%10] 
# print(local_peak_function_version(1,9,survey3))
# print(local_peak_function_version(11,19,survey3)) 
# survey1 = lambda i: [1,2,3,4,5,6,7,8,9,10,11][i] 
# print(local_peak_function_version(0,10,survey1))


# Part3

# def nth_day_pw (N):
#     if N==1:
#         return 'F'
#     if N==2:
#         return 'B'
#     return nth_day_pw(N-2)+nth_day_pw(N-1)
# please use memo to avoid repeat calculation ;P

def nth_day_pw (N): #recursive
    memo={1:'F',2:'B'}
    def go(n):
        if n in memo:
            return memo[n]
        curr=go(n-2)+go(n-1)
        memo[n]=curr
        return curr
    return go(N)

def nth_day_pw (N): #iterative
    A='F'
    B='B'
    for _ in range(3,N+1):
        A,B=B,A+B
    return B if N>1 else A

def kth_letter_nth_day_pw(k,n):
    if k<=2:
        return 'BFB'[k+n%2-1] # for case of k<=2
    a,b='F','B'
    while len(b)<k: #from the pattern... password[i] for i>=2 (0-index) wont change, so we just get a "b" that have enough length will do
        a,b=b,a+b
    return b[k-1]

# print(nth_day_pw(10)) 
# print(nth_day_pw(40)[-20:]) 
# print(kth_letter_nth_day_pw(-1,50)) 

# print(kth_letter_nth_day_pw(2,6))
# print(kth_letter_nth_day_pw(3,8))
# print(kth_letter_nth_day_pw(123456789,99999))
# print(kth_letter_nth_day_pw(123456789,9875)) 