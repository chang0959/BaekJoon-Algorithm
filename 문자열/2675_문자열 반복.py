# %%
score=int(input())
for i in range(score):
    a=list(input().split())
    num=int(a[0]) #숫자  
    alph = list(a[1]) #알파벳
    for i in range(len(alph)):     
        print(alph[i]*num,end='')
    print()
