# python dictionary
studentinfo = {
    "saifullah": {
    'name': 'saifullah',
    'age': 21,
    'course': 'CSE',
    'roll': 212010097,
    },


     "chayan": {
    'name': 'chayan',
    'age': 21,
    'course': 'CSE',
    'roll': 212010096,}

}
print(studentinfo["chayan"])

print(studentinfo['saifullah'])

#access items
x = studentinfo.get("saifullah")
print(x)

#get keys

print(studentinfo.keys())

#get values

print(studentinfo.values())

#change values

studentinfo["saifullah"] = {
    'name':'saifullah',
    'age': 21,
    'course': 'CSE',
    'roll': 212010097,
    },

print(studentinfo["saifullah"])

#copy values

studentinfo2 = studentinfo.copy()
print(studentinfo2)
