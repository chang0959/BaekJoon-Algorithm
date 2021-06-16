# %%
from string import ascii_lowercase #알파벳 소문자 불러오기
alphbat_list= list(ascii_lowercase)

alphbat=input() 
for i in alphbat_list:
    print(alphbat.find(i))
