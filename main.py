from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 40, "bold")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Teanga")
window.minsize(height=410, width=500)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

CARD_FRONT_IMG = PhotoImage(file="./images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="./images/card_back.png")
canvas_card = Canvas(width=400, height=200)
canvas_card.create_image(250, 250, image=CARD_FRONT_IMG)
canvas_card.create_text(200, 50, text="Irish", font=LANGUAGE_FONT)
canvas_card.create_text(200, 125, text="foireann", font=WORD_FONT)
canvas_card.grid(column=1, row=1, columnspan=2, pady=(0, 50))

CORRECT_IMG = PhotoImage(file="./images/right.png")
button_correct = Button(image=CORRECT_IMG, highlightthickness=0, height=60, width=60)
button_correct.grid(column=1, row=2)

INCORRECT_IMG = PhotoImage(file="./images/wrong.png")
button_incorrect = Button(image=INCORRECT_IMG, highlightthickness=0, height=60, width=60)
button_incorrect.grid(column=2, row=2)

window.mainloop()