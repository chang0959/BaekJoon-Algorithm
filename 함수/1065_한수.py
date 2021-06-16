# %%
#한수 함수 정의
def d(num):
    score=list(str(num))
    diff=[]
    for i in range(len(score)-1):
        diff.append(abs(score[i]-score[i+1]))
    print(diff)

    
# %%
