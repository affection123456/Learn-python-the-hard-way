# Cross Srike
# Engine
#    select
# StartScreen 
#    select_map
#    select_player
#        Terrorist--Kill all the Counter Terrorist 
#        Counter Terrorist--Place a C4 bomb in the T's home and let it bomb successfully
#    select_weapon
# Map
#    -select
#    Transport Ship
#    Desert
#    Nuclear Power Plant
# Weapon
#    -select
#    guns 
#    equipments
# Finish
#    -success or defeat
import random

class Engine(object):

    def __init__(self, start_screen):
        self.start_screen = start_screen

    def start(self):
        self.start_screen.select_map()
        self.start_screen.select_player()
        self.start_screen.select_weapon()

        act = raw_input(">>fight?y/n\n")
        if act == 'y':
            self.start_screen.success()
        else:
            self.start_screen.defeat()

	
class Finish(object):

    def success(self):
        print "Well done!"
        exit(0)

    def defeat(self):
        print "Defeat!"
        exit(0)


class Weapon(object):

    guns = {
        1: "pistol",
        2: "shotgun",
        3: "rifle",
        4: "sniper_rifle",
        5: "submachine_gun",
    }

    equipments = {
        1: "smoke_bomb",
        2: "ordinary_bomb",
        3: "bulletproof_vest",
        4: "helmet",
        5: "bullet",
    }

    def __init__(self, number_1, number_2):
        self.number_1, self.number_2 = number_1, number_2
	
    def select(self):
        gun = self.guns.get(self.number_1)
        equipment = self.equipments.get(self.number_2)
        return gun, equipment
	
class Map(object):

    def select(self):
        print "Loading------"
		

class TransportShip(Map):

    def select(self):
        print "Wellcome to the transport ship"


class Desert(Map):

    def select(self):
        print "Wellcome to the desert"
		
		
class NuclearPowerPlant(Map):

    def select(self):
        print "Wellcome to the nuclear power plant"

		
class StartScreen(Finish):

    maps = {
        "transport_ship": TransportShip(),
        "desert": Desert(),
        "nuclear_power_plant": NuclearPowerPlant(),
    }

    def select_map(self):
        return self.maps.get(random.choice(("transport_ship","desert","nuclear_power_plant")))

    def select_player(self):
        pick = raw_input(">>CT or T \n")
        if pick == 'CT':
            print "Place a C4 bomb in the T's home and let it bomb successfully."
        elif pick == 'T':
            print "Kill all the Counter Terrorist."
        else:
            print "Select again!"
            self.start_screen.select_player()
		
    def select_weapon(self):
        number_1, number_2 = random.randint(1,5), random.randint(1,5)
        buying = Weapon(number_1, number_2)
        your_gun, your_equipment = buying.select()
        print "Complete your mission with your",your_gun,your_equipment


starting = StartScreen()
a_game = Engine(starting)
a_game.start()