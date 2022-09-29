from tkinter import *
import pandas as pd
import random as rn

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("noto-cjk", 80, "bold")

# ---------------------------- DATA/PANDAS ------------------------------- #
data = pd.read_csv("./data/Japanese Words - Alphabet.csv")
data_pairs = data.to_dict(orient="records")
title_text = data.columns[0]


def new_card():
    random_index = rn.randint(0, len(data_pairs)-1)
    canvas.itemconfigure(word_text, text=data_pairs[random_index][title_text])


# ---------------------------- UI SETUP ------------------------------- #
# Window related
window = Tk()
window.title("FlashCardApp")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, )

# Card canvas
card_front = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)
canvas.create_image(400, 263, image=card_front)
language_title = canvas.create_text(400, 150, text=title_text, justify="center", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Word", justify="center", font=WORD_FONT)
# spelling_text = canvas.create_text(400, 150, text="Title", justify="center")

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=new_card)
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
