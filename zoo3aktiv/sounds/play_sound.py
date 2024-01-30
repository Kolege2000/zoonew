from databases.lists import anlaufstellen
import pygame

def playing_sound(anna):
    pygame.init()
    pygame.mixer.init()

    mp3_file_path = anlaufstellen[anna.position][4]
    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play()

    pygame.time.delay(int(2 * 1000))

    pygame.quit()

