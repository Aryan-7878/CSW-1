class Demo:
    def __new__(cls):
        print("__new__ method called (object creation)")
        obj = object.__new__(cls)   
        return obj

    def __init__(self):
        print("__init__ method called (object initialization)")


print("Creating Demo object:")
d = Demo()


class MyInt(int):
    def __new__(cls, value):
        print("__new__ of MyInt called")
        
        return super().__new__(cls, value + 10)

    def __init__(self,value):
        print("__init__ of MyInt called (value already fixed)")


print("\nCreating MyInt object:")
num = MyInt(5)
print("Final value of num:", num)