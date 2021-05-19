inventory = {'Rope': 1, 'Torch': 6, 'Gold': 42, 'Dagger': 1, 'Bow': 1, 'Arrow(s)': 12}
dragonLoot = ['Gold', 'Dagger', 'Gold', 'Gold', 'Ruby']

def displayLoot(loot):
    
    print('Loot:')
    for i in range(len(loot)):
        print(str(loot[i]))
    
def takeLoot(inventory, loot):
    print('Loot all?(y/n)')
    while True:
        toloot = str(input())
        if toloot == 'y' or toloot =='Y':
            addToInventory(inventory, loot)
            break
        elif toloot == 'n' or toloot == 'N':
            break
        else:
            print('Sorry did you want to loot?(y/n)')

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ': ' + str(v))
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] += 1
displayInventory(inventory)
print("You've slain a monster!")
displayLoot(dragonLoot)
takeLoot(inventory, dragonLoot)
displayInventory(inventory)
