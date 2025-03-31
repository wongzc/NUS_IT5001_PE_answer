# Part1
def check(x,y,d):
    if d=='W':
        x-=1
    if d=='E':
        x+=1
    if d=='N':
        y+=1
    if d=='S':
        y-=1
    return x,y

def final_pos_i(x,y,seq):
    for d in seq:
        if d=='W':
            x-=1
        if d=='E':
            x+=1
        if d=='N':
            y+=1
        if d=='S':
            y-=1
    return (x,y)

def final_pos_r(x,y,seq):
    if not seq:
        return (x,y)
    d=seq[0]
    if d=='W':
        x-=1
    if d=='E':
        x+=1
    if d=='N':
        y+=1
    if d=='S':
        y-=1
    return final_pos_r(x,y,seq[1:])

def final_pos_o(x,y,seq):
    return (x+(seq.count('E')-seq.count('W')),y+(seq.count('N')-seq.count('S')))

# print(final_pos_i(2,4,'WNWNE')) 
# print(final_pos_i(9,1,'NSWSSWNSSE')) 
# print(final_pos_i(0,0,'WWENSWSNSWSSWNSSE'))

# Part2
def mutate(amino_acid,no_gen):
    d={'A':'CG','C':'AT','G':'CA',"T":'GT'}
    for _ in range(no_gen):
        new=''
        for a in amino_acid:
            new+=d[a]
        amino_acid=new
    return amino_acid

def amino_acid(start_amino_acid,no_gen,pos):
    l=[]
    for _ in range(no_gen):
        l.append(pos)
        pos=pos//2
    l=l[::-1]
    curr=start_amino_acid
    for i in range(no_gen):
        new=mutate(curr,1)
        curr=new[l[i]%2]
    return curr



# You should not submit the following test cases 
# print(mutate('A',3)) 
# print(mutate('T',2)) 
# print(mutate('G',5)) 
# print(amino_acid('A',3,3)) # DNA: 'CGGTATCG' 
# print(mutate('G',5)) 
# print(amino_acid('G',5,12)) 
# print(amino_acid('T',31,1231311))

# Part3
def upgrade_burger(b1,b2):
    i=0
    j=0
    l2=len(b2)
    l1=len(b1)
    if l1<l2:
        return False
    while j<l2 and i<l1:
        if b1[i]==b2[j]:
            j+=1
        i+=1
    if j==l2:
        return True
    return False

# print(upgrade_burger("BLLB","BLB")) 
# print(upgrade_burger("BLB","BCLB")) 
# print(upgrade_burger("BCLPCPLCB","BCLLCB")) 
# print(upgrade_burger("BCLPLCLPPCLCPLCB","BCLPCPLCB")) 
# print(upgrade_burger("BCLB","BLCB")) 
# print(upgrade_burger("BCLCB","BLCB")) 
# print(upgrade_burger("B"+"LC"*10000+"LB","B"+"LC"*10000+"CB")) 
# print(upgrade_burger("B"+"LC"*10000+"VB","B"+"LC"*10000+"LCB")) 
# print(upgrade_burger("B"+"LC"*10000+"CLB","B"+"LC"*10000+"CB"))
