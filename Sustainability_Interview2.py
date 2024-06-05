import json

n = '{"name" : "siva"}'
print(type(n))

data = json.loads(n)
print(data["name"])