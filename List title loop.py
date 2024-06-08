shoppinglist = []
max_items = 2
while len(shoppinglist) < max_items:
    item = input("What would you like to buy? ")
    shoppinglist.append(item)
    print('Excellent! YUM YUM!')
    print('\n')
print('\n')
print('Choosen only the best sir!')
print('\n')
for food in shoppinglist:
    print(food.title())
print('\n')