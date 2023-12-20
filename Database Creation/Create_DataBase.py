import sqlite3

# Connect to the database
conn = sqlite3.connect("../hospital_database2.sqlite")
cursor = conn.cursor()

# Create User table
cursor.execute("""
CREATE TABLE User (
    Username VARCHAR(255) PRIMARY KEY,
    DoB DATE,
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255),
    UserType VARCHAR(50),
    Password VARCHAR(255),
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);
""")

# Create HospitalManager table
cursor.execute("""
CREATE TABLE HospitalManager (
    Username VARCHAR(255) PRIMARY KEY,
    Role VARCHAR(50),
    AccessLevel INT,
    FOREIGN KEY (Username) REFERENCES User(Username)
);
""")

# Create SystemAdmin table
cursor.execute("""
CREATE TABLE SystemAdmin (
    Username VARCHAR(255) PRIMARY KEY,
    SecurityLevel INT,
    FOREIGN KEY (Username) REFERENCES User(Username)
);
""")

# Create Doctor table
cursor.execute("""
CREATE TABLE Doctor (
    Username VARCHAR(255) PRIMARY KEY,
    PagerNumber VARCHAR(20),
    LicenseNumber VARCHAR(50),
    Specialization VARCHAR(100),
    FOREIGN KEY (Username) REFERENCES User(Username)
);
""")

# Create Nurse table
cursor.execute("""
CREATE TABLE Nurse (
    Username VARCHAR(255) PRIMARY KEY,
    PagerNumber VARCHAR(20),
    LicenseNumber VARCHAR(50),
    FOREIGN KEY (Username) REFERENCES User(Username)
);
""")

# Create Pharmacist table
cursor.execute("""
CREATE TABLE Pharmacist (
    Username VARCHAR(255) PRIMARY KEY,
    LicenseNumber VARCHAR(50),
    FOREIGN KEY (Username) REFERENCES User(Username)
);
""")

# Create Patient table
cursor.execute("""
CREATE TABLE Patient (
    SSN VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255),
    Gender CHAR(1),
    DoB DATE,
    RoomNumber INT,
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);
""")

# Create Room table
cursor.execute("""
CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    NumberOfBeds INT,
    FloorNumber INT,
    NurseUsername VARCHAR(255),
    FOREIGN KEY (NurseUsername) REFERENCES Nurse(Username)
);
""")

# Create NHelpsD table
cursor.execute("""
CREATE TABLE NHelpsD (
    NurseUsername VARCHAR(255),
    DoctorUsername VARCHAR(255),
    PRIMARY KEY (NurseUsername, DoctorUsername),
    FOREIGN KEY (NurseUsername) REFERENCES Nurse(Username),
    FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username)
);
""")

# Create NHelpsP table
cursor.execute("""
CREATE TABLE NHelpsP (
    NurseUsername VARCHAR(255),
    PatientSSN VARCHAR(20),
    PRIMARY KEY (NurseUsername, PatientSSN),
    FOREIGN KEY (NurseUsername) REFERENCES Nurse(Username),
    FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN)
);
""")

# Create Resources table
cursor.execute("""
CREATE TABLE Resources (
    Res_ID INT PRIMARY KEY,
    Res_Name VARCHAR(100),
    Quantity INT,
    Type VARCHAR(50),
    Manufacture VARCHAR(100)
);
""")

# Create Medicine table
cursor.execute("""
CREATE TABLE Medicine (
    Res_ID INT PRIMARY KEY,
    Expiration DATE,
    Dosage VARCHAR(50),
    CurrentStock INT,
    Purpose VARCHAR(100),
    FOREIGN KEY (Res_ID) REFERENCES Resources(Res_ID)
);
""")

# Create Beholden table
cursor.execute("""
CREATE TABLE Beholden (
    PharmacistUsername VARCHAR(255),
    MedicineID INT,
    PRIMARY KEY (PharmacistUsername, MedicineID),
    FOREIGN KEY (PharmacistUsername) REFERENCES Pharmacist(Username),
    FOREIGN KEY (MedicineID) REFERENCES Medicine(Res_ID)
);
""")

# Create Medical_Equipment table
cursor.execute("""
CREATE TABLE Medical_Equipment (
    Res_ID INT PRIMARY KEY,
    Equipment_Type VARCHAR(50),
    Purchase_Date DATE,
    Current_Condition VARCHAR(100),
    FOREIGN KEY (Res_ID) REFERENCES Resources(Res_ID)
);
""")

# Create Utilizes table
cursor.execute("""
CREATE TABLE Utilizes (
    DoctorUsername VARCHAR(255),
    Res_ID INT,
    PRIMARY KEY (DoctorUsername, Res_ID),
    FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username),
    FOREIGN KEY (Res_ID) REFERENCES Resources(Res_ID)
);
""")

# Create Medical_History table
cursor.execute("""
CREATE TABLE Medical_History (
    MedHis_ID INT PRIMARY KEY,
    PatientSSN VARCHAR(20),
    FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN)
);
""")

# Create MedicalHistory_Diagnosis table
cursor.execute("""
CREATE TABLE MedicalHistory_Diagnosis (
    MedHis_ID INT,
    Diagnosis VARCHAR(100),
    PRIMARY KEY (MedHis_ID, Diagnosis),
    FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID)
);
""")

# Create Patient_Medication table
cursor.execute("""
CREATE TABLE Patient_Medication (
    MedHis_ID INT,
    Medicine_ID INT,
    PRIMARY KEY (MedHis_ID, Medicine_ID),
    FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID),
    FOREIGN KEY (Medicine_ID) REFERENCES Medicine(Res_ID)
);
""")

# Create Treats table
cursor.execute("""
CREATE TABLE Treats (
    DoctorUsername VARCHAR(255),
    PatientSSN VARCHAR(20),
    PRIMARY KEY (DoctorUsername, PatientSSN),
    FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username),
    FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN)
);
""")

# Create MedicalHistory_Treatment table
cursor.execute("""
CREATE TABLE MedicalHistory_Treatment (
    Treatment INT,
    MedHis_ID INT,
    PRIMARY KEY (Treatment, MedHis_ID),
    FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID)
);
""")

# Create MedicalHistory_Procedures table
cursor.execute("""
CREATE TABLE MedicalHistory_Procedures (
    Procedures INT,
    MedHis_ID INT,
    PRIMARY KEY (Procedures, MedHis_ID),
    FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID)
);
""")

# Create MedicalHistory_Allergies table
cursor.execute("""
CREATE TABLE MedicalHistory_Allergies (
    Allergies INT,
    MedHis_ID INT,
    PRIMARY KEY (Allergies, MedHis_ID),
    FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID)
);
""")

# Create Writes table
cursor.execute("""
CREATE TABLE Writes (
    MedHis_ID INT,
    DoctorUsername VARCHAR(255),
    PRIMARY KEY (MedHis_ID, DoctorUsername),
    FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID),
    FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username)
);
""")

# Commit the changes and close the database connection
conn.commit()
conn.close()
