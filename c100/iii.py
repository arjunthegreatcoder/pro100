class Atm(object):
    def __init__(self,pin,number):
        self.pin = pin
        self.number = number
    def balEnq(self):
        print("your Balance is : 1000000") 
    def cashWithDraw(self):
        print("Cash WithDraw")
    
hdfc = Atm(1002,7346)
print(hdfc.balEnq())
print(hdfc.cashWithDraw())
    







