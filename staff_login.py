from pathlib import Path
from globals import *
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def staff_login(check_user_username):
    window = Tk()

    window.geometry("978x353")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 353,
        width = 978,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        489.0,
        176.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        128.0,
        246.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        601.0,
        246.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        463.0,
        173.0,
        image=image_image_4
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        308.0,
        246.5,
        image=entry_image_1
    )
    username_entry = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username_entry.place(
        x=215.0,
        y=238.0,
        width=186.0,
        height=15.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        783.0,
        246.5,
        image=entry_image_2
    )
    password_entry = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*"  # This line makes the entered text appear as asterisks for password entry
    )
    password_entry.place(
        x=695.0,
        y=238.0,
        width=176.0,
        height=15.0
    )

    submit_btn_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    submit_btn = Button(
        image=submit_btn_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: check_user_username(username_entry.get("1.0", "end-1c"), password_entry.get(),window),
        relief="flat"
    )
    submit_btn.place(
        x=401.0,
        y=292.0,
        width=132.0,
        height=31.0
    )
    window.resizable(False, False)
    window.mainloop()
