import random


def msg(room) :
    if room['msg'] =='':
        return 'You have entered the ' + room['name'] + '.'
    else:
        return room['msg']


def get_choice(room,dir) :
    if dir =='N':
        choice = 0
    elif dir =='E':
        choice = 1
    elif dir =='S':
        choice = 2
    elif dir =='W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice


def main() :
    dirs = (0,0,0,0) #tupple (immutable)

    #rooms are defined as dictionaries with three properties:
    #Name, directions and message

    entrance = {'name':'Entrance Way', 'directions':dirs, 'msg':''}
    livingroom = {'name':'Livingroom', 'directions':dirs, 'msg':''}
    hallway = {'name':'Hallway', 'directions':dirs, 'msg':''}
    kitchen = {'name':'Kitchen', 'directions':dirs, 'msg':''}
    diningroom = {'name':'Diningroom', 'directions':dirs, 'msg':''}
    family_room = {'name':'Family Room', 'directions':dirs, 'msg':''}

    #specifying the directions for each of the rooms
    #We didn't do this in the previous dictionaries because all the rooms were not defined
    entrance['directions'] = (kitchen, livingroom, 0, 0)
    livingroom['directions'] = (diningroom,0,0, entrance)
    hallway['directions'] = (0,kitchen,0, family_room)
    kitchen['directions'] = (0,diningroom,entrance,hallway)
    diningroom['directions'] = (0, 0, livingroom, kitchen)
    family_room['directions'] = (0, hallway, 0, 0)

    #rooms where the basket and eggs might be (all except entrance)
    rooms = [livingroom, hallway, kitchen, diningroom, family_room]
    #hide the eggs in a random room everytime
    room_with_eggs = random.choice(rooms)
    #Keep entering the loop
    eggs_delivered = False
    #starting room
    room = entrance

    #Start of the game

    print('Hello pirate! Are you brave enough to find the treasure?')

    while True :
        if eggs_delivered and room['name'] == 'Entrance Way':
            print('Congrats! You finished the game! You can now leave with your prize.')
            break;

        elif not eggs_delivered and room['name'] == room_with_eggs['name']:
            eggs_delivered = True
            print(msg(room) + ' There is the treasure! Now get out quick, other pirates are also searching for it!')
            room['msg'] = ('You are back in the ' + room['name'] + '! Get out!')
        else:
            print(msg(room))
            room['msg'] = 'You are back in the ' + room['name']

        stuck = True
        while stuck:
            dir = raw_input("Which direction do you want to go: N, E, S or W? (North, East, South or West) ")
            choice = get_choice(room,dir)

            if choice == -1:
                print("Please enter N, E, S or W")
            elif choice == 4:
                print("You can not go in that direction.")
            else:
                room = room['directions'][choice]
                stuck = False


main()
