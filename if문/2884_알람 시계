# %%
hour, minute = map(int,input().split())
#45분 기준 
if minute < 45:  
    if hour == 0:
        hour= 23
        minute=(60+minute)-45
         
    elif  hour>0:
        hour=hour-1
        minute=(60+minute)-45
    print(hour, minute)

elif minute==45:
    print(hour, 0) 

else:
    print(hour, minute-45)  