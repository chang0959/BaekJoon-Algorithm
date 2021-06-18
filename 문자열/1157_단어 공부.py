# %%
a= list(input().upper())
s=set(a)
d={} #딕셔너리 
for i in list(s):
    d[i]=a.count(i) #알파벳 갯수 count

key=[]
for k,v in d.items():
    if v == max(d.values()):
        key.append(k) 

if len(key) >=2: #중복이면
    print('?')
else: print(key[0])