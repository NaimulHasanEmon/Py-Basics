dict = {
    "name": "Lameya",
    "age": 25,
    "course": ['python', 'oop 2'],
    "score": 94.50,
    "subject": ('cse', 'math')
}

stringList = []
intList = []
floatList = []
listList = []
tupleList = []

for key in dict:
    if type(dict[key]) == str:
        stringList.append(dict[key])
    elif type(dict[key]) == int:
        intList.append(dict[key])
    elif type(dict[key]) == float:
        floatList.append(dict[key])
    elif type(dict[key]) == list:
        listList.append(dict[key])
    elif type(dict[key]) == tuple:
        tupleList.append(dict[key])

print(stringList)
print(intList)
print(floatList)
print(listList)
print(tupleList)
