# Hospital Management System

The Hospital Management System is a software application designed to streamline and automate various tasks within a hospital environment. This system is built using Python and SQLite, providing a user-friendly interface for hospital staff.

## Functionalities

### 1. User Management
- **Register User**: Allows registration of users including nurses, doctors, pharmacists, and hospital managers.
- **User Login**: Provides secure login functionality for registered users.

### 2. Patient Management
- **Add Patient**: Enables the addition of patient records, including personal information, contact details, and assigned rooms.
- **Assign Nurse to Patient**: Assigns a nurse to a patient, creating a relationship between them.
- **View Assigned Patients (Nurse)**: Displays a list of patients assigned to a specific nurse.

### 3. Doctor Management
- **Add Doctor**: Adds a doctor to the system with details such as pager number, license number, and specialization.
- **Assign Nurse to Doctor**: Assigns a nurse to assist a doctor, creating a relationship between them.
- **View Assigned Nurses (Doctor)**: Displays a list of nurses assigned to a specific doctor.

### 4. Pharmacist Management
- **Add Pharmacist**: Adds a pharmacist to the system with a unique license number.
- **Sell Medicine**: Allows the pharmacist to sell medicine, updating stock in the database.

### 5. Hospital Manager Management
- **Add Hospital Manager**: Adds a hospital manager to the system with a specified role and access level.

### 6. Medicine Management
- **Add Medicine**: Enables the addition of medicine to the system, including details such as expiration date, dosage, and purpose.
- **Sell Medicine (Pharmacist)**: Allows the pharmacist to sell medicine, updating stock in the database.

### 7. Database Structure
# Hospital Management System

The Hospital Management System is a software application designed to streamline and automate various tasks within a hospital environment. This system is built using Python and SQLite, providing a user-friendly interface for hospital staff.

## Database Structure

### Tables

#### 1. User
- **Fields**: Username, DoB, PhoneNumber, Address, UserType, Password, FirstName, LastName
- **Primary Key**: Username

#### 2. HospitalManager
- **Fields**: Username, Role, Access_Level
- **Primary Key**: Username
- **Foreign Key**: Username (references User.Username)

#### 3. SystemAdmin
- **Fields**: Username, SecurityLevel
- **Primary Key**: Username
- **Foreign Key**: Username (references User.Username)

#### 4. Doctor
- **Fields**: Username, PagerNumber, LicenseNumber, Specialization
- **Primary Key**: Username
- **Foreign Key**: Username (references User.Username)

#### 5. Nurse
- **Fields**: Username, PagerNumber, LicenseNumber
- **Primary Key**: Username
- **Foreign Key**: Username (references User.Username)

#### 6. Pharmacist
- **Fields**: Username, LicenseNumber
- **Primary Key**: Username
- **Foreign Key**: Username (references User.Username)

#### 7. Patient
- **Fields**: SSN, FirstName, LastName, PhoneNumber, Address, Gender, DoB, RoomNumber
- **Primary Key**: SSN
- **Foreign Key**: RoomNumber (references Room.RoomNumber)

#### 8. Room
- **Fields**: RoomNumber, NumberOfBeds, FloorNumber, NurseUsername
- **Primary Key**: RoomNumber
- **Foreign Key**: NurseUsername (references Nurse.Username)

#### 9. NHelpsD
- **Fields**: NurseUsername, DoctorUsername
- **Primary Key**: (NurseUsername, DoctorUsername)
- **Foreign Key**: NurseUsername (references Nurse.Username), DoctorUsername (references Doctor.Username)

#### 10. NHelpsP
- **Fields**: NurseUsername, PatientSSN
- **Primary Key**: (NurseUsername, PatientSSN)
- **Foreign Key**: NurseUsername (references Nurse.Username), PatientSSN (references Patient.SSN)

#### 11. Resources
- **Fields**: Res_ID, Res_Name, Quantity, Type, Manufacture
- **Primary Key**: Res_ID

#### 12. Medicine
- **Fields**: Res_ID, Expiration, Dosage, CurrentStock, Purpose
- **Primary Key**: Res_ID
- **Foreign Key**: Res_ID (references Resources.Res_ID)

#### 13. Beholden
- **Fields**: PharmacistUsername, MedicineID
- **Primary Key**: (PharmacistUsername, MedicineID)
- **Foreign Key**: PharmacistUsername (references Pharmacist.Username), MedicineID (references Medicine.Res_ID)

#### 14. Medical_Equipment
- **Fields**: Res_ID, Equipment_Type, Purchase_Date, Current_Condition
- **Primary Key**: Res_ID
- **Foreign Key**: Res_ID (references Resources.Res_ID)

