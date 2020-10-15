class calculator:
    
    def __init__(self,argv):
        self.argv = argv
        
    def sum(self):
        self.summery = sum(self.argv)
        return print(self.summery)

    def avg(self):
        a=len(self.argv)
        self.avg=self.summery/a
        return print(self.avg)

cal1=calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
        
cal2=calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

        


