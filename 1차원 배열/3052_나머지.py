# %%
score=[] #나머지
for i in range(10):
    num=int(input())
    score.append(num%42)

a=set(score) #중복 제거 
print(len(a)) 

