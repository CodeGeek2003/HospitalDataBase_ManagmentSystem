from patient_login import patient_login
from staff_login import staff_login
import globals
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from login_gui import *
from patient_gui import open_patient
from doctor_gui import *
from nurse_gui import *
from pharmacist_gui import *
from sys_1_gui import *
from sys_2_gui import *
from hos_1_gui import *
from hos_2_gui import *
from MedHis import *
import tkinter.simpledialog
import csv
import os
from icecream import ic
def execute_query(query):
    conn = None
    try:
        # Establish a connection and create a cursor
        conn = sqlite3.connect("hospital_database.sqlite")
        cursor = conn.cursor()

        # Execute the query
        result = cursor.execute(query)

        # Fetch the results
        results = result.fetchall()

        return results

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def show_message_box(title, message):
    messagebox.showinfo(title, message)
def logout_func(window):
    window.destroy()
    login_gui(open_patient_login,open_staff_login)
def open_patient_gui(window):
    window.destroy()
    open_patient()
def open_doctor(window):
    window.destroy()
    open_doctor_gui()
def open_nurse(window):
    window.destroy()
    open_nurse_gui()
def open_pharmacist(window):
    window.destroy()
    open_pharmacist_gui()
def open_sys_1(window):
    window.destroy()
    open_sys_1_gui()
def open_sys_2(window):
    window.destroy()
    open_sys_2_gui()
def display_doctor_data():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT [User].*, Doctor.PagerNumber, Doctor.LicenseNumber, Doctor.Specialization
    FROM [User]
    RIGHT JOIN Doctor ON [User].Username = Doctor.Username
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    window = tk.Toplevel()
    window.title("User and Doctor Data")

    tree = ttk.Treeview(window)
    tree["columns"] = (
        "Username", "DoB", "PhoneNumber", "Address", "UserType", "Password",
        "FirstName", "LastName", "PagerNumber", "LicenseNumber", "Specialization"
    )

    for col in tree["columns"]:
        tree.column(col, anchor=tk.W, width=100)
        tree.heading(col, text=col, anchor=tk.W)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, conn))
    window.mainloop()
def display_nurse_data():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT [User].*, Nurse.PagerNumber, Nurse.LicenseNumber
    FROM [User]
    RIGHT JOIN Nurse ON [User].Username = Nurse.Username
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    window = tk.Toplevel()
    window.title("User and Nurse Data")

    tree = ttk.Treeview(window)
    tree["columns"] = (
        "Username", "DoB", "PhoneNumber", "Address", "UserType", "Password",
        "FirstName", "LastName", "PagerNumber", "LicenseNumber"
    )

    for col in tree["columns"]:
        tree.column(col, anchor=tk.W, width=100)
        tree.heading(col, text=col, anchor=tk.W)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, conn))
    window.mainloop()
def display_pharmacist_data():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT [User].*, Pharmacist.LicenseNumber
    FROM [User]
    RIGHT JOIN Pharmacist ON [User].Username = Pharmacist.Username
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    window = tk.Toplevel()
    window.title("User and Pharmacist Data")

    tree = ttk.Treeview(window)
    tree["columns"] = (
        "Username", "DoB", "PhoneNumber", "Address", "UserType", "Password",
        "FirstName", "LastName", "LicenseNumber"
    )

    for col in tree["columns"]:
        tree.column(col, anchor=tk.W, width=100)
        tree.heading(col, text=col, anchor=tk.W)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, conn))
    window.mainloop()
def display_hospital_manager_data():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT [User].*, HospitalManager.Role, HospitalManager.AccessLevel
    FROM [User]
    RIGHT JOIN HospitalManager ON [User].Username = HospitalManager.Username
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    window = tk.Toplevel()
    window.title("User and Hospital Manager Data")

    tree = ttk.Treeview(window)
    tree["columns"] = (
        "Username", "DoB", "PhoneNumber", "Address", "UserType", "Password",
        "FirstName", "LastName", "Role" ,"AccessLevel"
    )

    for col in tree["columns"]:
        tree.column(col, anchor=tk.W, width=100)
        tree.heading(col, text=col, anchor=tk.W)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, conn))
    window.mainloop()
def display_system_admin_data():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT [User].*, SystemAdmin.SecurityLevel
    FROM [User]
    RIGHT JOIN SystemAdmin ON [User].Username = SystemAdmin.Username
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    window = tk.Toplevel()
    window.title("User and System Admin Data")

    tree = ttk.Treeview(window)
    tree["columns"] = (
        "Username", "DoB", "PhoneNumber", "Address", "UserType", "Password",
        "FirstName", "LastName", "SecurityLevel"
    )

    for col in tree["columns"]:
        tree.column(col, anchor=tk.W, width=100)
        tree.heading(col, text=col, anchor=tk.W)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, conn))
    window.mainloop()
def on_close(window, conn):
    window.destroy()
    conn.close()
