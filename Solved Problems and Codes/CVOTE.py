C,V = map(int,input().split())
Chef,Country,CC= {},{},{}
for i in range(C):
    x,y= input().split()
    Chef[x],Country[y]=0,0
    CC[x] = y
for __ in range(V):
    x =input()
    Chef[x]+=1 
    Country[CC[x]]+=1
max_value = max(Chef.values())
li1 = [k for k,v in Chef.items() if v == max_value]
max_value = max(Country.values())

li2 = [k for k,v in Country.items() if v == max_value]

print(min(li2))
print(min(li1))
