def treasure_island():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    choice_1 = input('You\'re at a crossroad, Left(L) or Right(R):')
    if choice_1.upper() != 'L':
        print('You\'ve fell into a hole\nGAME OVER')
    else:
        choice_2 = input('You\'ve come to a lake, do you swim(S) or wait(W):')
        if choice_2.upper() == 'W':
            choice_3 = input('You\'ve arrived at an island unharmed. There is house with 3 doors.\nWhich door do you take? Yellow - (Y), Red - (R), or Blue- (B)')
            if choice_3.upper() == 'Y':
                print('You enter the room and are teleported to safety with nothing.')
            elif choice_3.upper() == 'R':
                print('You enter the room and are teleported to safety with all the treasures of the island.')
            elif choice_3.upper() == 'B':
                print('You enter the room and are mauled to death.')
            else:   
                print('You\'ve decided to do nothing and stood till you died of dehydration.')
        else:
            print('You\'ve decided to swim and have drowned... silly really.')
    exit()
treasure_island()

