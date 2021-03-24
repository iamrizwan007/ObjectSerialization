class Employee:
 def __init__(self,eno,ename,esal):
  self.eno = eno
  self.ename = ename
  self.esal = esal

 def display(self):
  print("employee number: {} employee name: {} employee salary: {}".format(self.eno,self.ename,self.esal))
