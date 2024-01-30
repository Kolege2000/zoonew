# use_case
anlaufstellen       =   {   1   :   ['am', 'Ein- und Ausgang', 'aus dem Zoo raus', (4,1), 'sounds/ausgang.mp3'],
                            2   :   ['am', 'Restaurant', 'in das Restaurant rein', (3,2), 'sounds/affe(restauramt).mp3'],
                            3   :   ['an der', 'Polarwelt', 'in die Polarwelt rein', (3,4),'sounds/penguin.wav'],
                            4   :   ['am', 'Savannengehege', 'in das Savannegehege rein', (5,4), 'sounds/elefant.mp3'],
                            5   :   ['an der', 'Unterwasserwelt', 'in die Unterwasserwelt ', (6,3), 'sounds/two adult alligators.mp3'],
                        }
# quiz
aussage =   [         # Polarwelt
                [   'Nils Olav der Dritte ist Generalmajor der königlichen Garde Norwegens',  # pinguin
                    'Das Tier hat 42 Zähne und kann Kadaver vermutlich aus über 30 km Entfernung wittern',  # eisbär
                    'Eine Gruppe dieser Tiere nennt sich Parlament',  # eule
                    'Diese Tiere leben in einem Matriarchat. Ihre Kommunikation weisen Dialekte auf',  # orca
                    'Verträgt Temperaturen bis zu 50 Grad Celsius unter Null',  # fuchs
                    'Der lateinische Name lautet Lepus timidus'  # schneehase
                ],      # Savannengehege
                [   'Timon (König der Löwen)',      # erdmännchen
                    'Pumba (König der Löwen)',      # warzenschwein
                    'Melman (Madagaskar)',          # giraffe
                    'Colonel Hathi (Djungelbuch)',  # elefant
                    'Otter',                        # otter
                    'Simba (König der Löwen)'       # löwe
                ],       # unterwasserwelt
                [   'In der Gruppe existier ein Weibchen. Stirbt das Weibchen, wechselt das größte Männchen das Geschlecht',  # clownfisch
                    'Das älteste bekannte Exemplar erreichte ein geschätzes Alter von über 500 Jahren',  # grönlandhai
                    'Das Geschlecht dieser Tiere wird durch die Temperaturen während der Brutzeit bestimmt',  # alligtor
                    'Hat drei Herzen',  # oktopus
                    'Das Männchen trägt den Nachwuchs aus',  # seepferdchen
                    'Quak'  # piranha
                ]
             ]

bild_pfade = [          # Polarwelt
                [   "inside_acting/polarwelt/hase.jpg",
                    "inside_acting/polarwelt/eisbär.png",
                    "inside_acting/polarwelt/polarfuchs.jpg",
                    "inside_acting/polarwelt/schneeeule.jpg",
                    "inside_acting/polarwelt/orca.jpg",
                    "inside_acting/polarwelt/koenigspinguin.jpg"
                ],      # Savannengehege
                [   "inside_acting/savanne/simba.jpg",
                    "inside_acting/savanne/giraffe.jpg",
                    "inside_acting/savanne/hiding_meerkat.jpg",
                    "inside_acting/savanne/hiding_otter.jpg",
                    "inside_acting/savanne/elefant.png",
                    "inside_acting/savanne/Pumba.png"
                ],      # unterwasserwelt
                [   "inside_acting/unterwasserwelt/oktopus.png",
                    "inside_acting/unterwasserwelt/grönlandhai.png",
                    "inside_acting/unterwasserwelt/clownfisch.png",
                    "inside_acting/unterwasserwelt/aligator.png",
                    "inside_acting/unterwasserwelt/seepferdchen.png",
                    "inside_acting/unterwasserwelt/piranha.png"
                ]
             ]

bild_idx_reihenfolge = [[5, 1, 3, 4, 2, 0], # Polarwelt
                        [2, 5, 1, 4, 3, 0], # Savannengehege
                        [2, 1, 3, 0, 4, 5]] # unterwasserwelt

# immutable, globale Variable (Tuple)
oeffnungszeiten = ("09:00", "19:00")

eintrittspreise = ("Kinder bis 3 Jahre : Freier Eintritt",
                   "Kinder bis 15 Jahre : 15€",
                   "Erwachsene : 20€")