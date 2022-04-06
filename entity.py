from utils import *

class Entity():
    pass


races = {
    'human': {
        'name': 'Human',
        'attributes': [0, 0, 0, 0, 0, 0],
        'features': 0
    },
    'elf': {
        'name': 'Elf',
        'attributes': [0, 2, 0, 0, 1, 0],
        'features': 0
    }
}

classes = {
    'fighter': {
        'name': 'Fighter',
        'features': 0
    },
    'wizard': {
        'name': 'Wizard',
        'features': 0
    }
}


# CLASSES FOR ENTITIES
class NPC(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.character_name = ""
        self.description = ""
        self.character_class = [""]
        self.character_level = [0]
        self.character_experience = 0
        self.character_alignment = "TN"
        self.character_race = [""]
        self.character_gender = ""
        self.combat_actions = ["MOVE","INTERACT","EVADE","ASSIST"]
        # TODO - POSSIBLY add taunt in the future

        self.character_attributes = {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 10,
            "WIS": 10,
            "CHA": 10
        }
        self.character_totalHP = 10
        self.character_currentHP = 10

        self.character_skills = {
            "athletics": 0,
            "acrobatics": 0,
            "endurance": 0,
            "knowledge": 0,
            "nature": 0,
            "social": 0
        }

        self.character_gear = {
            "ATTR": [],
            "SKILL": [],
            "ARMOR": [],
            "TRINKET": [],
            "COMBAT": []
        }

    def getAttributeModifier(self, attribute):
        return (self.character_attributes[attribute] - 10) // 2

    def getArmorClass(self):
        modifiers = 0
        for armor in self.character_gear["ARMOR"]:
            modifiers += armor.gear_modifier
        for trinket in self.character_gear["TRINKET"]:
            if trinket.gear_subType == "AC":
                modifiers += trinket.gear_modifier
        return 8 + self.getAttributeModifier('DEX') + modifiers

    def getInitiative(self):
        modifiers = 0
        # TODO = update according to the current character_gear dictionary labels; "trinkets"
        for trinket in self.character_gear["TRINKET"]:
            if trinket.gear_subType == "initiative":
                modifiers += trinket.gear_modifier
        return modifiers + rollSum(1, 20)

    def change_attribute(self, attribute, value):
        self.character_attributes[attribute] += value

    def change_skill(self, skill, value):
        self.character_skills[skill] += value

    def change_HP(self, value):
        self.character_currentHP += value

    def change_XP(self, value):
        self.character_experience += value


class Player(NPC):
    def __init__(self):
        NPC.__init__(self)


        #TODO - add a way to provide combat actions with gear
class Gear(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.description = ""
        self.actions = []
        self.value = 0
        self.gear_modifier = 0
        self.gear_type = ""
        self.gear_sub_type = ""
        
class Weapon(Gear):
    def __init__(self):
        super().__init__()
        self.damage = ""
        self.actions.append('ATTACK')

# subtypes: AC, initiative
