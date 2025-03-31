# part1
def sum_digit_square_I(n):
    ans=0
    while n:
        ans+=(n%10)**2
        n=n//10
    return ans
    
def sum_digit_square_R(n):
    if not n:
        return 0
    return (n%10)**2+ sum_digit_square_R(n//10)
def is_happy_number(n):
    seen=set()
    while n not in seen:
        seen.add(n)
        n=sum_digit_square_I(n)
        if n==1:
            return True
    return False
def all_happy_number(n,m):
    ans=[]
    for j in range(n,m+1):
        if is_happy_number(j):
            ans.append(j)
    return ans

# part2
def is_unique(seq):
    counter=0
    for c1 in seq:
        for c2 in seq[counter+1:]:
            if c1==c2:
                return False
        counter+=1
    return True

