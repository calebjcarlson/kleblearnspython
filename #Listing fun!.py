#Listing fun!
party_guests = []
def picker():
   while True prompt = ('Add Guest: 1 Remove Guest: 2 See Guests: 3', '\n', 'What would you like to do? ')
    print(prompt)
    choice = input().strip()
    
    if choice == '1':
        add = input('Who do you want to add? ').strip()
        party_guests.append(add)
        home ()
    elif i == '2':
        if party_guests:
            remove = input('Who do you want to remove? ').strip()
            party_guests.remove(remove)
        else:
            print('No guests to remove')
        picker()



