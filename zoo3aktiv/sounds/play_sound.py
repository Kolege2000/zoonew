from databases.lists import anlaufstellen
import pygame

def playing_sound(anna):
    pygame.init()
    pygame.mixer.init()

    mp3_file_path = anlaufstellen[anna.position][4]
    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

    pygame.quit()