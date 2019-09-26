class CallDetail:
    def __init__(self,c,r,d,t):
        self.c=c
        self.r=r
        self.d=d
        self.t=t
    def returnvalues(self):
        return (self.c,self.r,self.d,self.t)

class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            a=i.split(",")
            detail=CallDetail(a[0],a[1],a[2],a[3])
            self.list_of_call_objects.append(detail)
    def printdetails(self):
        y={"STD":0,"Local":0,"ISD":0}
        for i in self.list_of_call_objects:
            x=i.returnvalues()
            y[x[3]]+=1
            print("\nCaller:"+x[0]+"\nReceiver:"+x[1]+"\nDuration:"+x[2]+"\nType:"+x[3])
        print("\nCount:")
        print("Local:"+str(y["Local"])+"\nSTD:"+str(y["STD"])+"\nISD:"+str(y["ISD"]))  
            
call1 = "9481476756,7406636601,5.0,STD"
call2 = "9742011501,9481476756,43.0,Local"
call3 = "7975149962,7406636601,5,ISD"
l = [call1,call2,call3]
util=Util()
util.parse_customer(l)
util.printdetails()
