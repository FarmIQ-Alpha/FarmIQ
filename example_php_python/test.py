import json

variable1 = "Hello from Python"
variable2 = 42

data = {
    "variable1": variable1,
    "variable2": variable2
}

print(json.dumps(data))
