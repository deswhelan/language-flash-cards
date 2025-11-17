import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 40, "bold")

def get_translations_list():
    # TODO: stretch - use irish words instead and/or allow user to choose/toggle language
    translations_df = pandas.read_csv("./data/french_words.csv")
    translations_list = translations_df.to_dict(orient="records")

    return translations_list

def display_new_word():
    global current_translation
    # TODO: stretch - handle special characters
    update_current_translation()
    display_current_word()

def display_current_word():
    canvas_card.itemconfig(text_current_word, text=current_translation[current_language])

def update_current_translation():
    global translations_list, current_translation
    current_translation = random.choice(translations_list)

def flip_card():
    global current_language

    if current_language == "English":
        update_current_translation()
        display_current_word()
        current_language = "French"
        card_img = CARD_FRONT_IMG
        text_colour = "black"
    else:
        current_language = "English"
        card_img = CARD_BACK_IMG
        text_colour = "white"

    canvas_card.itemconfig(image_card, image=card_img)
    canvas_card.itemconfig(text_current_language, text=current_language, fill=text_colour)
    display_current_word()
    canvas_card.itemconfig(text_current_word, fill=text_colour)

    window.after(3000, flip_card)

# TODO: stretch - implement using itertools
# def toggle_language():

translations_list = get_translations_list()
current_translation = random.choice(translations_list)
current_language = "French"

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
image_card = canvas_card.create_image(250, 250, image=CARD_FRONT_IMG)
text_current_language = canvas_card.create_text(200, 50, text=current_language, font=LANGUAGE_FONT)
text_current_word = canvas_card.create_text(200, 125, text=current_translation[current_language], font=WORD_FONT)
canvas_card.grid(column=1, row=1, columnspan=2, pady=(0, 50))

CORRECT_IMG = PhotoImage(file="./images/right.png")
button_correct = Button(image=CORRECT_IMG, command=display_current_word, highlightthickness=0, height=60, width=60)
button_correct.grid(column=1, row=2)

INCORRECT_IMG = PhotoImage(file="./images/wrong.png")
button_incorrect = Button(image=INCORRECT_IMG, command=flip_card, highlightthickness=0, height=60, width=60)
button_incorrect.grid(column=2, row=2)

window.after(3000, flip_card)

window.mainloop()
