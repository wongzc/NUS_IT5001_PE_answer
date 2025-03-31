# part1

def RLD_I(s):
    res=''
    for i in range(len(s)//2):
        char=s[2*i]
        count=int(s[2*i+1])
        res+=char*count
    return res
        
def RLD_R(s):
    if not s:
        return ''
    return s[0]*int(s[1])+RLD_I(s[2:])


# part2
def num_divisor_list(d):
    res=[]
    for j in range(d+1):
        c=0
        for i in range(1,j+1):
            if not j%i:
                c+=1
        res.append(c)
    return res
def list_of_max_divisor(d):
    res=[]
    max=0
    for j in range(d+1):
        c=0
        for i in range(1,j+1):
            if not j%i:
                c+=1
        if c==max:
            res.append(j)
        elif max<c:
            max=c
            res=[j]
    return res
    
def how_many_prime(d):
    ans=0
    for i in range(2,d+1):
        add=True
        for j in range(2,i):
            if not i%j:
                add=False
                break
        if add:
            ans+=1
    return ans

# part3
# def magicPotionTreatment(h1,h2): 
#     if h1<h2:
#         return 'A'*(h2-h1)
#     elif h1%2:
#         return 'A'+magicPotionTreatment(h1+1,h2)
#     elif h1==h2:
#         return ''
#     else:
#         return 'B'+magicPotionTreatment(h1//2,h2)
# love recursion but sadly this is goning to fail the testcase due to the depth limitation LOL
    
def magicPotionTreatment(h1,h2):
    ans='' 
    while h1>h2:
        if h1%2:
            ans+='A'
            h1+=1
        else:
            ans+='B'
            h1=h1//2
    if h1<h2:
        return ans+'A'*(h2-h1)
    return ans
    