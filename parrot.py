#This is class
class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
#This is Object
parrotobjectone=Parrot("parrotbluy",10)
parrotobjecttwo=Parrot("greenyparrot",15)
print(parrotobjectone.name,"age is",parrotobjectone.age)
print(parrotobjecttwo.name,"age is ", parrotobjecttwo.age,"and she is friends with", parrotobjectone.name)