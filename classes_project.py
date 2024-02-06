import random


class InventoryItem:
    def __init__(self, item_name, body_part):
        self.item_name = item_name
        self.body_part = body_part

    def __repr__(self):
        return f'{self.item_name}'


class Character:
    def __init__(self, name, level=1, experience=0, strength=0,
                 agility=0, intelligence=0, health=100, attack_type='', attack_dmg=0,
                 char_class='BaseCharacterMannequin'):
        self.name = name
        self.experience = experience
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.health = health
        self.level = level
        self.attack_dmg = attack_dmg
        self.attack_type = attack_type
        self.__inventory = []
        self.head_item = ''
        self.shoulders_item = ''
        self.rhand_item = ''
        self.lhand_item = ''
        self.body_item = ''
        self.legs_item = ''
        self.char_class = char_class

    def __repr__(self):
        return f'{self.name}, {self.char_class}, level: {self.level}'

    def add_to_inventory(self, item: InventoryItem):
        self.__inventory.append(item)
        return f'{item} is added to the inventory '

    def equip_item(self, item: InventoryItem):
        if item in self.__inventory:
            if item.body_part == 'head':
                self.head_item = item
            elif item.body_part == 'shoulders':
                self.shoulders_item = item
            elif item.body_part == 'right hand':
                self.rhand_item = item
            elif item.body_part == 'left hand':
                self.lhand_item = item
            elif item.body_part == 'body':
                self.body_item = item
            elif item.body_part == 'legs':
                self.legs_item = item

    def take_off_item(self, body_part):
        if body_part == 'head':
            self.head_item = ''
        elif body_part == 'shoulders':
            self.shoulders_item = ''
        elif body_part == 'right hand':
            self.rhand_item = ''
        elif body_part == 'left hand':
            self.lhand_item = ''
        elif body_part == 'body':
            self.body_item = ''
        elif body_part == 'legs':
            self.legs_item = ''

    def attack(self, target):
        if self.attack_type == 'melee':
            target.health -= self.attack_dmg
        elif self.attack_type == 'ranged':
            target.health = (target.health - self.attack_dmg) + random.randint(0, 3)

    def defence(self):
        if self.attack_type == 'melee':
            self.health += 5
        elif self.attack_type == 'ranged':
            self.health += 4


class TheElementalMage(Character):
    def __init__(self, name):
        super().__init__(name, level=1, agility=4, strength=3, intelligence=8,
                         attack_type='ranged', attack_dmg=8, char_class='The Elemental Mage')




class TheStealthyRogue(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=3, agility=8, intelligence=4,
                         attack_type='melee', attack_dmg=12, char_class='The Stealthy Rogue')


class TheResilientWarrior(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=8, agility=4, intelligence=3,
                         attack_type='melee', attack_dmg=13, char_class='The Resilient Warrior')


class TheSkilledArcher(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=4, agility=9, intelligence=3,
                         attack_type='ranged', attack_dmg=10, char_class='The Skilled Archer')



class TheMysticalDruid(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=6, agility=6, intelligence=6,
                         attack_type='ranged', attack_dmg=8, char_class='The Mystical Druid')


a = TheElementalMage('Igor')
print(a)
b = TheResilientWarrior('Vasya')
b.level = 3
print(b)

cosmetics = InventoryItem('Straw Hat', 'head')
a.add_to_inventory(cosmetics)
a.equip_item(cosmetics)
print(a.head_item)
a.attack(b)
b.defence()
print(b.health)
