mydictionary={
    "name": "Jack",
    "age": 26,
}
mydictionary['name']='jarif'
print(mydictionary)
mydictionary['address']='dhaka'
print(mydictionary)
mydictionary['age']=12
print(mydictionary)
#remove particular element
mydictionary.pop('address')
print(mydictionary)
#accsess a particular element
print("Name is:",mydictionary.get('name'))
