print("Welcome to Tresure Island\nYour mission is to find the tresure.")
choice1 = input(
    "You\'re at a crossroad, where do you want to go? Type 'left' or 'right'. ").lower()
if choice1 == 'left':
    choice2 = input(
        "You\'ve come to a lake. There is an island in the middle of the lake. Do you choose to 'wait' or 'swim' across? ")
    if choice2 == 'wait':
        choice3 = input(
            "You arrive at the island thanks to Gangplank. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you pick? ").lower()
        if choice3 == 'red':
            print("You overextended a Brand mid, gg ez Brand fed, Game Over. ")
        elif choice3 == 'yellow':
            print("You managed to get to the Tresure, being full build at 20 minutes. Now you are the diff across all lanes 😈.")
        elif choice3 == 'blue':
            print("You face a Garen jungle and get 13/0'd, gg ez jungle diff. Game Over.")
        else:
            print("You didn't pick a door and end up getting 1v5'd where everyone used their ult. gg ez team diff. Game Over.")
    else:
        print("You tried to swim but Tahm Kench one shot you with his ult, gg ez top diff, Game Over.")
else:
    print("You're facing a level 18 Yasuo, gg ez ADC diff, Game Over.")