def check_patient_ssn(ssn,window):
    try:
        # Establish a connection and create a cursor
        conn = sqlite3.connect("hospital_database.sqlite")
        cursor = conn.cursor()

        # Execute the SELECT query to check if the SSN exists in the Patient table
        cursor.execute("SELECT COUNT(*) FROM Patient WHERE SSN = ?", (ssn,))
        result = cursor.fetchone()

        # Check the result
        if result and result[0] > 0:
            globals.p_ssn=ssn
            print(globals.p_ssn)
            open_patient_gui(window)
        else:
            show_message_box("Error", f"Patient with this SSN {ssn} does not exist in the Patient table.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()
def check_user_username(username,password,window):
    try:
        conn = sqlite3.connect("hospital_database.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*),UserType FROM User WHERE Username = ? AND Password =?", (username,password,))
        result = cursor.fetchone()
        gl.u_type=result[1]
        if result and result[0] > 0:
            if gl.u_type=="Doctor":
                gl.u_username = username
                open_doctor(window)
            elif gl.u_type=="Nurse":
                gl.u_username = username
                open_nurse(window)
            elif gl.u_type=="Pharmacist":
                gl.u_username = username
                ic(gl.u_username)
                open_pharmacist(window)
            elif gl.u_type=="SystemAdmin":
                gl.u_username=username
                cursor.execute("SELECT SecurityLevel FROM SystemAdmin WHERE Username = ?",
                               (username,))
                result = cursor.fetchone()
                gl.s_level=result[0]
                if gl.s_level==1:
                    open_sys_1(window)
                elif gl.s_level==2:
                    open_sys_2(window)

            elif gl.u_type=="HospitalManager":
                gl.u_username=username
                cursor.execute("SELECT AccessLevel FROM HospitalManager WHERE Username = ?",
                               (username,))
                result = cursor.fetchone()
                gl.h_level=result[0]
                if gl.h_level==1:
                    open_hos_1(window)
                elif gl.h_level==2:
                    open_hos_2(window)

        else:
            show_message_box("Error", f"Staff with this Username {username} does not exist, Please try again.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        if conn:
            conn.close()
def open_staff_login(window):
    window.destroy()
    staff_login(check_user_username)
def open_patient_login(window):
    window.destroy()
    patient_login(check_patient_ssn)
def open_login():
    login_gui(open_patient_login,open_patient_login)

def open_allergy_gui(window):
    window.destroy()
    allergy_gui()
def open_medhis_gui(window):
    window.destroy()
    open_medhis()
def open_hos_1(window):
    window.destroy()
    open_hos_1_gui()
def open_hos_2(window):
    window.destroy()
    open_hos_2_gui()
def display_written_medical_histories():
    print(gl.u_username)
    # Connect to the database
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    # Fetch medical histories for the specified doctor
    cursor.execute("""
        SELECT MH.MedHis_ID, 
               GROUP_CONCAT(DISTINCT MHA.Allergies) AS Allergies,
               GROUP_CONCAT(DISTINCT MHP.Procedures) AS Procedures,
               GROUP_CONCAT(DISTINCT MHD.Diagnosis) AS Diagnosis,
               GROUP_CONCAT(DISTINCT MHT.Treatment) AS Treatment
        FROM Medical_History MH
        LEFT JOIN MedicalHistory_Allergies MHA ON MH.MedHis_ID = MHA.MedHis_ID
        LEFT JOIN MedicalHistory_Procedures MHP ON MH.MedHis_ID = MHP.MedHis_ID
        LEFT JOIN MedicalHistory_Diagnosis MHD ON MH.MedHis_ID = MHD.MedHis_ID
        LEFT JOIN MedicalHistory_Treatment MHT ON MH.MedHis_ID = MHT.MedHis_ID
        WHERE MH.MedHis_ID IN (SELECT MedHis_ID FROM Writes WHERE DoctorUsername = ?)
        GROUP BY MH.MedHis_ID
    """, (gl.u_username,))

    medical_histories = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Create a GUI window with a tree view
    root = tk.Tk()
    root.title("Medical Histories")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Allergies", "Procedures", "Diagnosis", "Treatment")
    tree.heading("#0", text="Medical History ID")
    tree.heading("Allergies", text="Allergies")
    tree.heading("Procedures", text="Procedures")
    tree.heading("Diagnosis", text="Diagnosis")
    tree.heading("Treatment", text="Treatment")

    for history in medical_histories:
        tree.insert("", "end", text=history[0], values=(history[1], history[2], history[3], history[4]))

    tree.pack(expand=True, fill="both")

    # Run the GUI
    root.mainloop()
def display_helping_nurses_for_doctor():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT NHD.NurseUsername, U.FirstName, U.LastName, N.PagerNumber, N.LicenseNumber
        FROM NHelpsD NHD
        JOIN [User] U ON NHD.NurseUsername = U.Username
        JOIN Nurse N ON NHD.NurseUsername = N.Username
        WHERE NHD.DoctorUsername = ?
    """, (gl.u_username,))

    helping_nurses = cursor.fetchall()

    conn.close()

    root = tk.Tk()
    root.title("Helping Nurses")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Username", "First Name", "Last Name", "Pager Number", "License Number")
    tree.heading("#0", text="Nurse Username")
    tree.heading("Username", text="Username")
    tree.heading("First Name", text="First Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Pager Number", text="Pager Number")
    tree.heading("License Number", text="License Number")

    for nurse in helping_nurses:
        tree.insert("", "end", text=nurse[0], values=(nurse[0], nurse[1], nurse[2], nurse[3], nurse[4]))

    tree.pack(expand=True, fill="both")

    root.mainloop()
def display_utilized_tools_for_doctor():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT U.DoctorUsername, R.Res_ID, R.Res_Name, R.Quantity, R.Type, R.Manufacture
        FROM Utilizes U
        JOIN Resources R ON U.Res_ID = R.Res_ID
        WHERE U.DoctorUsername = ?
    """, (gl.u_username,))

    utilized_tools = cursor.fetchall()

    conn.close()

    root = tk.Tk()
    root.title("Utilized Tools for Doctor")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Doctor Username", "Resource ID", "Resource Name", "Quantity", "Type", "Manufacture")
    tree.heading("Doctor Username", text="Doctor Username")
    tree.heading("Resource ID", text="Resource ID")
    tree.heading("Resource Name", text="Resource Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Type", text="Type")
    tree.heading("Manufacture", text="Manufacture")

    for tool in utilized_tools:
        tree.insert("", "end", values=(tool[0], tool[1], tool[2], tool[3], tool[4], tool[5]))

    tree.pack(expand=True, fill="both")

    root.mainloop()
def modify_resource_quantity():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    resource_id = tkinter.simpledialog.askstring("Resource ID", "Enter Resource ID:")

    cursor.execute("""
        SELECT COUNT(*) FROM Utilizes
        WHERE DoctorUsername = ? AND Res_ID = ?
    """, (gl.u_username, resource_id))

    utilization_count = cursor.fetchone()[0]

    if utilization_count > 0:
        cursor.execute("""
            UPDATE Resources SET Quantity = Quantity - 1 WHERE Res_ID = ?
        """, (resource_id,))
    else:
        cursor.execute("""
            INSERT INTO Utilizes (DoctorUsername, Res_ID) VALUES (?, ?)
        """, (gl.u_username, resource_id))

        cursor.execute("""
            UPDATE Resources SET Quantity = Quantity - 1 WHERE Res_ID = ?
        """, (resource_id,))

    conn.commit()
    conn.close()
def add_medical_history():
    def save_medical_history():
        conn = sqlite3.connect("hospital_database.sqlite")
        cursor = conn.cursor()

        # Get values from the input fields
        patient_ssn = patient_ssn_var.get()
        allergies = allergies_entry.get().split(',')
        diagnoses = diagnoses_entry.get().split(',')
        procedures = procedures_entry.get().split(',')
        treatment = treatment_entry.get().split(',')

        # Remove white spaces
        allergies = [allergy.strip() for allergy in allergies]
        diagnoses = [diagnosis.strip() for diagnosis in diagnoses]
        procedures = [procedure.strip() for procedure in procedures]
        treatment = [treat.strip() for treat in treatment]

        # Insert into Medical_History table
        cursor.execute("INSERT INTO Medical_History (PatientSSN) VALUES (?)", (patient_ssn,))
        conn.commit()

        # Get the inserted Medical History ID
        cursor.execute("SELECT last_insert_rowid()")
        medhis_id = cursor.fetchone()[0]

        # Insert into respective tables
        for allergy in allergies:
            if allergy:
                cursor.execute("INSERT INTO MedicalHistory_Allergies (MedHis_ID, Allergies) VALUES (?, ?)",
                               (medhis_id, allergy))

        for diagnosis in diagnoses:
            if diagnosis:
                cursor.execute("INSERT INTO MedicalHistory_Diagnosis (MedHis_ID, Diagnosis) VALUES (?, ?)",
                               (medhis_id, diagnosis))

        for procedure in procedures:
            if procedure:
                cursor.execute("INSERT INTO MedicalHistory_Procedures (MedHis_ID, Procedures) VALUES (?, ?)",
                               (medhis_id, procedure))

        for treat in treatment:
            if treat:
                cursor.execute("INSERT INTO MedicalHistory_Treatment (MedHis_ID, Treatment) VALUES (?, ?)",
                               (medhis_id, treat))

        # Insert into Writes table
        cursor.execute("INSERT INTO Writes (MedHis_ID, DoctorUsername) VALUES (?, ?)",
                       (medhis_id, gl.u_username))
        cursor.execute("INSERT INTO Medical_History (MedHis_ID, PatientSSN) VALUES (?, ?)",
                       (medhis_id,patient_ssn,))

        conn.commit()
        conn.close()
        window.destroy()
        show_message_box("Success", "Medical History successfully added.")

    # Create a small window for entering medical history
    window = tk.Tk()
    window.title("Add Medical History")

    # Patient SSN
    tk.Label(window, text="Patient SSN:").grid(row=0, column=0, padx=5, pady=5)
    patient_ssn_var = tk.StringVar()
    tk.Entry(window, textvariable=patient_ssn_var).grid(row=0, column=1, padx=5, pady=5)

    # Allergies
    tk.Label(window, text="Allergies (comma-separated):").grid(row=1, column=0, padx=5, pady=5)
    allergies_entry = tk.Entry(window)
    allergies_entry.grid(row=1, column=1, padx=5, pady=5)

    # Diagnoses
    tk.Label(window, text="Diagnoses (comma-separated):").grid(row=2, column=0, padx=5, pady=5)
    diagnoses_entry = tk.Entry(window)
    diagnoses_entry.grid(row=2, column=1, padx=5, pady=5)

    # Procedures
    tk.Label(window, text="Procedures (comma-separated):").grid(row=3, column=0, padx=5, pady=5)
    procedures_entry = tk.Entry(window)
    procedures_entry.grid(row=3, column=1, padx=5, pady=5)

    # Treatment
    tk.Label(window, text="Treatment (comma-separated):").grid(row=4, column=0, padx=5, pady=5)
    treatment_entry = tk.Entry(window)
    treatment_entry.grid(row=4, column=1, padx=5, pady=5)

    # Save button
    save_button = tk.Button(window, text="Save", command=save_medical_history)
    save_button.grid(row=5, column=0, columnspan=2, pady=10)

    window.mainloop()
def add_patient_gui():
    def add_patient():
        ssn = ssn_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        room_number = room_number_entry.get()

        # Insert the patient into the database
        try:
            conn = sqlite3.connect("hospital_database.sqlite")  # Change the database name accordingly
            cursor = conn.cursor()

            # Example SQL query to insert a patient into the Patient table
            query = f"INSERT INTO Patient (SSN, FirstName, LastName, PhoneNumber, Address, Gender, DoB, RoomNumber) " \
                    f"VALUES ('{ssn}', '{first_name}', '{last_name}', '{phone_number}', '{address}', '{gender}', '{dob}', '{room_number}')"

            cursor.execute(query)
            conn.commit()

            # Show a success message
            messagebox.showinfo("Success", "Patient added successfully!")

            # Destroy the window after adding the patient
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding patient: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add Patient")

    # Create and place labels and entry widgets
    labels = ["SSN", "First Name", "Last Name", "Phone Number", "Address", "Gender", "DoB", "Room Number"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    ssn_entry = tk.Entry(window)
    ssn_entry.grid(row=0, column=1)

    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=1, column=1)

    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=2, column=1)

    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=3, column=1)

    address_entry = tk.Entry(window)
    address_entry.grid(row=4, column=1)

    gender_entry = tk.Entry(window)
    gender_entry.grid(row=5, column=1)

    dob_entry = tk.Entry(window)
    dob_entry.grid(row=6, column=1)

    room_number_entry = tk.Entry(window)
    room_number_entry.grid(row=7, column=1)

    # Button to add patient
    add_button = tk.Button(window, text="Add Patient", command=add_patient)
    add_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def view_assigned_patients():
    try:
        # Connect to the database
        conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
        cursor = conn.cursor()

        # Query to get patients assigned to the nurse
        query = f"SELECT * FROM NHelpsP " \
                f"JOIN Patient ON NHelpsP.PatientSSN = Patient.SSN " \
                f"WHERE NHelpsP.NurseUsername = '{gl.u_username}'"

        cursor.execute(query)
        patients = cursor.fetchall()

        if not patients:
            messagebox.showinfo("Info", "No patients assigned to this nurse.")
            return

        # Create a window to display the patient details
        window = tk.Tk()
        window.title("Assigned Patients")

        # Create a treeview widget to display data
        tree = ttk.Treeview(window)
        tree["columns"] = tuple([description[0] for description in cursor.description])

        for col in tree["columns"]:
            tree.column(col, anchor="w")
            tree.heading(col, text=col, anchor="w")

        for patient in patients:
            tree.insert("", "end", values=tuple(patient))

        tree.pack(expand=True, fill="both")

        # Run the GUI
        window.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching assigned patients: {str(e)}")

    finally:
        if conn:
            conn.close()
