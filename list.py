l1=[2,3,4,5,6,7,8]
l2=[4,9,16,25,36,49,64]
a=(l1[0:1]+l2[0:1])
b=(l1[1:2]+l2[1:2])
c=(l1[2:3]+l2[2:3])
d=(l1[3:4]+l2[3:4])
e=(l1[4:5]+l2[4:5])
f=(l1[5:6]+l2[5:6])
g=(l1[6:7]+l2[6:7])
z=[a,b,c,d,e,f,g]
print(z)

speed={"jan":47,"feb":52,"march":47,"Abril":44,"may":52,"jun":53,"july":54}
nlist=list(speed.values())
res = []
for i in nlist:
    if i not in res:
        res.append(i)

print(res)


