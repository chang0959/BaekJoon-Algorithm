# %% 
score=[]
while True:
  num,num1=map(int,input().split())
  if (num == 0) & (num1 == 0):
    break     
  else:
    score.append(num+num1) 
 
i=0
while i < len(score):
  print(score[i])
  i+=1