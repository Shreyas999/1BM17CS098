a=list(map(int,input("Enter the list:").split()))
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print("ORIGINAL LIST :\n",a)
print("OUTPUT :")
for j in b:
    print(j,end=" ")

'''OUTPUT:
Enter the list:1 2 3 4 5 6 7 8 9
ORIGINAL LIST :
 [1, 2, 3, 4, 5, 6, 7, 8, 9]
OUTPUT :
2 4 6 8
'''
