# %%
num,num1=map(int,input("").split(" "))
if (num>=1) & (num1<=10000):
    print(num+num1)
    print(num-num1)
    print(num*num1)
    print(int(num/num1))
    print(num%num1)
else:  
    print("잘못 입력하셨습니다.")