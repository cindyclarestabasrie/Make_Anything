from Supermarket.Supermarket_class import Product

class Fruit(Product):
    def __init__(self, name, price, barcode, quantity, weight):
        super().__init__(name, price, barcode, quantity)
        self.__weight = weight

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def FruitPrice(self):
        return self.getPrice() * (self.__weight/100)
