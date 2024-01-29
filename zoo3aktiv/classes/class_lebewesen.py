from classes.class_GuV_quelle import Einnahme_und_Kostenquelle
from databases.lists import anlaufstellen
from sounds.play_sound import playing_sound
from inside_acting.ausgang.exit import get_out
from inside_acting.ia_quiz import *
from inside_acting.restaurant.ia_restaurant import *

class Lebewesen:
    def __init__(self, name, position):
        self.name           =   name
        self.position       =   position
#-----------------------------------------------------
class Mensch(Lebewesen):
    def __init__(self, name, position):
        Lebewesen.__init__(self, name, position)

class Tier(Lebewesen):
    def __init__(self, name, position):
        Lebewesen.__init__(self, name, position)
#-----------------------------------------------------
class Zooangestellter(Einnahme_und_Kostenquelle, Mensch):
    def __init__(self, income, expenditure, name, position):
        Einnahme_und_Kostenquelle.__init__(self, income, expenditure)
        Mensch.__init__(self, name, position)

class Besucher(Einnahme_und_Kostenquelle, Mensch):
    def __init__(self, income, expenditure, name, position, money):
        Einnahme_und_Kostenquelle.__init__(self, income, expenditure)
        Mensch.__init__(self, name, position)
        self.money              =   money
        self.points             =   0
        self.already_been_there =   []

    def go_to(self):
        options = '\n'.join([f'{key}: {value[1]}' if key != self.position else f'{key}: {value[2]}' for key, value in anlaufstellen.items()])
        position_nr = input(f'du stehst {anlaufstellen[self.position][0]} {anlaufstellen[self.position][1]}. Wo willst du hingehen?\n{options}\n')
        return position_nr

    def inside_acting(self):
        playing_sound(self)

        if self.position in self.already_been_there and self.position != 2:
            print('da warst du schon\n')
        else:
            if self.position    ==  1:
                print(f'du hast {self.points} von 18 möglichen Punkten erreicht!')
                get_out()
            elif self.position  ==  2:
                run_order(self)
            else:
                points = run_quiz(self.position)
                self.points += points
            self.already_been_there.append(self.position)