class Student:
    def init(self):
        self.sid=None
        self.age=None
        self.marks=None
    def validate_marks(self):
            if(self.marks>0 and self.marks>=100):
                return True
            else:
                return False
    def validate_age(self):
            if(self.age>20):
                return True
            else:
                return False
    def check_qualification(self):
            if(self.marks>=65):
                return True
            else:
                return False
    def setdata(self):
        
            self.sid=input("enter student id:")
            self.age=int(input("enter age:"))
            self.marks=int(input("enter marks:"))
        
    def getdata(self):
        
            print("student id:",self.sid)
            print("student age:",self.age)
            print("student marks:",self.marks)
            if self.check_qualification():
                print("qualified")
            else:
                print("not qualified")
def main():
    n=int(input("enter number of students:"))
    for i in range(n):
        s=Student()
        s.setdata()
        s.validate_marks()
        s.validate_age()
        s.check_qualification()
        s.getdata()
main()