def view_assigned_doctors():
    try:
        # Connect to the database
        conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
        cursor = conn.cursor()

        # Query to get doctors assigned to the nurse
        query = f"SELECT User.FirstName AS DoctorFirstName, User.LastName AS DoctorLastName, " \
                f"Doctor.PagerNumber, Doctor.LicenseNumber " \
                f"FROM NHelpsD " \
                f"JOIN Doctor ON NHelpsD.DoctorUsername = Doctor.Username " \
                f"JOIN User ON Doctor.Username = User.Username " \
                f"WHERE NHelpsD.NurseUsername = '{gl.u_username}'"

        cursor.execute(query)
        doctors = cursor.fetchall()

        if not doctors:
            messagebox.showinfo("Info", "No doctors assigned to this nurse.")
            return

        # Create a window to display the doctor details
        window = tk.Tk()
        window.title("Assigned Doctors")

        # Create a treeview widget to display data
        tree = ttk.Treeview(window)
        tree["columns"] = tuple([description[0] for description in cursor.description])

        for col in tree["columns"]:
            tree.column(col, anchor="w")
            tree.heading(col, text=col, anchor="w")

        for doctor in doctors:
            tree.insert("", "end", values=tuple(doctor))

        tree.pack(expand=True, fill="both")

        # Run the GUI
        window.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching assigned doctors: {str(e)}")

    finally:
        if conn:
            conn.close()
