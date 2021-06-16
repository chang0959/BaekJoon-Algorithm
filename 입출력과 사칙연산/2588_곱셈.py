# %%
num=int(input())
num1=int(input())
third=num1%10
second=int(num1%100/10)
first=int(num1/100) 
print(num*third) #num1%10:마지막 자리
print(num*second) #int(num1%100/10): 두번째 자리 
print(num*first) #int(num1/100): 첫번째자리
print(num*third+num*second*10+num*first*100) 