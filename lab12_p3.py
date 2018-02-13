class rectangle:
    def __init__(self,a,b):
        self.length=a
        self.width=b
    def calculate(self):
        self.area=self.length*self.width
        self.per=2*(self.length+self.width)
        print 'Area of rectangle : %s'%self.area
        print 'perimeter of rectangle : %s'%self.per
    def display(self):
        print 'length of the rectangle : ',self.length
        print 'width of the rectangle is : ',self.width
