import time  # Used to add delays for better user experience

# Ask for the player's name and format it
name = input("Type Your Name: ").strip().title()
print(f"\nWelcome, {name}, to this Adventure!!\n")

inventory = []  # List to store items the player collects

# First choice: go left or right
answer = input("You are on a dirt road, and it has come to an end. "
               "You can go left or right. Which way would you like to go? (left/right): ").strip().lower()

# If player chooses left path
if answer == "left":
    print("\nYou walk down the path and arrive at a river. You can:")
    time.sleep(1)
    print("1. Swim across (type 'swim')")
    print("2. Walk around it (type 'walk')")
    print("3. Look for a boat (type 'boat')")

    a1 = input("What do you choose? ").strip().lower()

    if a1 == "swim":
        print("\nYou start swimming, but halfway through, an alligator attacks you. Game Over!")

    elif a1 == "walk":
        print("\nYou walked for miles, ran out of water, and collapsed. Game Over!")

    elif a1 == "boat":
        print("\nYou find an old boat and row across the river safely.")
        time.sleep(1)
        print("On the other side, you see a cave and a small village.")
        # Player chooses between cave or village
        a2 = input("Do you explore the 'cave' or go to the 'village'? ").strip().lower()

        if a2 == "cave":
            print("\nInside the cave, you find a treasure chest!")
            time.sleep(1)
            # Decide whether to open the chest
            choice = input("Do you 'open' it or 'leave' it? ").strip().lower()

            if choice == "open":
                print("\nThe chest is filled with gold! You WIN!")
            else:
                print("\nYou leave the treasure behind and exit the cave. The adventure ends.")

        elif a2 == "village":
            print("\nThe villagers welcome you and offer you food. You rest and continue your journey. You WIN!")

        else:
            print("\nNot a valid choice! You get lost in the wilderness. Game Over!")

    else:
        print("\nInvalid choice! You Lose!")

# If player chooses right path
elif answer == "right":
    print("\nYou walk down the path and reach a rickety bridge.")
    time.sleep(1)
    print("1. Cross it (type 'cross')")
    print("2. Go back (type 'back')")
    print("3. Look for another way around (type 'search')")

    a2 = input("What do you choose? ").strip().lower()

    if a2 == "back":
        print("\nYou go back and get lost in the forest. Game Over!")

    elif a2 == "cross":
        print("\nYou cross the bridge and meet a stranger.")
        time.sleep(1)
        # Decide whether to talk to the stranger
        a3 = input("Do you talk to them? (yes/no): ").strip().lower()

        if a3 == "yes":
            print("\nThe stranger gives you a magical key!")
            inventory.append("magic key")  # Add item to inventory
            print("You continue walking and find an old haunted house.")
            # Decide to enter house or keep walking
            choice = input("Do you enter the 'house' or 'keep walking'? ").strip().lower()

            if choice == "house":
                print("\nInside the house, you find a locked door. Luckily, you have the magic key!")
                time.sleep(1)
                print("Behind the door, you find a hidden treasure. You WIN!")
            else:
                print("\nYou walk past the house and find nothing. The adventure ends.")

        else:
            print("\nThe stranger was a wizard. You ignored him, and he cursed you. Game Over!")

    elif a2 == "search":
        print("\nYou find a secret tunnel under the bridge. You crawl through and end up in a hidden cave.")
        time.sleep(1)
        print("Inside, you find an old sword.")
        inventory.append("sword")  # Add sword to inventory
        print("With the sword in hand, you exit the cave and see a castle in the distance.")
        # Decide to go to castle or back to bridge
        castle = input("Do you go to the 'castle' or go back to the 'bridge'? ").strip().lower()

        if castle == "castle":
            print("\nAt the castle, you find a dragon guarding the entrance.")
            if "sword" in inventory:
                print("You use your sword to defeat the dragon and claim the treasure inside. You WIN!")
            else:
                print("You have no weapon! The dragon eats you. Game Over!")
        else:
            print("\nYou go back to the bridge but fall into the river. Game Over!")

    else:
        print("\nInvalid choice! You Lose!")

else:
    print("\nInvalid choice! You Lose!")

# End of the game
print("\nThanks for playing! Try again for a different adventure.")
