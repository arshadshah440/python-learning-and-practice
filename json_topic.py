x = {
  "name": "Alex Mercer",
  "age": 28,
  "isEmployee": True,
  "skills": ["Python", "JavaScript", "SQL"],
  "address": {
    "city": "Austin",
    "state": "Texas"
  },
  "certifications": ""
}

import json

y = json.dumps(x,indent=4,sort_keys=True)


print(y)

data = json.loads(y)

print(data["name"]);