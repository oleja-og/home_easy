import json
s = {"admin":"admin","oleg":"1111"}
with open("users.json", "w") as write_file:
    json.dump(s, write_file)