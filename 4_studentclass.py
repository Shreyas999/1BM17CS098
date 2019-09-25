class student:
    def __init__(self):
        self.name=None
        self.age=None
        self.marks=None
    def inputdata(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter Age:"))
        self.marks=int(input("Enter marks:"))
    def outputdata(self):
        print(self.name+"\n"+str(self.age)+"\n"+str(self.marks))                       
    def validate_marks(self):
        if 0<=self.marks<=100:
            return True
        return False
    def validate_age(self):
        if self.age>20:
            return True
    def check_qualification(self):
        if self.age>20 and 65<=self.marks<100:
            return True
        return False

s=student()
s.inputdata()
va=s.validate_age()
vm=s.validate_marks()
if vm==True and va==True:
    q=s.check_qualification()
    if q==True:
        print("Congratulations!")
    else:
        print("Rejected!")
else:
    print("Application Rejected")
