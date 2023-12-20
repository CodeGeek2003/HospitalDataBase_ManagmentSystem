from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions as fn
import globals as gl
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/Doctor_Main")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_doctor_gui():
    window = Tk()
    fn.get_doctor_info_and_patient_count()
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

    canvas.create_rectangle(
        778.9999677625146,
        345.0,
        1099.999755859375,
        348.0633326052027,
        fill="#202854",
        outline="")

    d_name=canvas.create_text(
        842.0,
        292.0,
        anchor="nw",
        text=gl.u_name,
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

    d_dob=canvas.create_text(
        842.0,
        445.0,
        anchor="nw",
        text=gl.u_dob,
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    d_pager=canvas.create_text(
        838.0,
        610.0,
        anchor="nw",
        text=gl.d_pager,
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    d_patient=canvas.create_text(
        838.0,
        530.0,
        anchor="nw",
        text=gl.d_p_count,
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    logout_btn = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:  fn.logout_func(window),
        relief="flat"
    )
    logout_btn.place(
        x=2.0,
        y=471.0,
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
    w_medhis_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_medical_history(),
        relief="flat"
    )
    w_medhis_btn.place(
        x=518.0,
        y=627.0,
        width=160.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    nurse_btn = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_helping_nurses_for_doctor(),
        relief="flat"
    )
    nurse_btn.place(
        x=133.0,
        y=307.0,
        width=160.0,
        height=44.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    medhis_btn = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_written_medical_histories(),
        relief="flat"
    )
    medhis_btn.place(
        x=518.0,
        y=312.0,
        width=160.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    v_tools_btn = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_utilized_tools_for_doctor(),
        relief="flat"
    )
    v_tools_btn.place(
        x=133.0,
        y=633.0,
        width=160.0,
        height=44.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    tools_btn = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.modify_resource_quantity(),
        relief="flat"
    )
    tools_btn.place(
        x=133.0,
        y=470.0,
        width=160.0,
        height=44.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    patient_btn = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    patient_btn.place(
        x=518.0,
        y=470.0,
        width=160.0,
        height=44.0
    )
    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    home_btn = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
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
#TODO: Add the code to display the labels of the doctor