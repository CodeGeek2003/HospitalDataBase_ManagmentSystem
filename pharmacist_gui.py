from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions as fn
import globals

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/Pharmacist_Main")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_pharmacist_gui():
    window = Tk()
    fn.get_pharmacist_info()
    window.geometry("1109x794")
    window.configure(bg = "#343E71")


    canvas = Canvas(
        window,
        bg = "#343E71",
        height = 794,
        width = 1109,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        554.0,
        397.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        869.0,
        585.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        845.0,
        490.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        778.9999677625146,
        345.0,
        1099.999755859375,
        348.0633326052027,
        fill="#202854",
        outline="")

    ph_name=canvas.create_text(
        812.0,
        292.0,
        anchor="nw",
        text=globals.u_name,
        fill="#FFFFFF",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        413.0,
        6.0,
        anchor="nw",
        text="Nada’s Memorial Hospital",
        fill="#FFFFFF",
        font=("Inter", 28 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        818.0,
        535.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        819.0,
        625.0,
        image=image_image_5
    )

    ph_dob=canvas.create_text(
        842.0,
        528.0,
        anchor="nw",
        text=globals.u_dob,
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    ph_license=canvas.create_text(
        838.0,
        617.0,
        anchor="nw",
        text=globals.ph_license,
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    logout_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.logout_func(window),
        relief="flat"
    )
    logout_btn.place(
        x=3.0,
        y=465.0,
        width=45.0,
        height=31.0
    )

    canvas.create_rectangle(
        76.0,
        220.0,
        751.0,
        742.0,
        fill="#2F396B",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    addMed_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_medicine_gui(),
        relief="flat"
    )
    addMed_btn.place(
        x=133.0,
        y=480.0,
        width=160.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    sellMed_btn = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:fn.sell_medicine_gui(),
        relief="flat"
    )
    sellMed_btn.place(
        x=518.0,
        y=470.0,
        width=160.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    home_btn = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    home_btn.place(
        x=3.0,
        y=360.0,
        width=41.0,
        height=41.0
    )
    window.resizable(False, False)
    window.mainloop()
#TODO: Add the code to display the labels of the pharmacist