import json
json_string = '''{
		"name":"rizwan",
		"age":25,
		"isMarried":false,
		"isHavingGF":null}'''
employee = json.loads(json_string)
print(type(employee))	#Dict Type
print(employee)
for k,v in employee.items():
 print(k,':',v)

with open('emp.json','r') as f:
 employee = json.load(f)
 print(employee)
 for k,v in employee.items():
  print(k,':',v)