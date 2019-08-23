import json

a = {"Name": "Anton",
      "Students": ["Anton", "Andrey", "Yulya"]
     }


b2 = json.dumps(a, indent=4)

str_json = '{"Name": "Anton"}'

a = json.loads(str_json)

print(a)
print(type(a))
print(a["Name"])


