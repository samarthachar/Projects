inventory = dict()
def add():
    print("--")
    quel = input("Enter item name: ").lower
    quantite = int(input("Enter quantity in numbers: "))
    argent = int(input("Enter price in number: "))
    inventory[quel] = [quantite,argent]
def update():
    print("--")
    quel = input("Enter item name: ").lower
    if quel in inventory:
        quantite = int(input("Enter quantity in numbers: "))
        argent = int(input("Enter price in number: "))
        inventory[quel] = [quantite,argent]
    else:
        print(f"No item called {quel}")

def delete():
    print("--")
    quel = input("Enter item name: ").lower
    if quel in inventory:
        inventory.pop(quel)
    else:
        print(f"No item called {quel}")
def view():
    print("--")
    quel = input("Enter item name: ").lower
    if quel in inventory:
        lst = inventory[quel]
        print(f"Quanity: {lst[0]}")
        print(f"Price: {lst[1]}")
    else:
        print(f"No item called {quel}")

def showAll():
    print("--")
    for x,y in inventory.items():
        print(f"Name: {x}")
        print(f"Quantity: {y[0]}")
        print(f"Price: {y[1]}")
while True:
    print("Inventory Access")
    inp = int(input("""
To add an item, press 1
To remove an item, press 2
To update an item, press 3
To view an item, press 4
To exit, press 5
"""))
    if inp == 1:
        add()
        showAll()
    elif inp == 2:
        delete()
        showAll()
    elif inp == 3:
        update()
        showAll()
    elif inp == 4:
        view()
    elif inp == 5:
        break
    else:
        print("No operation available")
    print("--")