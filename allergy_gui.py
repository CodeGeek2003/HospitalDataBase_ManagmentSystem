from pathlib import Path
import functions
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/ahmedmohamed/GUIs/Patient_medical_history/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def allergy_gui():
    window = Tk()

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
        850.0,
        498.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        845.0,
        407.0,
        image=image_image_3
    )

    area=canvas.create_rectangle(
        778.9999677625146,
        345.0,
        1099.999755859375,
        348.0633326052027,
        fill="#202854",
        outline="")

    canvas.create_text(
        842.0,
        292.0,
        anchor="nw",
        text="Patients Name",
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
        452.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        819.0,
        538.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        865.0,
        579.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        819.0,
        619.0,
        image=image_image_7
    )

    canvas.create_text(
        842.0,
        445.0,
        anchor="nw",
        text="Data of Birth Goes Here",
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        838.0,
        610.0,
        anchor="nw",
        text="Medical History ID Goes Here",
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        838.0,
        530.0,
        anchor="nw",
        text="Room Number Goes Here",
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    logout_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.logout_func(window),
        relief="flat"
    )
    logout_btn.place(
        x=1.0,
        y=471.0,
        width=45.0,
        height=31.0
    )
    canvas.create_rectangle(
        76.0,
        221.0,
        751.0,
        743.0,
        fill="#2F396B",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    medhis_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    medhis_btn.place(
        x=4.0,
        y=404.0,
        width=38.0,
        height=41.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    home_btn = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: functions.open_patient_gui(window),
        relief="flat"
    )
    home_btn.place(
        x=3.0,
        y=341.0,
        width=41.0,
        height=41.0
    )
    window.resizable(False, False)
    window.mainloop()
