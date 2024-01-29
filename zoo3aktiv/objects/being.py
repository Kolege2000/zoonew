from classes.class_lebewesen import Besucher, Tier, Zooangestellter

def create_visitor():
    anna = Besucher(0, 0, 'Anna', 1, 50)
    return anna

def create_polar_animals():
    schneehase      =   Tier ('Klopfer', 3)
    eisbaer         =   Tier ('Knut', 3)
    polarfuchs      =   Tier ('Andrea', 3)
    schneeeule      =   Tier ('Hedwig', 3)
    orca            =   Tier ('Willi', 3)
    pinguin         =   Tier ('Nils Olav der Dritte', 3)
    return schneehase, eisbaer, polarfuchs, schneeeule, orca, pinguin

def create_savanna_animals():
    loewe           =   Tier ('Simba', 4)
    giraffe         =   Tier ('Melman', 4)
    erdmaennchen    =   Tier ('Timon', 4)
    otter           =   Tier ('Otti', 4)
    elefant         =   Tier ('Colonel Hathi', 4)
    warzenschwein   =   Tier ('Pumba', 4)
    return loewe, giraffe, erdmaennchen, otter, elefant, warzenschwein

def create_unterwasserwelt_animals():
    groenlandhai    =   Tier ('Oleg', 5)
    piranha         =   Tier ('Selin', 5)
    oktopus         =   Tier ('Marcel', 5)
    alligator       =   Tier ('Ali', 5)
    seepferdchen    =   Tier ('Robert', 5)
    clownfische     =   Tier ('Nemo', 5)
    return groenlandhai, piranha, oktopus, alligator, seepferdchen, clownfische

def create_employees():
    kassierer       =   Zooangestellter (0, 70,  'Dennis'   , 1)
    koch            =   Zooangestellter (0, 80,  'Mahmi'    , 2)
    tierwaerter     =   Zooangestellter (0, 100, 'Heidi'    , None)
    buchhalter      =   Zooangestellter (0, 120, 'Edeltraut', None)
    return kassierer, koch, tierwaerter, buchhalter

polar_animals       =   create_polar_animals()
savanna_animals     =   create_savanna_animals()
unterwasser_animals =   create_unterwasserwelt_animals()
employees           =   create_employees()