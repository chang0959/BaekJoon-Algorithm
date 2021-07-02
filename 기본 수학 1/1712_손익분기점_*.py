# %%
a,b,price=list(map(int, input().split()))
count=0
#절대 while문으로 짜지 말고 수식을 만들어서 사용 
if b>=price: 
    print(-1) 
 
else:
    n=a/(price-b) 
    print(int(n)+1)  
