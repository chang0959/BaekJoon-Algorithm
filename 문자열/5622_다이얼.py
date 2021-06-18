# %% 
alpha=list(input())
dic={'1':[],'2':['A','B','C'], '3':['D','E','F'], '4': ['G','H','I'], '5':['J','K','L'],
'6':['M','N','O'],'7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'],
'0':[]}

sum=0
for k,v in dic.items():
    for i in range(len(alpha)): 
        if alpha[i] in v: #해당 문자에 해당하는 key값 찾기
            sum+=int(k)+1
print(sum)

# %% 간결한 코드
dial= ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
ipt=input()  
ret=0
for i in range(len(ipt)):
    for j in dial:
        if ipt[i] in j:
            ret += dial.index(j)+3

print(ret)