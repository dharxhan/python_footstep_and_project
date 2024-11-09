"""class Emp:
    def getDetails(self):
        self.eid=int(input("Enter the emp id:"))
        self.ename=input("Enter the emp name:")
        self.salary=float(input("Enter the emp salary:"))
    def putDetails(self):
        print("Emp id:",self.eid)
        print("Name is:",self.ename)
        print("Salary is:",self.salary)
empRecord=Emp()
empRecord.getDetails()
empRecord.putDetails()"""

#encapsulated eid
"""
class Emp:
    def getDetails(self):
        self.__eid=int(input("Enter the emp id:"))
        self.ename=input("Enter the emp name:")
        self.salary=float(input("Enter the emp salary:"))
    def putDetails(self):
        print("Emp id:",self.__eid)
        print("Name is:",self.ename)
        print("Salary is:",self.salary)
empRecord=Emp()
empRecord.getDetails()
empRecord.__eid=150
empRecord.putDetails()"""

#adding extra objects
"""
class Emp:
    def getDetails(self):
        self.__eid=int(input("Enter the emp id:"))
        self.ename=input("Enter the emp name:")
        self.salary=float(input("Enter the emp salary:"))
    def putDetails(self):
        print("Emp id:",self.__eid)
        print("Name is:",self.ename)
        print("Salary is:",self.salary)
objContainer=[]
numofObjects=int(input("Enter the no. of objects:"))
for obj in range(numofObjects):
    empRecord=Emp()
    empRecord.getDetails()
    objContainer.append(empRecord)
for obj in range(numofObjects):
    objContainer[obj].putDetails()
    print("=================")
"""

class Emp:
    def getDetails(self):
        self.eid=int(input("Enter the emp id:"))
        self.ename=input("Enter the emp name:")
        self.salary=float(input("Enter the emp salary:"))
    def putDetails(self):
        print("Emp id:",self.eid)
        print("Name is:",self.ename)
        print("Salary is:",self.salary)
objContainer=[]
numofObjects=int(input("Enter the no. of objects:"))
for obj in range(numofObjects):
    empRecord=Emp()
    empRecord.getDetails()
    objContainer.append(empRecord)
eid=int(input("Enter the eid:"))
for obj in range(numofObjects):
    if objContainer[obj].eid==eid:
        found=1
        objContainer[obj].putDetails()
        print("=================")
        break
if found==0:
    print("No record exists")
