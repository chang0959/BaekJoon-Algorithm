# %%
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # 절대 ''으로만 하지 말기 
print(len(word))
