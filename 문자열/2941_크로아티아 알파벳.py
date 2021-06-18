# %%
alpha=input()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

sum=0
for i in croatia:
    if alpha.count(i) >= 1:
        sum+=alpha.count(i) 
        alpha=alpha.replace(i,'')
print(alpha)
print(sum+len(alpha))
# %%
