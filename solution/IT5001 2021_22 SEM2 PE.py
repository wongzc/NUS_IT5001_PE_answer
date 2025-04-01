# Part1

def common_char_i(name1,name2):
    l=min(len(name1),len(name2))
    ans=0
    name1=name1.lower()
    name2=name2.lower()
    for i in range(l):
        if name1[i]==name2[i]:
            ans+=1
    return ans

def common_char_r(name1,name2):
    name1=name1.lower()
    name2=name2.lower()
    if not name1 or not name2:
        return 0
    return (name1[0]==name2[0])+common_char_r(name1[1:],name2[1:])

def common_char_u(name1,name2):
    return sum([name1.lower()[i]==name2.lower()[i] for i in range(min(len(name1),len(name2)))])


# print(common_char_i('Mark','Mary'))
# print(common_char_i('Brandy','Flank'))
# print(common_char_i('Larry','Clark'))
# print(common_char_i('Teddy','Andy'))
# print(common_char_i('McDonald','Andrey')) 
# print(common_char_r('Mark','Mary'))
# print(common_char_r('Brandy','Flank'))
# print(common_char_r('Larry','Clark'))
# print(common_char_r('Teddy','Andy'))
# print(common_char_r('McDonald','Andrey')) 
# print(common_char_u('Mark','Mary'))
# print(common_char_u('Brandy','Flank'))
# print(common_char_u('Larry','Clark'))
# print(common_char_u('Teddy','Andy'))
# print(common_char_u('McDonald','Andrey')) 

# Part2

def text_compression(text):
    d={}
    ans=[]
    for i,word in enumerate(text.split()):
        lowerWord=word.lower()
        if len(lowerWord)==1:
            ans.append(word)
        elif lowerWord not in d:
            ans.append(word)
            d[lowerWord]=str(i+1)
        else:
            ans.append(d[lowerWord])

    return ' '.join(ans)
# so... the str(i) that is used to replace repeated word is the actual index of the orginal word
# doesnt mean it is the no.x of unqiue word lol

# text7 = 'Text compression will save the world from inefficiency Inefficiency is a blight on the world and its humanity' 
# print(text_compression(text7), text_compression(text7)=='Text compression will save the world from inefficiency 8 is a blight on 5 6 and its humanity' )
# text2 = 'To be or not to be' 
# print(text_compression(text2), text_compression(text2)=='To be or not 1 2') 
# text3 = 'Do you wish me a good morning or mean that it is a good morning whether I want not or that you feel good this morning or that it is morning to be good on' 
# print(text_compression(text3),text_compression(text3)=='Do you wish me a good morning or mean that it is a 6 7 whether I want not 8 10 2 feel 6 this 7 8 10 11 12 7 to be 6 on') 

# Part3

from pprint import pprint

part0 = [
    '   ###   ',
    '  #   #  ',
    ' #     # ',
    ' #     # ',
    ' #     # ',
    '  #   #  ',
    '   ###   ']

pic = [
    [' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' '], 
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' '], 
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '], [' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' '], [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' '], [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' '], [' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' '], [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '], [' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' '], [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ']]
pic1 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'], 
    ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'], 
    ['.', '.', '#', '.', '#', '.', '#', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
    ['.', '.', '.', '.', '#', '.', '#', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
part1 = ['#.#','.#.','#.#']
def pattern_matching(picture,part):
    ans=[]
    m1=len(picture)
    n1=len(picture[0])
    m2=len(part)
    n2=len(part[0])
    for i in range(m1-m2+1):
        for j in range(n1-n2+1):
            ok=True
            for i1 in range(m2):
                for j1 in range(n2):
                    if picture[i+i1][j+j1]!=part[i1][j1]:
                        ok=False
                        break
                if not ok:
                    break
            if ok:
                ans.append((i,j,i+i1,j+j1))
    return ans

#mTightPrint(pic1)
#mTightPrint(part1)
# print(pattern_matching(pic1,part1))

# Part4
def strategic_count(mapfile):
    d={}
    with open(mapfile) as file:
        for line in file.readlines():
            lineList=line.strip().split()
            startPt=lineList[0]
            for destPt in lineList[1:]:
                if destPt not in d:
                    d[destPt]=[]
                d[destPt].append(startPt)
    memo={}
    def dfs(currPt):
        if currPt =='CountryA':
            return 1
        if currPt in memo:
            return memo[currPt]
        count=0
        for pt in d[currPt]:
            count+=dfs(pt)
        memo[currPt]=count
        return count
    
    return dfs('capitalB')
# need to memo to avoid repeat calculation, thought the testcase wont be this big to need a memo haha

# print(strategic_count('mapfile1.txt'))

    
