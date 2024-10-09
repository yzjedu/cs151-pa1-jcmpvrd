print("You have suddenly woken up in a mysterious castle. The air is very cold, and you hear voices all around you.")
print("The only way to escape this castle is through it and it is filled with puzzles, magic, and choices.")

name = input("Enter your name:")

print(f"{name}, you have an orb with numbers floating near it.")
orb_number = int(input("Please select a number between 1 and 20."))

if orb_number < 5:
    print("Going through Path A.")
    print("You are safe. Proceed with caution!")
elif 5 <= orb_number <= 10 :
    print("Going through Path B.")
    print("You are safe. Proceed with caution!")
else:
    print("Going through Path C.")
    print("You were almost captured by a guard.")

potion_portion = float(input("You have found a potion. How much of the potion would you like to drink 0.0 to 1.0"))

if potion_portion <= 0.3 :
    print("Going through Path D.")
    print("Your vision has begun to blur.")
elif 0.3 < potion_portion <= 0.6 :
    print("Going through Path E.")
    print("You have drunken a small amount but are still functional")
else:
    print("Going through Path F.")
    print("You have gained great powers that will help you escape.")

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
    stair_choice = input("You have two different stairs to choose from.You must make a choice: Left or Right ?")

    if stair_choice == "Left" :
        print("Going through Path J.")
        print("You must answer the following riddle presented to you.")
        break
    elif stair_choice == "Right" :
        print("Going through Path K.")
        print("You must answer the following riddle presented to you.")
        break
    else:
        print("Invalid choice. Please choose 'Left' or 'Right'.")

riddle_choice = int(input("Pick which riddle you would like to solve, 1 or 2: "))

if riddle_choice == 1 and stair_choice == "Left" :
    print("You have made it through the castle.")
elif riddle_choice == 2 and stair_choice == "Left" :
    print("You failed to escape the castle.")
elif riddle_choice == 1 and stair_choice == "Right" :
    print("You failed to escape the castle.")
elif riddle_choice == 2 and stair_choice == "Right" :
    print("You have made it through the castle.")
else:
    print("Invalid riddle choice. You remain trapped forever.")
