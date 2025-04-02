# Part 1
def goodMatchI(fpp,mpp):
    ans=''
    l=len(fpp)
    for i in range(l):
        if fpp[i]==mpp[i]:
            ans+='C'
        else:
            ans+='X'
    return ans

def goodMatchR(fpp,mpp):
    if not fpp or not mpp:
        return ''
    return ('C' if fpp[0]==mpp[0] else 'X')+goodMatchR(fpp[1:],mpp[1:])

def maxRotationalGoodMatch(fpp,mpp):
    ans=0
    l=len(fpp)
    for i in range(l):
        curr=0
        for j in range(l):
            curr+=(fpp[j]==mpp[(i+j)%l]) #the i is added after each full comparison
        ans=max(ans,curr)
    return ans

# f1 = ['INFP','INFP','ENTP','ENFJ','INFP','ENFJ']
# m1 = ['INFP','INTP','ENFJ','ISFJ','INFP','INFP']
# print(goodMatchI(m1,f1)) 
# print(goodMatchR(m1,f1)) 
# print(maxRotationalGoodMatch(f1,m1)) 

# Part 2
def maxAnyCombGoodMatch(fpp,mpp):
    ans=0
    f={}
    for fp in fpp:
        if fp in f:
            f[fp]+=1
        else:
            f[fp]=1

    m={}
    for mp in mpp:
        if mp in m:
            m[mp]+=1
        else:
            m[mp]=1
    for k,v in m.items():
        ans+=min(v,f.get(k,0))
    return ans

# print(maxAnyCombGoodMatch(f1,m1)) 

# Part 3

# L1         8,             9
# L2     88,     89,     98,    99
# L3  888,889,898,899,988,989,998,999

def nthAuspiciousNum(n):
    accum=2
    layerGap=2
    layer=1
    while n>accum: # we use this to know how many layer (L) needed to cover our target
        layer+=1
        layerGap*=2 # the gap between layer is 2,4,8,16, ....
        accum+=layerGap
    adjusted_n=n-(accum-layerGap)-1 # then we check the # of our target at its layer

    ans=0
    for i in range(layer):
        huat=8
        if adjusted_n%2: # look at the pyramid again, if in l3, adjusted_n is 3 (899), it must from l2 1 (89)
            huat+=1 
        ans+=huat*10**i # from top to bottom, there is only 2 route, 0: add 8, 1: add 9
        adjusted_n=adjusted_n//2
    return ans
    
    

# print(nthAuspiciousNum(1),8)
# print(nthAuspiciousNum(3),88)
# print(nthAuspiciousNum(4),89)
# print(nthAuspiciousNum(5),98)
# print(nthAuspiciousNum(8),889)
# print(nthAuspiciousNum(10),899)
# print(nthAuspiciousNum(59))
# print(nthAuspiciousNum(10**20))  