# %%
num=int(input())

for i in range(num):
    string = input()
    count=0
    point=[]
    for j in list(string):
        if j == 'O': 
            count+=1
            point.append(count) #count값 누적
        elif j == 'X':
            count=0
    print(sum(point))