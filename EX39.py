class CashRegister :
## Comment 1
#This is the constructor for a cash register class with
#cleared item count and total.
#The "self" parameter is reserved for class methods.
    def __init__(self) :
        self._itemCount = 0
        self._totalPrice = 0.0
# Comment 2
#The function "addItem" give the instruction to adds an item and
#the price of this item to the cash register
#The "self" parameter is reserved the methods
    def addItem(self, price) :
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
# Comment 3
#The function "getTotal" gets the price of all items in sale
#return the total price
        
    def getTotal(self) :
        return self._totalPrice
# Comment 4
#In this line the function became a parameter and take the
#numbers of items
#return the item count
    def getCount(self) :
        return self._itemCount
# Comment 5
#In this lines the function "clear" give the instraction to
#clear the item and total price.
    def clear(self) :
        self._itemCount = 0
        self._totalPrice = 0.0

register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register2 = CashRegister()
register2.addItem(1.90)

print("register1_itemCount is: \t", register1._itemCount)
print("register1_totalPrice is: \t", register1._totalPrice)
print("register2_itemCount is: \t", register2._itemCount)
print("register2_totalPrice is: \t", register2._totalPrice)
