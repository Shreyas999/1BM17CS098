a=input("Enter the string:")
b=a.split(" ")
c=[]
for i in b:
    c.append(list(i)[::-1])
for j in c:
    print("".join(j),end=" ")
print("")
b.reverse()
for k in b:
    print(k,end=" ")
