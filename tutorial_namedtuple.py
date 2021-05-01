# namedtuple is light weight alternative to class and structured alternative to tuple
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'marks'])
s1 = Student('ankit', 29, 70)
print(s1[0]) # ankit
print(s1.name) # ankit
print(s1._fields) # ('ankit', 29, 70)
print(s1._asdict()) # {'name': 'ankit', 'age': 29, 'marks': 70} but gives ordereddict

# namedtuple have _make api to create new instance from data coming from db/file
iterab = ('ajay', 28, 80)
s2 = Student._make(iterab)
print(s2)