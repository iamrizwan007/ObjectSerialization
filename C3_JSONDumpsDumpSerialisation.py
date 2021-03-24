import json
employee = {'name':'rizwan',
		'age':25,
		'isMarried':False,
		'isHavingGF':None
		}
print("Serialising python Dict obj to JSON string")
json_string = json.dumps(employee,indent=4,sort_keys=True)
print("serialised to JSON string")
print(json_string)

with open('emp.json','w') as f:
 json.dump(employee,f,indent=4,sort_keys = True)
 print("written json string to a file using dump function")
