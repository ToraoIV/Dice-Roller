import customtkinter as ctk
from PIL import Image
import random
import pygame

window = ctk.CTk()
ctk.set_appearance_mode("light")
window.geometry("400x250")
window.title("Dice Roller")
window.resizable(False, False)

dice1 = ctk.CTkImage(Image.open("dice/dice-1.png"), size=(100, 100))
dice2 = ctk.CTkImage(Image.open("dice/dice-2.png"), size=(100, 100))
dice3 = ctk.CTkImage(Image.open("dice/dice-3.png"), size=(100, 100))
dice4 = ctk.CTkImage(Image.open("dice/dice-4.png"), size=(100, 100))
dice5 = ctk.CTkImage(Image.open("dice/dice-5.png"), size=(100, 100))
dice6 = ctk.CTkImage(Image.open("dice/dice-6.png"), size=(100, 100))

dices = {1: dice1, 2: dice2, 3: dice3, 4: dice4, 5: dice5, 6: dice6}


label1 = ctk.CTkLabel(window, text="", image=dice1)
label1.place(relx=0.3, rely=0.4, anchor="center")

label2 = ctk.CTkLabel(window, text="", image=dice1)
label2.place(relx=0.7, rely=0.4, anchor="center")

pygame.mixer.init()


def roll():
    ran_1 = random.randint(1, 6)
    ran_2 = random.randint(1, 6)
    label1.configure(image=dices[ran_1])
    label2.configure(image=dices[ran_2])
    pygame.mixer.music.load("dice_sound.mp3")
    pygame.mixer.music.play()


button = ctk.CTkButton(window, text="Roll", command=roll)
button.place(relx=0.5, rely=0.85, anchor="center")


window.mainloop()
