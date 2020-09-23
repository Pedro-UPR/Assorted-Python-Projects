import math
import random
import time

class UI:
    '''This class defines ui elements'''
    def title(self):
        print('\n')
        print('--------------------')
        print('B A T T L E  G A M E')
        print('----------------v1.1')
        print('\n')
        input('Press enter to continue')

    def interactive_menu(self):
        print('\n')
        print('Menu')
        print('------------')
        print('1. Play Game')
        print('2. Controls')
        print('3. Quit')
        print('\n')
        while True:
            menuChoice = input()
            # filters out non-integer inputs
            try:
                menuChoice = int(menuChoice)
            except:
                print('Invalid input')
                continue
            # determines wether the input falls in the acepted range
            if menuChoice >= 1 and menuChoice <= 3:
                return menuChoice
            else:
                print('Invalid input')
    
    def display_controls(self):
        # display control options
        print('\n')
        print('Controls')
        print('----------')
        print('[A] Attack')
        print('[B] Block')
        print('[P] Potion')
        print('[Q] Quit')
        print('\n')
        input('Press enter to continue')

    def quit_game(self):
        print('\n')
        quit = input('Quit? [Q]')
        print('\n')
        if quit.upper() == 'Q':
            return False
        return True

    def display_round(self, currentRound):
        print('')
        print('~~~~~~~~~')
        print('ROUND', currentRound)
        print('~~~~~~~~~')

    def display_battle_stats(self, roundAchieved, enemyLevel, playerLevel):
        print('')
        print('Round achieved:', roundAchieved)
        print('Your level:', playerLevel)
        print('Lost to: lvl', enemyLevel, 'enemy')
        print('')


class Character:
    '''Template for a character that contains
    methods for attacking, defending, leveling,
    figuring out if its dead, etc'''

    name = None
    level = 1
    exp = 0
    baseDamage = ((level ** 4) // 1000) + 5
    baseBlock = ((level ** 4) // 100)
    damageBlocked = None
    health = int(math.log10(level ** 20)) + 20
    multiplier = {'ATK': 1, 'DEF': 1, 'EXP': 1} # unused as of now

    def __init__(self, name):
        self.name = name

    def attack(self):
        '''Computes damage'''
        criticalHit = random.randint(-17, 5) * self.multiplier['ATK']
        if criticalHit < 0:
            criticalHit = 0
        damageDealt = round((self.baseDamage * self.multiplier['ATK'])) + criticalHit
        return damageDealt
    
    def block(self):
        damageBlocked = round(self.baseBlock * self.multiplier['DEF']) + random.randint(2, 5)
        self.damageBlocked = damageBlocked

    def receive_damage(self, damageReceived):
        '''Receives the damage as input and modifies the health variable'''
        if self.damageBlocked is not None:
            damageReceived -= self.damageBlocked
            self.damageBlocked = None
        if damageReceived < 0:
            damageReceived = 0
        self.health -= damageReceived * self.multiplier['DEF']
        if self.health < 0:
            self.health = 0
        return damageReceived

    def is_dead(self):
        '''Retruns wether a character is dead or not'''
        if self.health <= 0:
            return True
        return False

    def win_battle(self, enemyLevel):
        lowBound = round(enemyLevel * self.multiplier['EXP']) + 10
        upBound = round(enemyLevel * self.multiplier['EXP']) + 15
        gainedEXP = random.randint(lowBound, upBound)
        self.health = int(math.log10(self.level ** 20)) + 20
        self.exp += gainedEXP

    def level_up(self):
        while True:
            levelCap = self.level * 10
            if self.exp >= levelCap:
                leftOver = self.exp - levelCap
                self.exp = leftOver
                self.level += 1
                if self.exp >= levelCap:
                    continue
                else:
                    self.baseDamage = ((self.level ** 4) // 1000) + 5
                    self.baseBlock = ((self.level ** 4) // 100)
                    self.health = int(math.log10(self.level ** 20)) + 20
                    return True
            else:
                return False
    
    def display_health(self):
        healthBarLength = int(math.log10(self.level ** 20)) + 20
        for num in range(healthBarLength):
            if num < self.health:
                print('♥︎', end = '')
            else:
                print('♡', end = '')
        print('\n')


class NPC(Character):
    '''This class inherits Character
    but adds a make_move method
    to let the NPC deciede a move
    without user input'''

    possibleMoves = {'Attack': 30, 'Block': 20,}

    def __init__(self, level):
        self.level = level
        self.health = int(math.log10(level ** 20)) + 20

    def make_move(self):
        num = random.randint(1, 50)
        if num >= self.possibleMoves['Attack']:
            return self.attack()
        else:
            self.block()
            return None       


def delay(text):
    print(text)
    time.sleep(0.5)

def clear():
    for _ in range(100):
        print()


ui = UI() # initializes the user interface

programIsRunning = True
ui.title()
while programIsRunning:
    # manage menu and input
    menuChoice = ui.interactive_menu()
    if menuChoice == 2:
        ui.display_controls()
        continue
    elif menuChoice == 3:
        break
    # game
    playerName = input('\nChoose your name: ')
    player = Character(playerName)
    gameIsRunning = True
    currentRound = 0
    clear()
    while gameIsRunning:
        currentRound += 1
        ui.display_round(currentRound)
        enemy = NPC(currentRound)
        fightIsLive = True
        while fightIsLive:
            print('\nEnemy\'s health:', enemy.health)
            enemy.display_health()
            print(playerName + '\'s health: ' + str(player.health))
            player.display_health()
            # checks for victory / loss
            if player.is_dead():
                print('')
                print(playerName, 'died...')
                fightIsLive = False
                gameIsRunning = False
                continue
            elif enemy.is_dead():
                delay('•••')
                print(playerName, 'wins!')
                player.win_battle(enemy.level)
                print('Gained', player.exp, 'XP')
                levelIsRaised = player.level_up()
                if levelIsRaised:
                    print('Level up! New level:', player.level)
                input('\nPress enter for next round')
                fightIsLive = False
                continue
            # player turn
            playerMove = input()
            clear()
            delay('')
            if playerMove.upper() == 'Q':
                print('Thank you for playing!\n')
                exit()
            elif playerMove.upper() == 'A':
                playerDamageDealt = player.attack()
                print(playerName, 'attacked for', playerDamageDealt, 'damage')
            elif playerMove.upper() == 'B':
                playerDamageDealt = 0
                player.block()
                print(playerName, 'blocked')
            else:
                print('\nInvalid move!\n')
                continue
            delay('')
            # npc turn
            enemyDamageDealt = enemy.make_move()
            enemyDamageReceived = enemy.receive_damage(playerDamageDealt)
            # fight
            if enemyDamageDealt is None:
                print('Enemy blocked')
                print('Enemy took', enemyDamageReceived, 'damage\n')
            else:
                print('Enemy took', enemyDamageReceived, 'damage')
                print('Enemy dealt', enemyDamageDealt, 'damage')
                playerDamageReceived = player.receive_damage(enemyDamageDealt)
                print(playerName, 'took', playerDamageReceived, 'damage\n')
    ui.display_battle_stats(currentRound, enemy.level, player.level)

                
            

# Comment on the code
# Add xp left for next level