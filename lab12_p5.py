class bank:
    def __init__(self,a,b,c,d):
        self.name=a
        self.number=b
        self.type=c
        self.bal=d
    def deposite(self,x):
        self.bal=self.bal+x
        print 'you current balance is : %s'%self.bal
    def withdrawl(self,y):
        self.bal=self.bal-y
        print 'after withdrawl amount \n your current balance is : %s'%self.bal
    def display(self):
        print 'name of the employee is : %s'%self.name
        print 'balance in %s account'%self.name,
        print 'is %s'%self.bal
