# %%
import sys
num=int(input())
for i in range(num): #개수
    stu=0
    score=list(map(int, sys.stdin.readline().split(' ')))
    count=score[0] #학생수
    del score[0] #성적만 남기기  
    m=sum(score)/len(score) 
    for i in range(len(score)): #학생 성적 검사 for문
        if score[i] > m: #평균 넘는 학생수
            stu+=1
    print("%.3f%%"%(stu/count*100))     