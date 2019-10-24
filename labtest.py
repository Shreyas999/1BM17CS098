class BakeHouse:
	def __init__(self):
		self.occupied_table_list=[]
	def get_occupied_table_list(self):
		return self.occupied_table_list
	def allocate_table(self):
		flag=0
		for i in range(1,11):
			if i in self.occupied_table_list:
				pass
			else:
				self.occupied_table_list.append(i)
				self.occupied_table_list.sort()
				print("Allocated table",i)
				flag=1
				break
		if flag==0:
			print("Table not allocated")
	def deallocate_table(self,table_number):
		if table_number in self.occupied_table_list:
			self.occupied_table_list.remove(table_number)
			print("Deallocated table",table_number)

bh=BakeHouse()		
print("1:Get occupied table list\n2:Allocate table\n3:Deallocate table\n0:Exit\n")
choice=-1
while(choice!=0):
	choice=int(input("Enter your choice:"))
	if choice==1:
		print(bh.get_occupied_table_list())
	elif choice==2:
		bh.allocate_table()
	elif choice==3:
		a=int(input("Enter table number:"))
		bh.deallocate_table(a)
