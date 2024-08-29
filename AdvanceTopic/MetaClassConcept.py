#it is creating class
class harish:
    y=20

#creating object
a=harish()

print(type(a))  #it returns the class value
print(type(harish))

#creating class using type
a=type('Python',(harish,),{'x':10})  #dictonary is used for the attribute #in tuple it is like inheriting the class

obj=a()

print(obj.x)
print(obj.y)

#create metaclass
class Meta(type):
    pass

class edureka(metaclass=Meta):
    pass

print(type(edureka)) #it points to custome meta class created instance of clas

#sample work

class MetaTwo(type):
    def __new__(self,name,bases,attr):
        attr['name']='harish'
        print(attr)
        return type(name,bases,attr)

    # def __init_(self,name,bases,attr):
    #     print("this")
    #     return None #only return null methon init method should return null

class Python(metaclass=MetaTwo):
    x=10
    y=20
    name="deepak"

a=Python()
print(a.name)
print(a.x)
