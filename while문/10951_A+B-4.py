# %%
import sys
while True:
    try: #try문 필요
        num,num1=map(int,sys.stdin.readline().split())
        print(num+num1) 
    except:
        break