"""
Author:         Landon Thomas
Date:           12/7/23
Assignment:     Project 02 RPG
Course:         CPSC1050
Course Section:    020

CODE DESCRIPTION:
This code is effectively a game, it takes user input and navigates through a house that holds
all different rooms, items, and actions those items and the user can perform. The user has
an inventory in which they hold their items as they naviaget the house. At the end of the user's
game, the code will write a log to the gamelog file displaying the number of steps it took the user
to complete the game. It makes use of classes, modules, files, functions, and loops.
"""









from room import Room
from adventure_map import AdventureMap
from inventory import Inventory
from item import Item
from room_not_found_error import RoomNotFoundError
#defines main class to run all code
def main():
    print("\nWelcome to the Adkins house! This time you won't be able to leave so easily. Goodluck.")
    word_string = "don't"

    # Initialize map w/room storage
    adventure_map = AdventureMap()
    
    # Initialize player inventory 
    inventory = Inventory()

    # Input variations
    inputs = {"exit": ["exit", "leave"],
              "lookaround": ["look around", "lookaround", "look"],
              "pickup": ["pick up","pickup", "take", "grab"],
              }

    exit_error = RoomNotFoundError()
    # Initialize Items
    book = Item("Book", "\"A Tale of Two Cities by Charles Dickens\". The greatest novel ever written.")
    book.set_action("read")
    book.set_item_content("You skip to the ending to read Sydney Carton's final speech:\n\tIt is a far, far better thing that I do, than I have ever done; it is a far far better rest that I go to than I have ever known.\nWhat a perfect ending...")
    
    fork = Item("Fork", "A conveniently pronged eating utensil. Now I just need something to eat.")
    
    pizza_cutter = Item("Pizza Cutter", "This must be left over from the tragedy that occurred at Adkin's Pizzeria")
    
    harmonica = Item("Harmonica", "A mouth organ. This might keep me entertained for a couple of hours.")
    harmonica.set_action("play")
    harmonica.set_item_content("You play the sweet sweet melodies of Piano Man on the harmonica. If only someone could hear you...")
    
    key = Item("Key", "A golden key. This has to unlock something. Right?")
    key.set_action("unlock")
    key.set_item_content("You unlock the trapdoor under the bed. You crawl through it and into the real world.\nParadiso awaits.\nCongratulations.")
    
    trophy = Item("Old Trophy", "An old youth bowling league trophy. The words engraved in the plaque are: \"Highest Youth Average: Richard Khouri 186\"")
    
    picture = Item("Picture", "An old picture found on the night stand.")
    picture.set_action("inspect")
    picture.set_item_content("You take a closer look at the picture. It's an old picture of Evan Kessler and Richard Khouri back when they studied at Clemson. Good times.")
    # add rooms to adventuremap for playing the game.
    adventure_map.add_room(Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen'], [harmonica]))
    adventure_map.add_room(Room("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study"], [book]))
    adventure_map.add_room(Room("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room"], [fork, pizza_cutter]))
    adventure_map.add_room(Room("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]))
    adventure_map.add_room(Room("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"], [key]))
    adventure_map.add_room(Room("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library",], [trophy]))
    adventure_map.add_room(Room("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom. You see a trapdoor hidden under the bed.", ["Study", "Trophy Room"], [picture]))
    adventure_map.add_room(Room('none','none',[],[]))
    #begin at study
    print(adventure_map.get_room('Study'))
    #list of possible actions to be taken in the game
    actions = ['read','play','unlock','inspect']
    # counts the number of steps taken to complete the game and is printed out in the gamelog
    num_steps_of_game = 0
    #keeps track of the room the player is currently in
    current_room = 'Study'
    #runs until player exits game
    while True:
        print('Please choose an action:')
        user_action = input().lower().strip()
        #takes user input if user input is to exit, and verifies that they want to exit and validates input with RoomNotFoundError
        if user_action in inputs['exit']:
            print('Where would you like to go?')
            user_exit = input().lower().strip()
            user_exits = user_exit.split()
            user_exit = ''
            first_item = True
            for item in user_exits:
                if first_item:
                    item = item.capitalize()
                    user_exit += item
                    first_item = False
                    continue
                item = item.capitalize()
                user_exit += ' ' + item
            if user_exit in adventure_map.get_room_exits(current_room):
                print(adventure_map.get_room(user_exit))
                current_room = user_exit
                num_steps_of_game += 1
            else:
                print(exit_error.__str__(user_exit))
                num_steps_of_game += 1  
        #allows the user to lookaround the room if it is their input, distinguishes between a room with items and one without
        elif user_action in inputs['lookaround']:
            if len(adventure_map.get_rooms_and_items(current_room)) == 0:
                print(f'{adventure_map.get_room_description(current_room)}\nYou find some items around you: There are no items around here.')
                num_steps_of_game += 1
            else:
                print(f'{adventure_map.get_room_description(current_room)}\nYou find some items around you: {adventure_map.get_string_of_items(current_room)}.')
                num_steps_of_game += 1
        #allows the user to pickup an item if it is in the room and removes it from the adventuremap and into the inventory
        elif user_action in inputs['pickup']:
            if len(adventure_map.get_rooms_and_items(current_room)) == 0:
                print('Nothing to pickup')
                num_steps_of_game += 1
            else:              
                print(f'Picked up {adventure_map.get_rooms_and_items(current_room)[0].get_item()}.')
                inventory.add_inventory(adventure_map.get_rooms_and_items(current_room)[0])
                adventure_map.remove_item(current_room)
                num_steps_of_game += 1
        #performs the action of items held only in the player's inventory  
        elif user_action in actions:
            if user_action == 'unlock' and current_room == 'Bedroom' and key in inventory.get_inventory():
                print('You unlock the trapdoor under the bed. You crawl through it and into the real world.\nParadiso awaits.\nCongratulations.')
                num_steps_of_game += 1
                break
            are_done = False
            for item in inventory.get_inventory():
                if item.get_action() == user_action:
                    print(item.get_item_content())
                    num_steps_of_game += 1
                    are_done = True
            if not are_done:
                print(f"I don't have anything to {user_action}. ")
                num_steps_of_game += 1
        #displays the user's inventory
        elif user_action == 'inventory':
            inventory.print_inventory()
            num_steps_of_game += 1
        #tells the user that their requested action is unknown
        else:
            print(f'I {word_string} know the word "{user_action}".')
            num_steps_of_game += 1
    #converts the number of steps into a string and prints it in the game log
    num_steps_of_game = str(num_steps_of_game)
    with open('gamelog.txt','w') as f:
        f.write(f'Congratulations! You finished the game in {num_steps_of_game} steps.')
    f.close()
        










if __name__ == "__main__":
    main()
