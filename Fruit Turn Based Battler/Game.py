import random, time, math

class Character:
    def __init__(self, name):
        self.isPlayer = True
        self.name = name
        self.level = 1
        self.xp = 0
        self.currentHealth = 150
        self.mult = {'ATK': 1, 'DEF': 1}
        # ATK is applied to increase outgoing damage, i.e. damageDealt * 1.5
        # DEF is used to reduce incoming damage, i.e. damageTaken * 0.8
        self.status = {'blocking': False, 'parrying': False, 'dodging': False, 
                        'vulnerable': False, 'stunned': False}
        self.items = {'potions': 1}
        # this value is edited by the attack methods and is used by deal_damage
        self.outgoingDamage = 0
        self.damageDealt = 0
        self.stunEnemy = False

    '''The following methods handle moves'''

    def sword(self):
        '''deals moderate, stable damage,
        scales with level'''
        baseDamage = 60
        damage = baseDamage + (10 * math.log(self.level) // 1)
        self.outgoingDamage = damage
        print(self.name, 'used sword\n')


    def dagger(self):
        '''low base damage but high max damage'''
        baseDamage = 40
        maxDamage = 80
        damage = random.randint(baseDamage, maxDamage) + (self.level * 2.5) // 1
        self.outgoingDamage = damage
        print(self.name, 'used dagger\n')


    def spell(self):
        '''delivers massive damage 1/5 times
        and does nothing the rest'''
        damage = 130
        num = random.randint(1, 4)
        print(self.name, 'used spell')
        if num == 1:
            self.outgoingDamage = damage
        else:
            print('Nothing happened...')
        print()


    def block(self):
        num = random.randint(2, 3)
        if num < 3:
            self.status['parrying'] = True
            print(self.name, 'parried\n')
            self.stunEnemy = True
        else:
            self.status['blocking'] = True
            print(self.name, 'blocked\n')
        self.outgoingDamage = 0


    def dodge(self):
        dodgeWorks = random.choice((True, False, False))
        if dodgeWorks:
            self.status['dodging'] = True
            print(self.name, 'got out of the way\n')
        else:
            print(self.name, 'tripped!\n')
            # make vulnerable
        self.outgoingDamage = 0
    

    def heal(self):
        if self.items['potions'] == 0:
            print(self.name, 'ran out of potions!\n')
        else:
            self.currentHealth = self.calculate_max_health()
            self.items['potions'] -= 1
            print(self.name, 'drank a health potion\n')
        self.outgoingDamage = 0

    '''The following methods handle user input'''

    def print_moves(self):
        print('\n     Attack      |      Defend     \n'
            '———————————————— | ————————————————\n'
            'Sword      [ 1 ] | Block      [ 4 ]\n'
            'Dagger     [ 2 ] | Dodge      [ 5 ]\n'
            'Spell      [ 3 ] | Heal       [ 6 ]\n'
            '———————————————————————————————————\n'
            'Inventory  [ i ] | Quit       [ q ]\n')

    def make_move(self):
        if self.status['stunned']:
            clear(20)
            print(self.name, 'is stunned!\n')
            self.status['stunned'] = False
            self.damageDealt = (0, False)
            input()
            return
        while True:
            move = input('\nYour move: ')
            if move.upper() == 'Q':
                print('Thank you for playing!\n')
                exit()
            elif move == '1':
                clear(20)
                self.sword()
            elif move == '2':
                clear(20)
                self.dagger()
            elif move == '3':
                clear(20)
                self.spell()
            elif move == '4':
                clear(20)
                self.block()
            elif move == '5':
                clear(20)
                self.dodge()
            elif move == '6':
                clear(20)
                self.heal()
            else: continue
            break
        self.damageDealt = self.deal_damage()


    '''The following methods handle
    outgoing/incoming damage'''

    def deal_damage(self):
        stun = self.stunEnemy
        self.stunEnemy = False
        damageDealt = int(self.outgoingDamage * self.mult['ATK'])
        self.outgoingDamage = 0 # resets the damage for the next turn
        return (damageDealt, stun)


    def take_damage(self, incomingDamage):
        damageTaken = incomingDamage[0] * self.mult['DEF']
        # cuts damage to 0 if dodging
        if self.status['dodging']:
            damageTaken = 0
            self.status['dodging'] = False # stops dodging
        # cuts damage by 60% if blocking
        elif self.status['blocking']:
            damageTaken = int(damageTaken * 0.4)
            self.status['blocking'] = False # stops blocking
        # cuts damage to 0 if parrying
        elif self.status['parrying']:
            damageTaken = 0
            self.status['parrying'] = False # stop parrying
        self.currentHealth -= damageTaken
        # stun
        if incomingDamage[1] is True and self.damageDealt[0] > 0:
            self.status['stunned'] = True
            print(self.name, 'has been stunned!\n')
        # ensures health doesn't go below 0
        if self.currentHealth < 0:
            self.currentHealth = 0
        if damageTaken > 0:
            print(self.name, 'took', damageTaken, 'damage!\n')

    '''The following methods handle formulas
    and are meant to be used internally'''

    def calculate_max_health(self):
        # health formula
        hp = int(math.log10(self.level ** 50) // 1) + 150
        return hp


    def calculate_xp_gained(self, enemyLevel):
        lowBound = 15
        upBound = 30
        # xp formula
        xp = random.randint(lowBound, upBound) + round(enemyLevel * 1.5)
        return xp
        
    
    def calculate_xp_per_level(self):
        levelCap = (self.level * 9)
        return levelCap

    
    def calculate_max_potions(self):
        maxPotions = 1 + self.level // 6
        return maxPotions

    '''The following methods take care of
    character functions'''

    def is_dead(self):
        if self.currentHealth <= 0:
            return True
        return False
    

    def win_battle(self, enemyLevel):
        # xp formula
        self.xp += self.calculate_xp_gained(enemyLevel)


    def print_xp(self):
        # do this one with percents...?
        xpBarLength = 20
        filledSquares = round(self.xp / self.calculate_xp_per_level() * xpBarLength)
        for num in range(xpBarLength):
            num += 1
            if num <= filledSquares:
                print('◼︎', end = '')
            else:
                print('◻︎', end = '')
        print('\n\nxp:', self.xp, '/', self.calculate_xp_per_level())


    def level_up(self):
        lvlUp = False
        while True:
            # the amount of xp needed to level up
            levelCap = self.calculate_xp_per_level()
            if self.xp >= levelCap:
                self.level += 1
                self.xp -= levelCap
                lvlUp = True
            else:
                # once a maximum has been reached, or if there isn't enough xp
                # update the values
                self.currentHealth = self.calculate_max_health() # health
                self.items['potions'] = self.calculate_max_potions() # potions
                break
        # determine if level increased
        if lvlUp:
            print('\nYou leveled up!\n')
            print('Current level:', player.level, '\n')
            # determine if potions were increased
            if self.level % 6 == 0:
                print('You now have', self.items['potions'], 'health potions!\n')
        else:
            print('Current level:', player.level, '\n')
        self.print_xp()


    def print_info(self):
        healthBarLength = self.calculate_max_health() // 10
        if self.currentHealth > 0 and self.currentHealth < 10:
            # makes the health bar have 1 heart if the hp
            # is below 10
            filledHearts = 1
        else:
            filledHearts = self.currentHealth // 10
        print()
        print(self.name)
        for num in range(healthBarLength):
            num += 1
            if num <= filledHearts:
                print('♥︎', end = '')
            else:
                print('♡', end = '')
        print(' ', self.currentHealth, '/', self.calculate_max_health())
        print('lvl', self.level)


class NPC(Character):
    def __init__(self, name, level):
        self.typesOfMove = {'attack': 7, 'defend': 10}
        self.possibleAttacks = {'sword': 9, 'dagger': 19, 'spell': 20}
        self.possibleDefenses = {'block': 7, 'dodge': 16, 'heal': 20}
        
        self.name = name
        self.level = level
        self.currentHealth = self.calculate_max_health()
        self.mult = {'ATK': 1, 'DEF': 1, 'dodgeBonus': 1}
        # ATK is applied to increase outgoing damage, i.e. damageDealt * 1.5
        # DEF is used to reduce incoming damage, i.e. damageTaken * 0.8
        self.status = {'blocking': False, 'parrying': False, 'dodging': False, 'stunned': False}
        self.outgoingDamage = 0 # this value is edited by the attack methods and is used by deal_damage
        self.damageDealt = 0 # this is the damage value that makes it out of the object
        self.stunEnemy = False
        self.items = {'potions': 1 + self.level // 5}


    def generate_move(self):
        if self.status['stunned']:
            print(self.name, 'is stunned!')
            self.status['stunned'] = False
            self.damageDealt = (0, False)
            return
        typeOfMove = random.randint(1, 10)
        move = random.randint(1, 20)
        if typeOfMove <= self.typesOfMove['attack'] or self.currentHealth > ( 3 * self.calculate_max_health() // 4):
            if move <= self.possibleAttacks['sword']:
                self.sword()
            elif move <= self.possibleAttacks['dagger']:
                self.dagger()
            else:
                self.spell()
        else:
            if move <= self.possibleDefenses['block']:
                self.block()
            elif move <= self.possibleDefenses['dodge']:
                self.dodge()
            else: # this option currently can't happen
                self.heal()
        self.damageDealt = self.deal_damage()


class boss(NPC, Character):
    pass
    

def title_and_menu():
    print('\n————————————————————————')
    print('❖ B A T T L E  G A M E ❖')
    print('——————————————————v2.1——\n')
    clear(2)
    input('Press enter to play')
    print()


def npc_name(tupleOfNames):
    name = random.choice(tupleOfNames)
    return name


def display_round(num):
    print()
    line(14 + len(str(num)))
    print('◇ R O U N D', num, '◇')
    line(14 + len(str(num)))
    print()


def line(n):
    line = ''
    for _ in range(n):
        line += '—'
    print(line)


def clear(n):
    for _ in range(n):
        print('\n\n\n\n\n')


# game

player = Character('Mango')
npcLevel = 0
clear(20)
title_and_menu()
while True:
    clear(20)
    npcLevel += 1
    display_round(npcLevel)
    npcName = npc_name(('Dragonfruit', 'Peach', 'Tim Apple', 'Banana-nana', 'Melon Knight', 'CheriBomb', 'Rhino Beetle', 'Venus Fly Trap'))
    enemy = NPC(npcName, npcLevel)
    # setup
    player.print_info()
    enemy.print_info()
    player.print_moves()
    while True:
        # fight
        '''screen clears here'''
        player.make_move()
        enemy.generate_move()
        enemy.take_damage(player.damageDealt)
        player.take_damage(enemy.damageDealt)
        # print halth bar
        player.print_info()
        enemy.print_info()
        # print move menu
        player.print_moves()
        # checking status
        if player.is_dead():
            print('\nYou died...\n')
            exit()
        if enemy.is_dead():
            print(enemy.name, 'died', end = '')
            input()
            clear(20)
            print('\n~~~~~~~~~~~~~~~~~~~~~~')
            print('       You win!       ')
            print('~~~~~~~~~~~~~~~~~~~~~~\n')
            player.win_battle(npcLevel)
            player.level_up()
            input('\nPress Enter for next round')
            print()
            break






# repurpose make_move to work for both



''' Improvements:
    Dodge:
        -work 1/2 times
        -when it works, it grants a counterattack that deals 1.x the damage of the incoming attack
        -when it doesn't, receive 1.x the damage (bc ur caught off guard)
    Block: (DONE)
        -if i add *, make it block all health and stun the enemy when parry is succesful (1/3 times...?)
        -the rest of the times, take reduced damage
    Heal:
        -add a limit to how many you can use per round
        -make it heal completely
        -maybe increase with each 10 levels...?
        -make enemy more likely to heal if health is low

    *Maybe make the attack that is release a tuple containing attack damage and outgoing status effects...? (DONE)
'''
