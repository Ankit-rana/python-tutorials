# The Singleton pattern is used when we want to guarantee that only 
# one instance of a given class exists during runtime

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

print(id(Singleton()))
print(id(Singleton()))