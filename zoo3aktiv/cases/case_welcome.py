import tkinter as tk
import sys
from databases.lists import *

def exit():
    abschiedsfenster = tk.Tk()
    tk.Label(abschiedsfenster, text="Schade, bis zum nächsten Mal.").pack()
    tk.Button(abschiedsfenster, text="Tschüss", command=sys.exit).pack()
    abschiedsfenster.mainloop()

def welcome():
    window = tk.Tk()
    tk.Label(window, text="Herzlich Willkommen lieber Zoobesucher, du befindest dich direkt vor dem Zoo").pack()
    tk.Button(window, text="weiter", command=window.destroy).pack()
    window.mainloop()

def opening_hours():
    # öffnet ein Tkinter-Fenster mit entsprechendem Text (tk.Label)
    window = tk.Tk()
    tk.Label(window, text=f"Bist du während der Öffnungszeiten am Zoo?\n\nÖffnungszeiten: {oeffnungszeiten[0]} bis {oeffnungszeiten[1]}\n").pack()
    # zwei Antwortbuttons (ja + nein) erstellen
    tk.Button(window, text="Ja", command=window.destroy).pack()
    tk.Button(window, text="Nein", command=lambda: [window.destroy(), exit()]).pack()
    # Tkinter-Fenster starten und auf Benutzereingaben warten.
    window.mainloop()

def enter_the_zoo():
    window = tk.Tk()
    tk.Label(window, text=f"Möchtest du den Zoo betreten?\n\nPreise:\n{eintrittspreise[0]}\n{eintrittspreise[1]}\n{eintrittspreise[2]}\n").pack()
    tk.Button(window, text="Ja", command=window.destroy).pack()
    tk.Button(window, text="Nein", command=lambda: [window.destroy(), exit()]).pack()
    window.mainloop()