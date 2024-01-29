import tkinter as tk
from PIL import Image, ImageTk
from databases.lists import *

class Quiz:
    def __init__(self, root, anna_pos):
        self.root       = root
        self.position   = anna_pos - 3
        self.root.title (anlaufstellen[anna_pos][1])
        self.geometrie  = root.geometry('830x850')
        self.resizable  = root.resizable(height=False, width=True)
        self.points     = 0
        self.buttons    = []

        global aussage
        global aussage_idx
        global bild_idx_reihenfolge
        aussage_idx = 0

        for i, bild_pfad in enumerate(bild_pfade[self.position]):
            pil_image = Image.open(bild_pfad).resize((250, 300))
            image = ImageTk.PhotoImage(pil_image)
            button = tk.Button(self.root, image=image, width=250, height=300, command=lambda idx=i: self.button_click(idx))
            button.image = image
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self.buttons.append(button)

        self.label1 = tk.Label(self.root, text='Ordne richtig zu:', font=("Helvetica", 16))
        self.label1.grid(columnspan=3, pady=10)

        self.label2 = tk.Label(self.root, text=aussage[self.position][0], font=("Helvetica", 16))
        self.label2.grid(columnspan=3, pady=10)

        self.exit_button = tk.Button(self.root, text= 'raus hier', state='disable', command= root.destroy)
        self.exit_button.grid(columnspan=3, pady=10)

    def button_click(self, idx):
        global aussage_idx
        global bild_idx_reihenfolge

        if idx == bild_idx_reihenfolge[self.position][aussage_idx]:
            self.buttons[idx].configure(bg="green", state='disabled')
            self.points += 1
        else:
            self.buttons[bild_idx_reihenfolge[self.position][aussage_idx]].configure(bg="red", state='disabled')

        aussage_idx += 1

        if aussage_idx <= 5:
            self.label2.configure(text=aussage[self.position][aussage_idx])
        else:
            self.exit_button.configure(state='normal')

def run_quiz(anna_pos):
    root = tk.Tk()
    run  = Quiz(root, anna_pos)
    root.mainloop()
    return run.points