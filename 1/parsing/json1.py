import json
jsonData = """ {
    "ID"       : 310450,
    "login"    : "admin",
    "name"     : "James Bond",
    "password" : "root",
    "phone"    : 3330303,
    "email"    : " bond@mail.com",
    "online"   : true
} """
dictdata = json.loads(jsonData)
print(dictdata["ID"])
print(dictdata["login"])
print(dictdata["password"])
print(dictdata["email"])