#### 15. Utilizes
- **Fields**: DoctorUsername, Res_ID
- **Primary Key**: (DoctorUsername, Res_ID)
- **Foreign Key**: DoctorUsername (references Doctor.Username), Res_ID (references Resources.Res_ID)

#### 16. Medical_History
- **Fields**: MedHis_ID, PatientSSN
- **Primary Key**: MedHis_ID
- **Foreign Key**: PatientSSN (references Patient.SSN)

#### 17. MedicalHistory_Diagnosis
- **Fields**: MedHis_ID, Diagnosis
- **Primary Key**: (MedHis_ID, Diagnosis)
- **Foreign Key**: MedHis_ID (references Medical_History.MedHis_ID)

#### 18. Patient_Medication
- **Fields**: MedHis_ID, Medicine_ID
- **Primary Key**: (MedHis_ID, Medicine_ID)
- **Foreign Key**: MedHis_ID (references Medical_History.MedHis_ID), Medicine_ID (references Medicine.Res_ID)

#### 19. Treats
- **Fields**: DoctorUsername, PatientSSN
- **Primary Key**: (DoctorUsername, PatientSSN)
- **Foreign Key**: DoctorUsername (references Doctor.Username), PatientSSN (references Patient.SSN)

#### 20. MedicalHistory_Treatment
- **Fields**: Treatment, MedHis_ID
- **Primary Key**: (Treatment, MedHis_ID)
- **Foreign Key**: MedHis_ID (references Medical_History.MedHis_ID)

#### 21. MedicalHistory_Procedures
- **Fields**: Procedures, MedHis_ID
- **Primary Key**: (Procedures, MedHis_ID)
- **Foreign Key**: MedHis_ID (references Medical_History.MedHis_ID)

#### 22. MedicalHistory_Allergies
- **Fields**: Allergies, MedHis_ID
- **Primary Key**: (Allergies, MedHis_ID)
- **Foreign Key**: MedHis_ID (references Medical_History.MedHis_ID)

#### 23. Writes
- **Fields**: MedHis_ID, DoctorUsername
- **Primary Key**: (MedHis_ID, DoctorUsername)
- **Foreign Key**: MedHis_ID (references Medical_History.MedHis_ID), DoctorUsername (references Doctor.Username)

### Foreign Key Constraints

- HospitalManager: Username (references User.Username)
- SystemAdmin: Username (references User.Username)
- Doctor: Username (references User.Username)
- Nurse: Username (references User.Username)
- Pharmacist: Username (references User.Username)
- Patient: RoomNumber (references Room.RoomNumber)
- Room: NurseUsername (references Nurse.Username)
- NHelpsD: NurseUsername (references Nurse.Username), DoctorUsername (references Doctor.Username)
- NHelpsP: NurseUsername (references Nurse.Username), PatientSSN (references Patient.SSN)
- Medicine: Res_ID (references Resources.Res_ID)
- Beholden: PharmacistUsername (references Pharmacist.Username), MedicineID (references Medicine.Res_ID)
- Medical_Equipment: Res_ID (references Resources.Res_ID)
- Utilizes: DoctorUsername (references Doctor.Username), Res_ID (references Resources.Res_ID)
- Medical_History: PatientSSN (references Patient.SSN)
- MedicalHistory_Diagnosis: MedHis_ID (references Medical_History.MedHis_ID)
- Patient_Medication: MedHis_ID (references Medical_History.MedHis_ID), Medicine_ID (references Medicine.Res_ID)
- Treats: DoctorUsername (references Doctor.Username), PatientSSN (references Patient.SSN)
- MedicalHistory_Treatment: MedHis_ID (references Medical_History.MedHis_ID)
- MedicalHistory_Procedures: MedHis_ID (references Medical_History.MedHis_ID)
- MedicalHistory_Allergies: MedHis_ID (references Medical_History.MedHis_ID)
- Writes: MedHis_ID (references Medical_History.MedHis_ID), DoctorUsername (references Doctor.Username)

## Usage

1. Clone the repository:
   ```bash
[   git clone https://github.com/your-username/hospital-management-system.git
](https://github.com/CodeGeek2003/HospitalDataBase_ManagmentSystem/)
2. Install Requirements:
-pip install -r requirements.txt
-pip3 install -r requirements.txt
3. Create Database:
-Run Create_DataBase.py
4. Open the Managment System:
-Run main.py and use Staff loging with the following credentials:
-Username: admin
-Password: admin

