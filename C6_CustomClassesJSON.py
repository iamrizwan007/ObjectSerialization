import json
class Employee:
 def __init__(self,eno,ename,esal):
  self.eno = eno
  self.ename = ename
  self.esal = esal
 def display(self):
  print("ENO: {}, ENAME: {}, ESAL: {}".format(self.eno,self.ename,self.esal))

e = Employee(101,"Rizwan",35000)
#e_dict = {"eno":e.eno,"ename":e.ename,"esal":e.esal}
e_dict = e.__dict__
print("Python DICT")
print(e_dict)
print("serialising to JSON string")
json_string = json.dumps(e_dict,indent=4,sort_keys=True)
print(json_string)
print("to a file")
with open("customjson.json","w") as f:
 json.dump(e_dict,f,indent=4)
print("written to file")

#I Want JSON to Employee Object Not DICT 
#Deserialization
print("\n\n")
with open("customjson.json",'r') as f:
 edict = json.load(f)
e = Employee(edict['eno'],edict['esal'],edict['esal'])
e.display()