from tkinter import Tk, Canvas, Button, PhotoImage, ttk
import functions as fn
def main():
    window = Tk()
    window.geometry("1109x794")
    window.configure(bg="#343E71")

    canvas = Canvas(
        window,
        bg="#343E71",
        height=794,
        width=1109,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Your existing code for images and text elements...

    # Create a Treeview widget for the table
    tree = ttk.Treeview(
        window,
        columns=("Name", "DOB", "Room Number", "Medical History ID"),
        show="headings"
    )

    # Define column headings
    tree.heading("Name", text="Patient's Name")
    tree.heading("DOB", text="Date of Birth")
    tree.heading("Room Number", text="Room Number")
    tree.heading("Medical History ID", text="Medical History ID")

    # Specify column widths
    tree.column("Name", width=200)
    tree.column("DOB", width=200)
    tree.column("Room Number", width=200)
    tree.column("Medical History ID", width=200)

    # Insert sample data (replace this with your actual data)
    tree.insert("", "end", values=("John Doe", "01/01/1990", "101", "MH12345"))
    tree.insert("", "end", values=("Jane Smith", "02/15/1985", "202", "MH56789"))

    # Place the Treeview widget inside the "area" rectangle
    tree.place(x=80, y=225, width=670, height=515)

    # Your existing code for buttons and other elements...

    area = canvas.create_rectangle(
        76.0,
        221.0,
        751.0,
        743.0,
        fill="#2F396B",
        outline=""
    )

    window.resizable(False, False)
    window.mainloop()
fn.display_helping_nurses()

