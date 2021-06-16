# %%
num=int(input())
for i in range(num):
    score=list(map(int, input().split(' ')))
    print(sum(score))
