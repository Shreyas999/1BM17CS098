import sqlite3
conn=sqlite3.connect("db8")
conn.execute("Create table if not exists studentinfo(NAME char(40) NOT NULL,USN char(10) PRIMARY KEY,SEM int NOT NULL,\
DEPT char(3) NOT NULL)")
conn.close()

def insert():
	conn=sqlite3.connect("db8")
	name=input("Enter name:")
	usn=input("Enter usn:")
	sem=int(input("Enter sem:"))
	dept=input("Enter dept:")
	try:
		conn.execute("INSERT INTO studentinfo(NAME,USN,SEM,DEPT) VALUES(?,?,?,?)",(name,usn,sem,dept))
		conn.commit()
		print("Insert successful\n")
	except:
		print("USN already exists")
	conn.close()
	

def display():
	conn=sqlite3.connect("db8")	
	usn=input("Enter usn:")
	c=conn.execute("SELECT * from studentinfo where USN=?",(usn,))
	flag=0
	for i in c:
		print("Name:",i[0])
		print("USN:",i[1])
		print("SEM:",i[2])
		print("DEPT:",i[3])
		print("\n")
		flag=1
	if flag==0:
		print("Not found")
	conn.close()

def update():
	conn=sqlite3.connect("db8")
	usn=input("Enter usn:")
	name=input("Enter name:")
	sem=int(input("Enter sem:"))
	dept=input("Enter dept:")
	conn.execute("UPDATE studentinfo set NAME=? ,SEM=? ,DEPT=? where USN=?",(name,sem,dept,usn))
	print("Updated successfully")
	conn.commit()
	conn.close()

def displayall():
	conn=sqlite3.connect("db8")	
	c=conn.execute("SELECT * from studentinfo")
	flag=0
	for i in c:
		print("Name:",i[0])
		print("USN:",i[1])
		print("SEM:",i[2])
		print("DEPT:",i[3])
		print("")
		flag=1
	if flag==0:
		print("No records")
	conn.close()

def delete():
	conn=sqlite3.connect("db8")
	usn=input("Enter usn:")
	conn.execute("DELETE from studentinfo where usn=?",(usn,))
	conn.commit()
	conn.close()

while True:
	ch=int(input("1-Insert 2-Display 3-Update 4-Displayall 5-Delete 6-Exit\nEnter choice :"))
	if ch==1:
		insert()
	if ch==2:
		display()
	if ch==3:
		update()
	if ch==4:
		displayall()
	if ch==5:
		delete()
	if ch==6:
		break
