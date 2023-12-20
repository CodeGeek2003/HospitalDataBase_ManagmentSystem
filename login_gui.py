from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_gui(open_patient_login,open_staff_login):
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
    canvas.create_image(
        489.0,
        176.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    canvas.create_image(
        463.0,
        173.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    canvas.create_image(
        465.0,
        236.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    staff_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_staff_login(window),
        relief="flat"
    )
    staff_btn.place(
        x=241.0,
        y=286.0,
        width=99.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    patient_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_patient_login(window),
        relief="flat"
    )
    patient_btn.place(
        x=589.0,
        y=286.0,
        width=99.0,
        height=31.0
    )
    window.resizable(False, False)
    window.mainloop()
