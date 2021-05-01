# this is used whenever you have composite attribute

class Student:
    def __init__(self, a):
        self.a = a
        self.b = self.a + 30 # composite attribute

s = Student(10)
print(s.a)
print(s.b)
s.a = 20
print(s.a)
print(s.b) # expecting 50 but gets old 40 (initializer are initiated once per instance)

# To solve above problem, we use property

class Student:
    def __init__(self, a):
        self.a = a
    
    @property
    def b(self):
        return self.a + 30

s = Student(10)
print(s.a)
print(s.b)
s.a = 20
print(s.a)
print(s.b) # 50


# Now what if we try to set s.b
s.b = 60 # AttributeError: can't set attribute

# To solve this
class Student:
    def __init__(self, a):
        self.a = a
    
    @property
    def b(self):
        return self.a + 30
    
    @b.setter
    def b(self, b):
        self.b = b


s = Student(10)
print(s.a)
print(s.b)
s.b = 60 
print(s.b)

# also this not changing s.a back, we can property for same 
