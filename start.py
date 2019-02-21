objects: {
    keys: {count: 2,
            methods: [be seen/found, picked up, used to open door]},
    furniture: {count: 5,
                attribute: type,
                methods: [opened/turned over, shake, move]}
    doors: {count Number,
            attribute: locked,
            }
    player: {count: 1,
            attribute: has keys,
            method: [walk/move, open door],
            movement/directions: [north, sourth, east, west]
            }
    rooms: {count: 10,
            attribute: location(use grid to allow navigation by
                directions functions, and try/except to prevent
                movement if no room exists),
                }
}
def bedroom():
    print('You are in a bedroom. A window is open and the sun is shining in.')
    print('There is a cell phone, resting on top of a chest of drawers.')
    print('north: Hallway')
    print('south: Bathroom')
    choice = input('? ')
    if choice == 'north':
        hallway()
    elif choice == 'south':
        bathroom()
    else:
        bedroom()
#
def bathroom():
    print('You are in a small bathroom. Everything is sparkling clean, except')
    print('there is toothpaste smeared on the counter. One small window lets')
    print('a bright beam of sunshine in.')
    print('north: Bedroom')
    choice = input('? ')
    if choice == 'north':
        bedroom()
    else:
        bathroom()

def hallway():
    print('You are in a long hallway. Everything is sparkling clean, except')
    print('there is toothpaste smeared on the wall. One small window lets')
    print('a bright beam of unicorns in.')
    print('north: Bathroom')
    print('south: continue down hallway')
    choice = input('? ')
    if choice == 'north':
        bathroom()
    elif choice == 'south':
        hallway()
    else:
        bedroom()

bedroom()

print('-------------')
"""
Bonus Challenge:
1. Make it so that you can pick up the phone while in the bedroom with a
command "take phone".
2. Once picked up, make it so that the phone will "start ringing" after
traveling to a few different rooms.

HINT: You will probably need to use a variable to mark that the user has
picked up the phone. For this, look up the "global" keyword in Python, it
might come in handy, as it allows functions to share variables.
"""

if __name__ == "__main__":
    main()
