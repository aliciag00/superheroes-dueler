import random
from ability import Ability
from armor import Armor
from weapon import Weapon



class Hero:

    def __init__(self, name, starting_health=100):
       
       self.abilities = list()
       self.armors = list()
       self.name = name
       self.starting_health = starting_health
       self.current_health = starting_health
       self.deaths = 0
       self.kills = 0

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

  # start our total out at 0
        total_damage = 0
    # loop through all of our hero's abilities
        for ability in self.abilities:
      # add the damage of each attack to our running total
            total_damage += ability.attack()
    # return the total damage
        return total_damage
    
    def armor(self, armor):
        ''' Add armor to self.armors
            Armor: Armor Object
        '''
        self.add_armor(armor) 

    def defend(self):
        ''' Calculate the total block amouunt from all armor blocks. 
            return: total_block:Int
        '''
        
        total_block = 0
        for armor in self.armors:

            total_block += armor.block()

        return total_block
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        defense = self.defend()
        damage -= defense
        self.current_health -= damage

    def is_alive(self):
        ''' Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0
    
    def fight(self,opponent):
        
        if not (self.abilities) or not opponent.abilities:
            print("Draw!")
            return

        while self.is_alive() and opponent.is_alive:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive():
            print(f"{self.name} won!")
            self.add_kill()
            opponent.add_death()

        else:
            print(f"{opponent.name} won!")
            self.add_death()
            opponent.add_kill()
       
    def add_ability(self, ability):

        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount.
        '''
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths.
        '''
        self.deaths += num_deaths


    
        

if __name__ == "__main__":

    
   hero = Hero("Chewy Bacca")
   weapon = Weapon("Spear", 90)
   hero.add_weapon(weapon)
   print(hero.attack())
   

    

    