def add_system_admin_gui():
    def add_system_admin():
        # Retrieve data from entry widgets
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        dob = dob_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        security_level = security_level_entry.get()

        try:
            # Connect to the database
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()

            # Insert user data into the User table
            user_query = f"INSERT INTO [User] (Username, DoB, PhoneNumber, Address, UserType, Password, FirstName, LastName) " \
                         f"VALUES ('{username}', '{dob}', '{phone_number}', '{address}', 'SystemAdmin', '{password}', '{first_name}', '{last_name}')"
            cursor.execute(user_query)

            # Insert system admin data into the SystemAdmin table
            sys_admin_query = f"INSERT INTO SystemAdmin (Username, SecurityLevel) " \
                              f"VALUES ('{username}', '{security_level}')"
            cursor.execute(sys_admin_query)

            # Commit the changes
            conn.commit()

            # Show a success message
            messagebox.showinfo("Success", "System Admin added successfully!")

            # Destroy the window after adding the system admin
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding system admin: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add System Admin")

    # Create and place labels and entry widgets
    labels = ["Username", "Password", "First Name", "Last Name", "DoB", "Phone Number", "Address", "Security Level"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=2, column=1)

    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=3, column=1)

    dob_entry = tk.Entry(window)
    dob_entry.grid(row=4, column=1)

    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=5, column=1)

    address_entry = tk.Entry(window)
    address_entry.grid(row=6, column=1)

    security_level_entry = tk.Entry(window)
    security_level_entry.grid(row=7, column=1)

    # Button to add system admin
    add_button = tk.Button(window, text="Add System Admin", command=add_system_admin)
    add_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def add_nurse_gui():
    def add_nurse():
        # Retrieve data from entry widgets
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        dob = dob_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        pager_number = pager_number_entry.get()
        license_number = license_number_entry.get()

        try:
            # Connect to the database
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()

            # Insert user data into the User table
            user_query = f"INSERT INTO [User] (Username, DoB, PhoneNumber, Address, UserType, Password, FirstName, LastName) " \
                         f"VALUES ('{username}', '{dob}', '{phone_number}', '{address}', 'Nurse', '{password}', '{first_name}', '{last_name}')"
            cursor.execute(user_query)

            # Insert nurse data into the Nurse table
            nurse_query = f"INSERT INTO Nurse (Username, PagerNumber, LicenseNumber) " \
                           f"VALUES ('{username}', '{pager_number}', '{license_number}')"
            cursor.execute(nurse_query)

            # Commit the changes
            conn.commit()

            # Show a success message
            messagebox.showinfo("Success", "Nurse added successfully!")

            # Destroy the window after adding the nurse
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding nurse: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add Nurse")

    # Create and place labels and entry widgets
    labels = ["Username", "Password", "First Name", "Last Name", "DoB", "Phone Number", "Address", "Pager Number", "License Number"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=2, column=1)

    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=3, column=1)

    dob_entry = tk.Entry(window)
    dob_entry.grid(row=4, column=1)

    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=5, column=1)

    address_entry = tk.Entry(window)
    address_entry.grid(row=6, column=1)

    pager_number_entry = tk.Entry(window)
    pager_number_entry.grid(row=7, column=1)

    license_number_entry = tk.Entry(window)
    license_number_entry.grid(row=8, column=1)

    # Button to add nurse
    add_button = tk.Button(window, text="Add Nurse", command=add_nurse)
    add_button.grid(row=9, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def add_doctor_gui():
    def add_doctor():
        # Retrieve data from entry widgets
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        dob = dob_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        pager_number = pager_number_entry.get()
        license_number = license_number_entry.get()
        specialization = specialization_entry.get()

        try:
            # Connect to the database
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()

            # Insert user data into the User table
            user_query = f"INSERT INTO [User] (Username, DoB, PhoneNumber, Address, UserType, Password, FirstName, LastName) " \
                         f"VALUES ('{username}', '{dob}', '{phone_number}', '{address}', 'Doctor', '{password}', '{first_name}', '{last_name}')"
            cursor.execute(user_query)

            # Insert doctor data into the Doctor table
            doctor_query = f"INSERT INTO Doctor (Username, PagerNumber, LicenseNumber, Specialization) " \
                            f"VALUES ('{username}', '{pager_number}', '{license_number}', '{specialization}')"
            cursor.execute(doctor_query)

            # Commit the changes
            conn.commit()

            # Show a success message
            messagebox.showinfo("Success", "Doctor added successfully!")

            # Destroy the window after adding the doctor
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding doctor: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add Doctor")

    # Create and place labels and entry widgets
    labels = ["Username", "Password", "First Name", "Last Name", "DoB", "Phone Number", "Address", "Pager Number", "License Number", "Specialization"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=2, column=1)

    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=3, column=1)

    dob_entry = tk.Entry(window)
    dob_entry.grid(row=4, column=1)

    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=5, column=1)

    address_entry = tk.Entry(window)
    address_entry.grid(row=6, column=1)

    pager_number_entry = tk.Entry(window)
    pager_number_entry.grid(row=7, column=1)

    license_number_entry = tk.Entry(window)
    license_number_entry.grid(row=8, column=1)

    specialization_entry = tk.Entry(window)
    specialization_entry.grid(row=9, column=1)

    # Button to add doctor
    add_button = tk.Button(window, text="Add Doctor", command=add_doctor)
    add_button.grid(row=10, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def add_pharmacist_gui():
    def add_pharmacist():
        # Retrieve data from entry widgets
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        dob = dob_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        license_number = license_number_entry.get()

        try:
            # Connect to the database
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()

            # Insert user data into the User table
            user_query = f"INSERT INTO [User] (Username, DoB, PhoneNumber, Address, UserType, Password, FirstName, LastName) " \
                         f"VALUES ('{username}', '{dob}', '{phone_number}', '{address}', 'Pharmacist', '{password}', '{first_name}', '{last_name}')"
            cursor.execute(user_query)

            # Insert pharmacist data into the Pharmacist table
            pharmacist_query = f"INSERT INTO Pharmacist (Username, LicenseNumber) " \
                               f"VALUES ('{username}', '{license_number}')"
            cursor.execute(pharmacist_query)

            # Commit the changes
            conn.commit()

            # Show a success message
            messagebox.showinfo("Success", "Pharmacist added successfully!")

            # Destroy the window after adding the pharmacist
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding pharmacist: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add Pharmacist")

    # Create and place labels and entry widgets
    labels = ["Username", "Password", "First Name", "Last Name", "DoB", "Phone Number", "Address", "License Number"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=2, column=1)

    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=3, column=1)

    dob_entry = tk.Entry(window)
    dob_entry.grid(row=4, column=1)

    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=5, column=1)

    address_entry = tk.Entry(window)
    address_entry.grid(row=6, column=1)

    license_number_entry = tk.Entry(window)
    license_number_entry.grid(row=7, column=1)

    # Button to add pharmacist
    add_button = tk.Button(window, text="Add Pharmacist", command=add_pharmacist)
    add_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def add_hospital_manager_gui():
    def add_hospital_manager():
        # Retrieve data from entry widgets
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        dob = dob_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        role = role_entry.get()
        access_level = access_level_entry.get()

        try:
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()
            user_query = f"INSERT INTO [User] (Username, DoB, PhoneNumber, Address, UserType, Password, FirstName, LastName) " \
                         f"VALUES ('{username}', '{dob}', '{phone_number}', '{address}', 'HospitalManager', '{password}', '{first_name}', '{last_name}')"
            cursor.execute(user_query)
            hospital_manager_query = f"INSERT INTO HospitalManager " \
                                     f"VALUES ('{username}', '{role}', '{access_level}')"
            cursor.execute(hospital_manager_query)

            conn.commit()

            messagebox.showinfo("Success", "Hospital Manager added successfully!")

            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding hospital manager: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add Hospital Manager")

    # Create and place labels and entry widgets
    labels = ["Username", "Password", "First Name", "Last Name", "DoB", "Phone Number", "Address", "Role", "Access Level"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=2, column=1)

    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=3, column=1)

    dob_entry = tk.Entry(window)
    dob_entry.grid(row=4, column=1)

    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=5, column=1)

    address_entry = tk.Entry(window)
    address_entry.grid(row=6, column=1)

    role_entry = tk.Entry(window)
    role_entry.grid(row=7, column=1)

    access_level_entry = tk.Entry(window)
    access_level_entry.grid(row=8, column=1)

    # Button to add hospital manager
    add_button = tk.Button(window, text="Add Hospital Manager", command=add_hospital_manager)
    add_button.grid(row=9, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def sell_medicine_gui():
    def sell_medicine():
        # Retrieve data from entry widgets
        medicine_id = medicine_id_entry.get()
        quantity_sold = int(quantity_sold_entry.get())

        try:
            # Connect to the database
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()

            # Check if medicine exists in the Medicine table
            check_query = f"SELECT * FROM Medicine WHERE Res_ID = {medicine_id}"
            cursor.execute(check_query)
            medicine = cursor.fetchone()

            if not medicine:
                messagebox.showinfo("Info", "Medicine not found in the database.")
                return

            current_stock = medicine[3]  # Index 3 is the CurrentStock column

            if quantity_sold > current_stock:
                messagebox.showinfo("Info", "Not enough stock available.")
            else:
                # Update the CurrentStock in the Medicine table
                update_query = f"UPDATE Medicine SET CurrentStock = {current_stock - quantity_sold} WHERE Res_ID = {medicine_id}"
                cursor.execute(update_query)

                # Commit the changes
                conn.commit()

                # Show a success message
                messagebox.showinfo("Success", f"{quantity_sold} units of medicine sold successfully!")

                # Destroy the window after selling the medicine
                window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error selling medicine: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Sell Medicine")

    # Create and place labels and entry widgets
    labels = ["Medicine ID", "Quantity Sold"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    medicine_id_entry = tk.Entry(window)
    medicine_id_entry.grid(row=0, column=1)

    quantity_sold_entry = tk.Entry(window)
    quantity_sold_entry.grid(row=1, column=1)

    # Button to sell medicine
    sell_button = tk.Button(window, text="Sell Medicine", command=sell_medicine)
    sell_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def add_medicine_gui():
    def add_medicine():
        # Retrieve data from entry widgets
        res_id = res_id_entry.get()
        res_name = res_name_entry.get()
        quantity = int(quantity_entry.get())
        type_var = type_entry.get()
        manufacture = manufacture_entry.get()
        expiration = expiration_entry.get()
        dosage = dosage_entry.get()
        current_stock = int(current_stock_entry.get())
        purpose = purpose_entry.get()

        try:
            # Connect to the database
            conn = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
            cursor = conn.cursor()

            # Insert data into the Resources table
            resources_query = f"INSERT INTO Resources (Res_ID, Res_Name, Quantity, Type, Manufacture) " \
                              f"VALUES ({res_id}, '{res_name}', {quantity}, '{type_var}', '{manufacture}')"
            cursor.execute(resources_query)

            # Insert data into the Medicine table
            medicine_query = f"INSERT INTO Medicine (Res_ID, Expiration, Dosage, CurrentStock, Purpose) " \
                             f"VALUES ({res_id}, '{expiration}', '{dosage}', {current_stock}, '{purpose}')"
            cursor.execute(medicine_query)

            # Commit the changes
            conn.commit()

            # Show a success message
            messagebox.showinfo("Success", "Medicine added successfully!")

            # Destroy the window after adding the medicine
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding medicine: {str(e)}")

        finally:
            if conn:
                conn.close()

    # Create the main window
    window = tk.Tk()
    window.title("Add Medicine")

    # Create and place labels and entry widgets
    labels = ["Res ID", "Resource Name", "Quantity", "Type", "Manufacture",
              "Expiration", "Dosage", "Current Stock", "Purpose"]
    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

    # Entry widgets
    res_id_entry = tk.Entry(window)
    res_id_entry.grid(row=0, column=1)

    res_name_entry = tk.Entry(window)
    res_name_entry.grid(row=1, column=1)

    quantity_entry = tk.Entry(window)
    quantity_entry.grid(row=2, column=1)

    type_entry = tk.Entry(window)
    type_entry.grid(row=3, column=1)

    manufacture_entry = tk.Entry(window)
    manufacture_entry.grid(row=4, column=1)

    expiration_entry = tk.Entry(window)
    expiration_entry.grid(row=5, column=1)

    dosage_entry = tk.Entry(window)
    dosage_entry.grid(row=6, column=1)

    current_stock_entry = tk.Entry(window)
    current_stock_entry.grid(row=7, column=1)

    purpose_entry = tk.Entry(window)
    purpose_entry.grid(row=8, column=1)

    # Button to add medicine
    add_button = tk.Button(window, text="Add Medicine", command=add_medicine)
    add_button.grid(row=9, column=0, columnspan=2, pady=10)

    # Run the GUI
    window.mainloop()
def get_hospital_manager_data():
    import sqlite3

    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()
    query = """
    SELECT u.FirstName || ' ' || u.LastName AS Name, u.DoB, hm.AccessLevel
    FROM [User] u
    JOIN HospitalManager hm ON u.Username = hm.Username
    WHERE u.Username =?;
    """
    cursor.execute(query,(gl.u_username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        gl.u_name = result[0]
        gl.u_dob = result[1]
        gl.h_level = result[2]
def get_doctor_info_and_patient_count():
    import sqlite3

    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT u.FirstName || ' ' || u.LastName AS DoctorName, u.DoB AS DoctorDoB, d.PagerNumber, COUNT(t.PatientSSN) AS PatientCount
    FROM [User] u
    JOIN Doctor d ON u.Username = d.Username
    LEFT JOIN Treats t ON d.Username = t.DoctorUsername
    WHERE u.Username = ?;
    """

    cursor.execute(query, (gl.u_username,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        gl.u_name = result[0]
        gl.u_dob = result[1]
        gl.d_pager = result[2]
        gl.d_p_count = result[3]
def get_pharmacist_info():
    ic(gl.u_username)
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT u.FirstName || ' ' || u.LastName AS PharmacistName, u.DoB AS PharmacistDoB, p.LicenseNumber
    FROM [User] u
    JOIN Pharmacist p ON u.Username = p.Username
    WHERE u.Username = ?;
    """
    cursor.execute(query, (gl.u_username,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        gl.u_name = result[0]
        gl.u_dob = result[1]
        gl.ph_license = result[2]
def get_nurse_info():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT u.FirstName || ' ' || u.LastName AS NurseName, u.DoB AS NurseDoB, COUNT(nhp.PatientSSN) AS NumberOfPatients, n.PagerNumber
    FROM [User] u
    JOIN Nurse n ON u.Username = n.Username
    LEFT JOIN NHelpsP nhp ON n.Username = nhp.NurseUsername
    WHERE u.Username = ?;
    """

    cursor.execute(query, (gl.u_username,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        gl.u_name = result[0]
        gl.u_dob = result[1]
        gl.n_patient_count = 0
        gl.n_pager = result[3]
    else:
        gl.u_name = 'Not Found'
        gl.u_dob = 'Not Found'
        gl.n_patient_count = 0
        gl.n_pager = 'Not Found'
def get_system_admin_info():

    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT u.FirstName || ' ' || u.LastName AS AdminName, u.DoB AS AdminDoB, sa.SecurityLevel AS AccessLevel
    FROM [User] u
    JOIN SystemAdmin sa ON u.Username = sa.Username
    WHERE u.Username = ?;
    """

    cursor.execute(query, (gl.u_username,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        gl.u_name = result[0]
        gl.u_dob = result[1]
        gl.s_level = result[2]
    else:
        gl.u_name = 'Not Found'
        gl.u_dob = 'Not Found'
        gl.s_level = 'Not Found'
def display_allergies_for_patient():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    # Retrieve the patient's medical history ID
    cursor.execute("""
        SELECT MHI.MedHis_ID
        FROM Medical_History MHI
        JOIN Patient P ON MHI.PatientSSN = P.SSN
        WHERE P.SSN = ?
    """, (gl.p_ssn,))

    medical_history_id = cursor.fetchone()

    if medical_history_id:
        # Retrieve allergies for the patient from MedicalHistory_Allergies
        cursor.execute("""
            SELECT * FROM MedicalHistory_Allergies
            WHERE MedHis_ID = ?
        """, (medical_history_id[0],))

        patient_allergies = cursor.fetchall()

        conn.close()

        root = Tk()
        root.title("Patient Allergies")

        tree = ttk.Treeview(root)
        tree["columns"] = ("Medical_History" ,"AllergyID")
        tree.heading("Medical_History", text="Medical History")
        tree.heading("AllergyID", text="Allergy")

        for allergy in patient_allergies:
            tree.insert("", "end", text=allergy[0], values=(allergy[0], allergy[1]))

        tree.pack(expand=True, fill="both")

        root.mainloop()

def display_diagnosis_for_patient():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    # Retrieve the patient's medical history ID
    cursor.execute("""
        SELECT MHI.MedHis_ID
        FROM Medical_History MHI
        JOIN Patient P ON MHI.PatientSSN = P.SSN
        WHERE P.SSN = ?
    """, (gl.p_ssn,))

    medical_history_id = cursor.fetchone()

    if medical_history_id:
        cursor.execute("""
            SELECT * FROM MedicalHistory_Diagnosis
            WHERE MedHis_ID = ?
        """, (medical_history_id[0],))

        patient_allergies = cursor.fetchall()

        conn.close()

        root = Tk()
        root.title("Patient Diagnosis")

        tree = ttk.Treeview(root)
        tree["columns"] = ("Medical_History","DiagnosisID")
        tree.heading("Medical_History", text="Medical History")
        tree.heading("DiagnosisID", text="Diagnosis")

        for allergy in patient_allergies:
            tree.insert("", "end", text=allergy[0], values=(allergy[0], allergy[1]))

        tree.pack(expand=True, fill="both")

        root.mainloop()

def display_procedures_for_patient():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    # Retrieve the patient's medical history ID
    cursor.execute("""
        SELECT MHI.MedHis_ID
        FROM Medical_History MHI
        JOIN Patient P ON MHI.PatientSSN = P.SSN
        WHERE P.SSN = ?
    """, (gl.p_ssn,))

    medical_history_id = cursor.fetchone()

    if medical_history_id:
        cursor.execute("""
            SELECT * FROM MedicalHistory_Procedures
            WHERE MedHis_ID = ?
        """, (medical_history_id[0],))

        patient_procedure = cursor.fetchall()

        conn.close()

        root = Tk()
        root.title("Patient Procedures")

        tree = ttk.Treeview(root)
        tree["columns"] = ("Medical_History","ProcedureID")
        tree.heading("Medical_History", text="Medical History")
        tree.heading("ProcedureID", text="Procedure")

        for procedure in patient_procedure:
            tree.insert("", "end", text=procedure[0], values=(procedure[0], procedure[1]))

        tree.pack(expand=True, fill="both")

        root.mainloop()
def display_treatment_for_patient():
    conn = sqlite3.connect("hospital_database.sqlite")
    cursor = conn.cursor()

    # Retrieve the patient's medical history ID
    cursor.execute("""
        SELECT MHI.MedHis_ID
        FROM Medical_History MHI
        JOIN Patient P ON MHI.PatientSSN = P.SSN
        WHERE P.SSN = ?
    """, (gl.p_ssn,))

    medical_history_id = cursor.fetchone()

    if medical_history_id:
        cursor.execute("""
            SELECT * FROM MedicalHistory_Treatment
            WHERE MedHis_ID = ?
        """, (medical_history_id[0],))

        patient_treatment = cursor.fetchall()

        conn.close()

        root = Tk()
        root.title("Patient Treatment")

        tree = ttk.Treeview(root)
        tree["columns"] = ("Medical_History","TreatmentID")
        tree.heading("Medical_History", text="Medical History")
        tree.heading("TreatmentID", text="Treatment")

        for treatment in patient_treatment:
            tree.insert("", "end", text=treatment[0], values=(treatment[0], treatment[1]))

        tree.pack(expand=True, fill="both")

        root.mainloop()
def display_logs_data():
    connection = sqlite3.connect("hospital_database.sqlite")  # Replace with your actual database name
    cursor = connection.cursor()

    # Retrieve all data from the logs table
    cursor.execute("SELECT * FROM logs")
    logs_data = cursor.fetchall()

    connection.close()

    root = tk.Tk()
    root.title("Logs Data")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Action", "Table", "Date")
    tree.heading("Action", text="Action")
    tree.heading("Table", text="Table")
    tree.heading("Date", text="Date")

    for log_entry in logs_data:
        tree.insert("", "end", values=log_entry)

    tree.pack(expand=True, fill="both")

    root.mainloop()

