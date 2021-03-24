import jsonpickle
#pip install jsonpickle
#encode - employee object to json directly (serialization)
#decode - json to employee object directly (Deserialization)

class Employee:
 def __init__(self,eno,ename,esal,isMarried):
  self.eno = eno
  self.ename = ename
  self.esal = esal
  self.isMarried = isMarried
 def display(self): 
  print("ENO: {}, ENAME: {}, ESAL: {}, isMarried: {}".format(self.eno,self.ename,self.esal,self.isMarried))

e = Employee(101,"rizwan",37000,False)

#Serialization to JSON string
json_string = jsonpickle.encode(e)
print(json_string)

#Serialization to JSON File
with open("customjsonpickle.json","w") as f:
 f.write(json_string)

#Deserialization from JSON string to Employee object
e2 = jsonpickle.decode(json_string)
print(type(e2))
e2.display()

#Deserialization from JSON File
with open("customjsonpickle.json","r") as f:
 json_string = f.readline()
e3 = jsonpickle.decode(json_string)
e3.display()