# %%
num,num1,num2=map(int,input("").split(" "))
if (num>=2) & (num<=10000) & (num1>=2) & (num1<=10000) & (num2>=2) & (num2<=10000):
    print((num+num1)%num2)
    print(((num-num2)+(num1%num2))%num2)
    print((num*num1)%num2)
    print(((num%num2) * (num1%num2))%num2)
else:  
    print("잘못 입력하셨습니다.")