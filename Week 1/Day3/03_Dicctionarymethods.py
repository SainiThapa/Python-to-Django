Dic={
    "Name":"Saini",
    "Roll":44,
    "marks":[79,89],
    "Dic2":{'Suman':'Gole'}
}
print(Dic)
Dic["Dic2"]["Suman"]="Tamang"
print(Dic)
print(type(Dic.keys())) #Prints the type of the dictionary
print(list(Dic.keys())) #Prints the list of the dictionary
print(Dic.values()) #Prints the values of the dictionary content
print(Dic.items()) #Prints the (key,value) of the dictionary content
Dict1={
    "Address":"Bhaktapur"
}
Dic.update(Dict1)
print(Dic.get("Name1"))
print(Dic["Name1"]) #Throws an error