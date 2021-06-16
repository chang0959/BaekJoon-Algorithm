# %%
num=int(input())          
copy=num 
i=0 
while 1:      
    score_1=int(num/10) #첫번째 자리수 
    score_2=num%10 #두번째 자리수
    sum=score_1+score_2 #각 자리의 숫자 더하기
    sum_2=sum%10 
    new=str(score_2)+str(sum_2)
    i+=1 
    if int(new) == copy:
        break
    else: 
        #print('score_1: ',score_1, 'score_2: ',score_2, 'sum: ',sum,'new: ',new)
        num=int(new)  
        continue
print(i)