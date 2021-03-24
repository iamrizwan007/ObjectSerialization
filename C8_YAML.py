#YAML: Yaml Aint't Markup Language, Yet Another Markup Language
#dump - to serialize to py dict object to yaml string or yaml string
#load - to deserialize from yaml string or yaml file to py dict object
#Note: load() is deprecated and we have to use safe_load() function
from pyaml import yaml
emp_dict ={'name': 'Rizwan','Age': 25,'Salary':37000,'isMarried' : False}
#serialization to yaml string
yaml_string = yaml.dump(emp_dict)
print(yaml_string)

#serializatioon to yaml file
with open("emp.yaml","w") as f:
 yaml.dump(emp_dict,f)

#Desrialization from yaml string to py dict obj
new_dict = yaml.safe_load(yaml_string)
print(new_dict)

#Deserialization from yaml file to py dict obj
with open("emp.yaml","r") as f:
 new_dict2 = yaml.safe_load(f)
print(new_dict2)
