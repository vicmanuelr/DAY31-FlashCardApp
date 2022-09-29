from tkinter import *
import pandas as pd
import random as rn

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("noto-cjk", 80, "bold")
IDLE = 3000

# ---------------------------- DATA/PANDAS ------------------------------- #
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/Japanese Words - Alphabet.csv")
finally:
    to_learn = data.to_dict(orient="records")
    language_to_learn = data.columns[0]
    translation = data.columns[1]
    current_card = {}


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rn.choice(to_learn)
    canvas.itemconfigure(card_background, image=front_img)
    canvas.itemconfigure(card_title, text=language_to_learn, fill="black")
    canvas.itemconfigure(card_word, text=current_card[language_to_learn], fill="black")
    flip_timer = window.after(IDLE, func=flip_card)


def flip_card():
    word_learning = current_card[language_to_learn] + "\n" + current_card[translation]
    canvas.itemconfigure(card_title, text=translation, fill="white")
    canvas.itemconfigure(card_word, text=word_learning, fill="white")
    canvas.itemconfigure(card_background, image=back_img)


# ---------------------------- UI SETUP ------------------------------- #

# Window related
window = Tk()
window.title("FlashCardApp")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, )
flip_timer = window.after(IDLE, func=flip_card)

# Card canvas
back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 125, text="Title", justify="center", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="Word", justify="center", font=WORD_FONT)
# spelling_text = canvas.create_text(400, 150, text="Title", justify="center")

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=new_card)
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

# Start with a new card generated randomly
new_card()

window.mainloop()
