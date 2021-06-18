# %%
num, num1= input().split()
num_ls=list(num)
num1_ls=list(num1)
  
# num_f=num_ls 절대 불가 값이 같이 변경됨
num_f=[num_ls[0],num_ls[1],num_ls[2]] 
num_f[0]=num_ls[2]
num_f[2]=num_ls[0] 
num_f=''.join(num_f) 
 
num1_f=[num1_ls[0],num1_ls[1],num1_ls[2]]
num1_f[0]=num1_ls[2]
num1_f[2]=num1_ls[0]
num1_f=''.join(num1_f) 

if int(num_f) > int(num1_f):
    print(num_f)
else:
    print(num1_f)

# %% 역순을 이용한 방법
num, num1= input().split()
num=num[::-1]
num1=num1[::-1]
#삼항 연산자
print(num) if num>num1 else print(num1)