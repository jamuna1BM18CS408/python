class CallDetail:
    def __init__(self):
        self.callto=None
        self.callby=None
        self.duration=None
        self.type=None
class Util:
    def __init__(self):
        self.list_of_call_objects=[]
    def parse_customer(self,list_of_call_string):
        for i in range(len(list_of_call_string)):
            lis=list_of_call_string[i].split(",")
            self.list_of_call_objects.append(lis)
    def output(self):
        for i in range(len(self.list_of_call_objects)):
            print("callto:",self.list_of_call_objects[i][0],"\n")
            print("callby:",self.list_of_call_objects[i][1],"\n")
            print("duration:",self.list_of_call_objects[i][2],"\n")
            print("type:",self.list_of_call_objects[i][3],"\n")
call='1234526526,5275527382,15,LOCAL'
call2='987235166,8972654256,25,STD'
call3='983765265,8764512356,30,LOCAL'
list_of_call_string=[call,call2,call3]
y=Util()
y.parse_customer(list_of_call_string)
y.output()
            
            
            
