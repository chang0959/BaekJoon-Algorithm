# %%
num=int(input())
score_list=list(map(int,input().split())) 
max=0
for i in range(num): #최대값 찾는 for문
    if score_list[i]>max:
        max=score_list[i]
    else:
        continue
for i in range(num):
    score_list[i]=score_list[i]/max*100
print(sum(score_list)/len(score_list)) 