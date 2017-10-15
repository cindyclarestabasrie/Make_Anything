from Supermarket.Fruit_class import Fruit
from Supermarket.Supermarket_class import Product

red = "\033[31m"
reset = "\033[0m"

shop_list = []
shop_price = []
quantity = []
weight = []

#The products
apple = Fruit("Apple", 1.20, "001", 0, 0)
banana = Fruit("Banana", 1.55, "002", 1, 0)
orange = Fruit("Orange", 1.3, "003", 1, 0)

can = Product("Beer Can", 3.45, "101", 6)
juice = Product("Fruit Juice", 2.20, "102", 5)

#Dictionary of products
barcodes = {apple.getBarcode(): apple,
            banana.getBarcode(): banana,
            can.getBarcode(): can,
            juice.getBarcode(): juice,
            orange.getBarcode(): orange}

def list_product():
    print(" \nBarcode", " \tPrice ", " \tQuantity ", " \tProduct ")
    for i,j in sorted(barcodes.items()):
        if j.getQuantity() == 0:
            print(i, " \t\t$" + str("%0.2f" % j.getPrice()) + " ",
                  " \t", "No Stock \t", j.getName())
        elif j.getQuantity() > 0:
            print(i, " \t\t$" + str("%0.2f" % j.getPrice()) + " ",
                  " \t", str(j.getQuantity()) + " ", " \t\t", j.getName())

print("Welcome to Happy Supermarket!")

while True:
    print("\nThis is main menu"
          "\nPick one:"
          "\n1. Buy Product"
          "\n2. List Products"
          "\n3. Add New Product"
          "\n4. Print Receipt")
    a = input("Input: ")
#Buy Products
    if a == "1":
        try:
            b = input("\nInput Barcode: ")
            if b.isdigit():
                print(barcodes[b].toString())
        except:
            print(end="")
        try:
            if barcodes[b].getQuantity() == 0:
                print("No stock. You can't buy this.")
            else:
                if type(barcodes[b]) == Fruit:
                    print("\nSince this product is fruit, the price will change according to weight."
                          "\nFruits are priced per 100 grams for each quantity."
                          "\nAlso, fruit will have separate names inside the receipt due to having different weights.")
                    try:
                        c = int(input("\nInput weight in grams: "))
                        weight.append("(" + str(c) + "g)")
                    except:
                        print(red + "Error. You must input in numbers." + reset)
                        c = int(input("\nInput weight in grams: "))
                    if c < 10:
                        print(red + "Any product that is less than 10 grams is just air." + reset)
                    else:
                        barcodes[b].setWeight(c)
                        shop_price.append(barcodes[b].FruitPrice())
                        shop_list.append(barcodes[b].getName())
                        quantity.append(1)
                elif type(barcodes[b]) == Product:
                    c = int(input("Input Quantity: "))
                    if c > barcodes[b].getQuantity():
                        print(red + "Input Quantity cannot be more than available stock!" + reset)
                    elif c < 0:
                        print(red + "Input Quantity cannot be less than zero!" + reset)
                    else:
                        barcodes[b].Purchase(c)
                        quantity.append(c)
                        shop_list.append(barcodes[b].getName())
                        shop_price.append(barcodes[b].getPrice())
                        weight.append("")
        except:
            print(red + "Error. Either you input wrong barcode or the input is not in digits." + reset)
#List of Products
    elif a == "2":
        list_product()
        b = input("Input Barcode: ")
        if b in barcodes.keys():
            print("\n1. Set New Price \n2. Set New Quantity")
            c = input("Input: ")
            if c == "1":
                d = input("Input New Price: ")
                barcodes[b].setPrice(float(d))
            elif c == "2":
                d = int(input("Input New Quantity: "))
                if d < 0:
                    print(red + "Input Quantity cannot be less than zero!" + reset)
                else:
                    barcodes[b].setQuantity(d)
            else:
                print("This program will go back to main menu.")
        else:
            print(red + "Error. Either you input wrong barcode or the input is not in digits."
                  "\nIf barcode is not input correctly, the program will return to main menu." + reset)
#Add New Product
    elif a == "3":
        try:
            b = input("Input Product Type: ")
            if b.capitalize() == "Fruit":
                c = input("Input Product Name: ")
                d = float(input("Input Product Price: "))
                e = input("Input Product Barcode: ")
                new = Fruit(c.capitalize(), d, e, 1, 0)
                barcodes[new.getBarcode()] = new
            else:
                c = input("Input Product Name: ")
                d = float(input("Input Product Price: "))
                e = input("Input Product Barcode: ")
                f = input("Input Product Quantity: ")
                new = Product(c.capitalize(), d, e, int(f))
                barcodes[new.getBarcode()] = new
        except:
            print(red + "Error. Maybe you input something wrong." + reset)

#Print Receipt
    elif a == "4":
        print("\nProduct ", " \t\tPrice ", " \t\tQuantity ")
        for i in shop_list:
            print(i + " ", " \t\t$" + str("%.2f" % shop_price[shop_list.index(i)]) + " ",
                  " \t\t", quantity[shop_list.index(i)], weight[shop_list.index(i)])
        print("\nTotal price: $", "%0.2f" % sum(shop_price))
        print("\nDone with the purchase?")
        print("1. Yes \n2. No")
        b = input("Input: ")
        if b == "1":
            break
