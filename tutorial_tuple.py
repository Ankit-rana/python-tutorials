# tuple is a datatype which is unmutable.
# tuples are generally collection of heterogenous datatype
# Student = (name, age, marks)
# tuple also take less storage than list

student = ('ankit', 20, 70)
print(student[2]) # marks ie. 70
student[2] = 90 # TypeError: 'tuple' object does not support item assignment