from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import functions
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def patient_login(check_patient_ssn):
    window = Tk()
    window.title("Patient Login")
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

    ssntext=canvas.create_text(
        271.0,
        235.0,
        anchor="nw",
        text="Enter Your SSN",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        463.0,
        173.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        495.0,
        243.5,
        image=entry_image_1
    )
    ssn_text = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    ssn_text.place(
        x=391.0,
        y=235.0,
        width=208.0,
        height=15.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    submit_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: check_patient_ssn(ssn_text.get("1.0", "end-1c"),window)
        ,
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
