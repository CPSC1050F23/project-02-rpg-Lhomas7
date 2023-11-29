from room import Room
from adventure_map import AdventureMap
from inventory import Inventory
from item import Item
from room_not_found_error import RoomNotFoundError

def main():
    print("\nWelcome to the Adkins house! This time you won't be able to leave so easily. Goodluck.")

    # Initialize map w/room storage
    adventure_map = AdventureMap()
    
    # Initialize player inventory 
    inventory = Inventory()
    
    # Initialize Items
    book = Item("Book", "\"A Tale of Two Cities by Charles Dickens\". The greatest novel ever written.")
    book.set_action("read")
    book.set_item_content("You skip to the ending to read Sydney Carton's final speech:\n\tIt is a far, far better thing that I do, than I have ever done; it is a far far better rest that I go to than I have ever known.\nWhat a perfect ending...")
    
    fork = Item("Fork", "A conviently pronged eating utensil. Now I just need something to eat.")
    
    pizza_cutter = Item("Pizza Cutter", "This must be left over from the tragedy that occured at Adkins's Pizzeria!")
    
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

    adventure_map.add_room(Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen'], [harmonica]))
    adventure_map.add_room(Room("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study"], [book]))
    adventure_map.add_room(Room("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With is pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room"], [fork, pizza_cutter]))
    adventure_map.add_room(Room("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]))
    adventure_map.add_room(Room("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"], [key]))
    adventure_map.add_room(Room("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library"], [trophy]))
    adventure_map.add_room(Room("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom. You see a trapdoor hidden under the bed.", ["Study", "Trophy Room"], [picture]))
   
    # Input variations
    inputs = {"exit": ["exit", "leave"],
              "lookaround": ["look around", "lookaround", "look"],
              "pickup": ["pick up","pickup", "take", "grab"],
              }




if __name__ == "__main__":
    main()
