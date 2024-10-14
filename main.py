# Programmers:  Jordi Campoverde
# Course:  CS151, Dr.Yalew
# Due Date: 10/9/2024
# Programming Assignment: 1
# Problem Statement: You are creating a text adventure game! In this game, the user gives input that affects the path of the story
# Data In: Name, orb number, potion portion, word choice, stair choice, and riddle choice
# Data Out: Descriptive text about the player's choices and the paths they take through the game. Results based on player’s decisions, such as whether they successfully escape the castle or not.
# Credits: Belong to me and uses is based on the code learned from class.

# Introduction to the story, setting up the player's environment.
print("You have suddenly woken up in a mysterious castle. The air is very cold, and you hear voices all around you.")
print("The only way to escape this castle is through it and it is filled with puzzles, magic, and choices.")

# Asking the player for their name.
name = input("Enter your name:")

# Introducing the orb with numbers and asking the player to choose a number.
print(f"{name}, you have an orb with numbers floating near it.")
orb_number = int(input("Please select a number between 1 and 20."))

# Based on the number chosen, guiding the player down different paths.
if orb_number < 5:
    print("Going through Path A.")
    print("You are safe. Proceed with caution!")
elif 5 <= orb_number <= 10 :
    print("Going through Path B.")
    print("You are safe. Proceed with caution!")
else:
    print("Going through Path C.")
    print("You were almost captured by a guard.")

# Asking the player how much potion they would like to drink.
potion_portion = float(input("You have found a potion. How much of the potion would you like to drink 0.0 to 1.0"))

# Based on the amount of potion consumed, guiding the player to different outcomes.
if potion_portion <= 0.3 :
    print("Going through Path D.")
    print("Your vision has begun to blur.")
elif 0.3 < potion_portion <= 0.6 :
    print("Going through Path E.")
    print("You have drunken a small amount but are still functional")
else:
    print("Going through Path F.")
    print("You have gained great powers that will help you escape.")

# Loop to continuously ask the player for a valid word choice until they provide one.
while True:
    word_choice = input("You have found a door. Tell it one of these words: ‘Whisper’, ‘Break’, or ‘Open’: ")

    if word_choice == "Whisper":
        print("Going through Path G.")
        print("The door opens slightly allowing you to squeeze through quietly.")
        break
    elif word_choice == "Break":
        print("Going through Path H.")
        print("The door has shattered open, and the guards are on high alert.")
        break
    elif word_choice == "Open":
        print("Going through Path I.")
        print("The door begins to open slowly, and you are able to pass through safely.")
        break
    else:
        print("Invalid choice. Please choose a valid word: ‘Whisper’, ‘Break’, or ‘Open’.")



while True:
    # Asking the player for a word to open the door.
    stair_choice = input("You have two different stairs to choose from.You must make a choice: Left or Right ?")

    # Based on the word choice, different outcomes occur.
    if stair_choice == "Left" :
        print("Going through Path J.")
        print("You must answer the following riddle presented to you.")
        break
    elif stair_choice == "Right" :
        print("Going through Path K.")
        print("You must answer the following riddle presented to you.")
        break
    else:
        # If the player provides an invalid stair choice, they are prompted again.
        print("Invalid choice. Please choose 'Left' or 'Right'.")

# Asking the player to choose which riddle they would like to solve.
riddle_choice = int(input("Pick which riddle you would like to solve, 1 or 2: "))

# Depending on the combination of stair and riddle choices, the outcome is determined.
if riddle_choice == 1 and stair_choice == "Left" :
    # If the player chose "Left" and riddle 1, they succeed.
    print("You have made it through the castle.")
elif riddle_choice == 2 and stair_choice == "Left" :
    # If the player chose "Left" and riddle 2, they fail.
    print("You failed to escape the castle.")
elif riddle_choice == 1 and stair_choice == "Right" :
    # If the player chose "Right" and riddle 1, they fail.
    print("You failed to escape the castle.")
elif riddle_choice == 2 and stair_choice == "Right" :
    # If the player chose "Right" and riddle 2, they succeed.
    print("You have made it through the castle.")
else:
    # If the player provides an invalid riddle choice, they remain trapped.
    print("Invalid riddle choice. You remain trapped forever.")
