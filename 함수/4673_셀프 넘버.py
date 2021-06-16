# %%
def d(n): # Kaprekar함수 정의
    score=0
    a=list(str(n)) #각 자리수를 리스트에 저장
    for i in range(len(a)):
        score+=int(a[i]) 
    score+=n
    return score  

s=set() #중복 제거
for i in range(1,10001):
    s.add(d(i))

num=set(range(1,10001)) - s
for k in sorted(num):
    print(k)