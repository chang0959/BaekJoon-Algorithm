# %%
num=int(input())
for i in range(num):
    word=input()
    count=0
    double=[]
    for i in word: #중복 알파벳
        if word.count(i)>=2:
            double.append(i) 
    print(set(double))
    if len(word) > len(set(word)): #그룹단어 판별
        for j in set(double):    
            if len(set(word[word.find(j) : word.rfind(j)]))>=2:
                continue #그룹 단어 x  
            else:            
                count+=1 #그룹 단어     
    elif len(word) == len(set(word)): #그룹단어이면
        count+=1  
    else: #그룹단어 아니면
        continue  

print(count)
# %%
