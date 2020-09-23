def title():
    print('\n')
    print('------------')
    print('Mangoes Home')
    print('--------v0.1')
    print('\n')
    input('Press enter to continue')

def menu(inGame):
    print('\n')
    print('Menu')
    print('------------')
    print('1. New Game')
    print('2. Load Game')
    print('3. Options')
    print('4. Controls')
    print('5. Quit')
    while True:
        menuChoice = input()
        # filters out non-integer inputs
        try:
            menuChoice = int(menuChoice)
        except:
            print('Invalid input')
            continue
        # determines wether the input falls in the acepted range
        if menuChoice >= 1 and menuChoice <= 5:
            return menuChoice
        else:
            print('Invalid input')

def new_game(inGame): # disable in game
    # if there is no save file, ask the user once more
    # make empty save file
    # go to game
    pass
def load_game(inGame): # disable in game
    # extract data from save files
    # 
    pass
def options(inGame):
    # display options
    #   difficulty
    #   some rates
    pass
def controls():
    # display control options
    print('\n')
    print('[A] Attack')
    print('[B] Block')
    print('[P] Potion')
    print('[R] Run')
    print('[I] Inventory')
    print('[M] Menu')

def quit(inGame):
    if inGame is True:
        # send player to main menu
        pass
    elif inGame is False:
        exit()


controls()