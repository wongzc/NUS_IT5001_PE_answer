# part1
def encode_I(word):
    d={c:i for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    d[' ']=99
    ans=''
    for w in word:
        x=d[w]
        if x<10:
            ans+='0'
        ans+=str(x)
    return ans
# print(encode_I('HI SALLY')=="0708991800111124")
# print(encode_I('ARE YOU FREE FOR DINNER TONIGHT')=="00170499241420990517040499051417990308131304179919141308060719")
def encoding_R(word):
    d={c:i for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    d[' ']=99
    if not word:
        return ''
    curr=d[word[0]]
    return ('0' if curr<10 else '')+str(curr)+encoding_R(word[1:])


# part2
def decode(msg, offset):
    offset=offset%26
    l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l=l[-offset:]+l[:-offset]
    d={}
    for i,c in enumerate(l):
        if i<10:
            k='0'+str(i)
        else:
            k=str(i)
        d[k]=c
    d['99']=' '
    ans=''
    for i in range(len(msg)//2):
        ans+=d[msg[2*i]+msg[2*i+1]]
    return ans

def decode_with_love(msg):
    d={c:i for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    love=[d[i] for i in 'LOVE']
    love26={}
    l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for shift in range(26):
        d={c:i for i,c in enumerate(l)}
        love=[d[i] for i in 'LOVE']
        slove=''
        for i in love:
            if i<10:
                slove+='0'
            slove+=str(i)
        love26[slove]=shift
        l=l[-1]+l[:-1]
    
    shift=0
    for k,v in love26.items():
        if k in msg:
            shift=v
            break
    return decode(msg, shift)

# print(decode_with_love('0906190699021906992109069920161508209924069913162306'))

# print(decode_with_love('011607111713129925120299011013200316'))

# print(decode_with_love('0819199906220299211212119916009919220312'))

# part3

def calculate_areas(w_list, h_list):
    ans=[0,0,0]
    new_h=[0,0,0]
    for j,h in enumerate(h_list):
        new_h[j%3]+=h
    for i,w in enumerate(w_list):
        for j,h in enumerate(new_h):
            a=w*h
            index=(i+j)%3
            ans[index]+=a
    return tuple(ans)

# print(calculate_areas((1,1,1),(1,1,1)))
# l1 = [6,2,4,5,1,1,4] 
# l2 = [2,5,1,4,2,3,4]
# print(calculate_areas(l1,l2))
# l3 = [1]*10
# print(calculate_areas(l3,l3))
# l4 = [i for i in range(100000)]
# print(calculate_areas(l4,l4[::-1]))
# l4 = [i for i in range(100000)]
# print(calculate_areas(l4,l4))