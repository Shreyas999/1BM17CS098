with open("happy.txt","r") as f1:
    a=f1.read()
    a=a.split(",")
    a=set(a)
with open("prime.txt","r") as f2:
    b=f2.read()
    b=b.split(",")
    b=set(b)
c=a.intersection(b)
c=list(c)
d=[]
for i in c:
    d.append(int(i))
d.sort()
print(d)
