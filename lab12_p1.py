class Myclass:
    def __init__(self,a,b):
        self.name = a # class data member name, no need to define
        self.age = b # class data member age
    def display(self):
        print 'your name is ',self.name
        print 'you are %s years old'%self.age
