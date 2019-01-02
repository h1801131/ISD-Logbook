class CashRegister :
    def __init__(self) :
        self._itemCount = 0
        self._totalPrice = 0.0

    def addItem(self, price) :
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    def getTotal(self) :
        return self._totalPrice
    
    def getPounds(self):
        return int(self._totalPrice)

    def giveChange(self, payment):
        change = payment - self._totalPrice
        self.clear()
        return change

    def getCount(self) :
        return self._itemCount

    def clear(self) :
        self._itemCount = 0
        self._totalPrice = 0.0
        
register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)

print(register1.getCount())
print("Expected: 3")
print("%.2f" % register1.getTotal())
print("Expected: 5,40")
print("In pound only:", register1.getPounds())
print("Expected: 5")
print("Change given is: %.2f" %register1.giveChange(10.00))
print("Expected: 4.60 assuming payment given is 10.00") 

 
