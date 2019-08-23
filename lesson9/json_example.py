import json

a = {"Name": "Anton",
      "Students": ["Anton", "Andrey", "Yulya"]
     }

b1 = json.dumps(a)
b2 = json.dumps(a, indent=4)


print(b1)
print(type(b1))

print(b2)
