from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import functions as fn
import globals as gl
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/SystemAdmin_ii_gui")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_sys_2_gui():
    window = Tk()
    fn.get_system_admin_info()
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

    s_name=canvas.create_text(
        802.0,
        291.0,
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

    s_dob=canvas.create_text(
        842.0,
        528.0,
        anchor="nw",
        text=gl.u_dob,
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    s_level=canvas.create_text(
        838.0,
        617.0,
        anchor="nw",
        text=gl.s_level,
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
        x=2.0,
        y=471.0,
        width=45.0,
        height=31.0
    )

    canvas.create_rectangle(
        76.0,
        219.0,
        751.0,
        741.0,
        fill="#2F396B",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    vSys_btn = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_system_admin_data(),
        relief="flat"
    )
    vSys_btn.place(
        x=180.0,
        y=260.0,
        width=160.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    aSys_btn = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_system_admin_gui(),
        relief="flat"
    )
    aSys_btn.place(
        x=475.0,
        y=260.0,
        width=160.0,
        height=44.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    aHos_btn = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_hospital_manager_gui(),
        relief="flat"
    )
    aHos_btn.place(
        x=180.0,
        y=670.0,
        width=160.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    aNurse_btn = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_nurse_gui(),
        relief="flat"
    )
    aNurse_btn.place(
        x=475.0,
        y=464.0,
        width=160.0,
        height=44.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    aDoc_btn = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_doctor_gui(),
        relief="flat"
    )
    aDoc_btn.place(
        x=180.0,
        y=464.0,
        width=160.0,
        height=44.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    home_btn = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    home_btn.place(
        x=3.0,
        y=341.0,
        width=41.0,
        height=41.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    vDoc_btn = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_doctor_data(),
        relief="flat"
    )
    vDoc_btn.place(
        x=180.0,
        y=363.0,
        width=160.0,
        height=44.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_image_100 = PhotoImage(
        file=relative_to_assets("button_100.png"))
    vPharm_btn = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_pharmacist_data(),
        relief="flat"
    )
    vPharm_btn.place(
        x=475.0,
        y=567.0,
        width=160.0,
        height=44.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    aPharm_btn = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.add_pharmacist_gui(),
        relief="flat"
    )
    aPharm_btn.place(
        x=475.0,
        y=670.0,
        width=160.0,
        height=44.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    vNurse_btn = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_nurse_data(),
        relief="flat"
    )
    vNurse_btn.place(
        x=475.0,
        y=363.0,
        width=160.0,
        height=44.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    vHos_btn = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_hospital_manager_data(),
        relief="flat"
    )
    vHos_btn.place(
        x=180.0,
        y=568.0,
        width=160.0,
        height=44.0
    )
    mhistory_btn = Button(
        image=button_image_100,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fn.display_logs_data(),
        relief="flat"
    )
    mhistory_btn.place(
        x=4.0,
        y=404.0,
        width=38.0,
        height=41.0
    )
    window.resizable(False, False)
    window.mainloop()
#TODO: Add the code to display the labels of the System Admin