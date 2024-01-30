import tkinter as tk
import sys
from classes.class_GuV_quelle import Einnahme_und_Kostenquelle
from databases.lists import *
from sounds.play_sound import playing_sound
from inside_acting.ausgang.exit import get_out
from inside_acting.ia_quiz import *
from inside_acting.restaurant.ia_restaurant import *
from abc import abstractmethod

class Lebewesen:
    def __init__(self, name, position):
        self.name           =   name
        self.position       =   position

    @abstractmethod
    def go_to(self):
        return input('du drehst dich im Kreis, gib eine Ganzzahl zwischen 1 und 5 ein:')
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
    def exit(self):
        self.window = tk.Tk()
        self.window.geometry('450x120')
        self.window.geometry(f'+{550}+{300}')
        tk.Label(self.window, text="Schade, bis zum nächsten Mal.").pack(pady=10)
        tk.Button(self.window, width= '12', text="Tschüss", command=sys.exit).pack(pady=10)
        self.window.mainloop()
    def welcome(self):
        self.window = tk.Tk()
        self.window.title('Willkommen')
        self.window.geometry('450x120')
        self.window.geometry(f'+{550}+{300}')
        tk.Label(self.window, text="Herzlich Willkommen lieber Zoobesucher, du befindest dich direkt vor dem Zoo").pack(pady=10)
        tk.Button(self.window, width= '12', text="weiter", command=lambda : [self.window.destroy(), self.opening_hours()]).pack(pady=10)
        self.window.mainloop()
    def opening_hours(self):
        # öffnet ein Tkinter-Fenster mit entsprechendem Text (tk.Label)
        self.window = tk.Tk()
        self.window.title('Öffnungzeiten')
        self.window.geometry('450x120')
        self.window.geometry(f'+{550}+{300}')
        tk.Label(self.window, text=f"Bist du während der Öffnungszeiten am Zoo?\n\nÖffnungszeiten: {oeffnungszeiten[0]} bis {oeffnungszeiten[1]}\n").pack()
        # zwei Antwortbuttons (ja + nein) erstellen
        tk.Button(self.window, width= '12', text="Ja", command=lambda: [self.window.destroy(), self.enter_the_zoo()]).pack(pady=1)
        tk.Button(self.window, width= '12', text="Nein", command=lambda: [self.window.destroy(), self.exit()]).pack(pady=1)
        # Tkinter-Fenster starten und auf Benutzereingaben warten.
        self.window.mainloop()
    def enter_the_zoo(self):
        self.window = tk.Tk()
        self.window.title('Zooeingang')
        self.window.geometry('450x170')
        self.window.geometry(f'+{550}+{300}')
        tk.Label(self.window,  text=f"Möchtest du den Zoo betreten?\n\nPreise:\n{eintrittspreise[0]}\n{eintrittspreise[1]}\n{eintrittspreise[2]}\n").pack()
        tk.Button(self.window, width= '12', text="Ja", command=lambda: [self.window.destroy(), self.paying_ticket()]).pack(pady=1)
        tk.Button(self.window, width= '12', text="Nein", command=lambda: [self.window.destroy(), self.exit()]).pack(pady=1)
        self.window.mainloop()
    def paying_ticket(self):
        self.money -= 20
        print(f'Du hast noch {self.money} übrig')
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