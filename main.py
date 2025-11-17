import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 40, "bold")

def get_foreign_word_dict():
    # TODO: stretch - use irish words instead and/or allow user to choose/toggle language
    foreign_word_df = pandas.read_csv("./data/french_words.csv")
    foreign_word_dict = foreign_word_df.to_dict(orient="records")

    return foreign_word_dict

def display_new_word():
    # TODO: stretch - handle special characters
    canvas_card.itemconfig(canvas_foreign_word, text=get_random_foreign_word())

def get_random_foreign_word():
    global foreign_word_dict
    return random.choice(foreign_word_dict)["French"]

foreign_word_dict = get_foreign_word_dict()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Teanga")
window.minsize(height=410, width=500)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# TODO: stretch - resize images to fit inside canvas, make shadow visible
# Alternatively, use tkinter to manually create shadow, rounded corners on canvas
CARD_FRONT_IMG = PhotoImage(file="./images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="./images/card_back.png")
canvas_card = Canvas(width=400, height=200)
canvas_card.create_image(250, 250, image=CARD_FRONT_IMG)
canvas_card.create_text(200, 50, text="French", font=LANGUAGE_FONT)
canvas_foreign_word = canvas_card.create_text(200, 125, text=random.choice(foreign_word_dict)["French"], font=WORD_FONT)
canvas_card.grid(column=1, row=1, columnspan=2, pady=(0, 50))

CORRECT_IMG = PhotoImage(file="./images/right.png")
button_correct = Button(image=CORRECT_IMG, command=display_new_word, highlightthickness=0, height=60, width=60)
button_correct.grid(column=1, row=2)

INCORRECT_IMG = PhotoImage(file="./images/wrong.png")
button_incorrect = Button(image=INCORRECT_IMG, command=display_new_word, highlightthickness=0, height=60, width=60)
button_incorrect.grid(column=2, row=2)

window.mainloop()