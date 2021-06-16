# %%
num=[] 
for i in range(9):   
    num.append(int(input()))   
  
print(max(num), num.index(max(num))+1) #최대값과 해당 원소의 인덱스 출력 
