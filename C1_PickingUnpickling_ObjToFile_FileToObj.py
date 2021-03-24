#process of converting object from python supported form to file supported form - serialization
#reverse opertation is deserialization
import pickle
class Emp:
 def __init__(self,eno,ename,esal):
  self.eno = eno
  self.ename = ename
  self.esal = esal

 def display(self):
  print("employee number: {} employee name: {} employee salary: {}".format(self.eno,self.ename,self.esal))

e = Emp(101,'Rizwan',40000)
e.display()
#Serialization/Pickling
with open('dump.ser','wb') as f:
 pickle.dump(e,f)
 print("Object converted to file")

#Deserialization/Unpickling
with open('dump.ser','rb') as f:
 emp_obj = pickle.load(f)
 print("converted to obj emp_obj from file")

emp_obj.display()