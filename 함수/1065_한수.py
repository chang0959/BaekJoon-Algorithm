# %%
# 한수 함수 정의
def d(num):
    score=list(str(num))  
    diff=[]
    if len(score)==1: #1의 자리수는 한수
        diff.append('O')        
    for i in range(len(score)-1): 
        diff.append(int(score[i])-int(score[i+1]))
    if len(set(diff))==1: #한수라면
        return "O"       
    else: #한수가 아니라면 
        return "X"
num=int(input()) 
output=[] 
for i in range(1, num+1):
    output.append(d(i))                
print(output.count("O"))  