class Product:
    def __init__(self, name, price, barcode, quantity):
        self.__name = name
        self.__price = price
        self.__barcode = barcode
        self.__quantity = quantity

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getBarcode(self):
        return self.__barcode

    def getQuantity(self):
        return self.__quantity

    def setPrice(self, price):
        self.__price = price

    def setBarcode(self, barcode):
        self.__barcode = barcode

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def toString(self):
        return "Name\t: " + self.__name + \
               "\nPrice\t: $" + str("%.2f" % self.__price) + \
               "\nQuantity\t: " + str(self.__quantity)

    def Purchase(self, quantity):
        self.__quantity = self.__quantity - quantity
