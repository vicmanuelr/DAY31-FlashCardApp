from tkinter import *
import pandas as pd

# ---------------------------- DATA/PANDAS ------------------------------- #
data = pd.read_csv("./data/Japanese Words - Alphabet.csv")

def new_card():
    pass

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

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
language_title = canvas.create_text(400, 150, text="Language", justify="center")
word_text = canvas.create_text(400, 263, text="Word", justify="center")
# spelling_text = canvas.create_text(400, 150, text="Title", justify="center")

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
