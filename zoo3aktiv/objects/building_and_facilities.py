from classes.class_anlage import *
from objects.being import polar_animals, savanna_animals, unterwasser_animals, employees

def create_builing():
    kassenbude      =   Kassenbude  (employees[0], 1,    0, employees[0].expenditure, {'normal' :   20, 'ermäßigt'  :   15})
    restaurant      =   Restaurant  (employees[1], 2,    0, employees[1].expenditure, {'Hauptgericht' : 10, 'Nachtisch' : 6, 'Getränk' : 5})
    buero           =   Buero       (employees[3], None, 0, employees[3].expenditure, 1800)
    return kassenbude, restaurant, buero

def create_facilities():
    polarwelt       =   Polarwelt (polar_animals, 3)
    savannengehege  =   Savannengehege (savanna_animals, 4)
    unterwasserwelt =   Unterwasserwelt (unterwasser_animals, 5)
    return polarwelt, savannengehege, unterwasserwelt

building    =   create_builing()
facilities  =   create_facilities()