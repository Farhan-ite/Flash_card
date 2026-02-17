from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

#Global variables
current_card={}
to_learn = {}

#Reading CSV
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict("records")


def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "White")
    canvas.itemconfig(card_word, text =current_card["English"], fill= "White")
    canvas.itemconfig(card_background, image=card_back)

window= Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer =window.after(3000, func = flip_card)


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill= "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill= "black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func = flip_card)


#removing known cards

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#functions

card_front = PhotoImage(file="images/card_front.png")
#images
card_back = PhotoImage(file="images/card_back.png")
check_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")

#Canvas

canvas = Canvas(width=800,height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400,150, text="Title", font=("Arial", 40, "italic"))
card_word= canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

#buttons
check_btn = Button(image=check_image, highlightthickness=0, command= is_known)
check_btn.grid(row=2, column=0)
cross_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_btn.grid(row=2, column=1)

next_card()

window.mainloop()