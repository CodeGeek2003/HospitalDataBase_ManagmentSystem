CREATE DATABASE Hospital_Database
-- User table --
USE Hospital_Database
CREATE TABLE [User] (
    Username VARCHAR(255) PRIMARY KEY,
    DoB DATE,
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255),
    UserType VARCHAR(50),
    Password VARCHAR(255),
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

-- HospitalManager table --
CREATE TABLE HospitalManager (
    Username VARCHAR(255) PRIMARY KEY,
    [Role] VARCHAR(50),
    [Access_Level] INT
);

-- SystemAdmin table --
CREATE TABLE SystemAdmin (
    Username VARCHAR(255) PRIMARY KEY,
    SecurityLevel INT
);

-- Doctor table --
CREATE TABLE Doctor (
    Username VARCHAR(255) PRIMARY KEY,
    PagerNumber VARCHAR(20),
    LicenseNumber VARCHAR(50),
    Specialization VARCHAR(100)
);

-- Nurse table --
CREATE TABLE Nurse (
    Username VARCHAR(255) PRIMARY KEY,
    PagerNumber VARCHAR(20),
    LicenseNumber VARCHAR(50)
);

-- Pharmacist table --
CREATE TABLE Pharmacist (
    Username VARCHAR(255) PRIMARY KEY,
    LicenseNumber VARCHAR(50)
);

-- Patient table --
CREATE TABLE Patient (
    SSN VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255),
    Gender CHAR(1),
    DoB DATE,
    RoomNumber INT
);

-- Room table --
CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    NumberOfBeds INT,
    FloorNumber INT,
    NurseUsername VARCHAR(255)
);

-- NHelpsD table --
CREATE TABLE NHelpsD (
    NurseUsername VARCHAR(255),
    DoctorUsername VARCHAR(255),
    PRIMARY KEY (NurseUsername, DoctorUsername)
);

-- NHelpsP table --
CREATE TABLE NHelpsP (
    NurseUsername VARCHAR(255),
    PatientSSN VARCHAR(20),
    PRIMARY KEY (NurseUsername, PatientSSN)
);

-- Resources table --
CREATE TABLE Resources (
    Res_ID INT PRIMARY KEY,
    Res_Name VARCHAR(100),
    Quantity INT,
    Type VARCHAR(50),
    Manufacture VARCHAR(100)
);

-- Medicine table --
CREATE TABLE Medicine (
    Res_ID INT PRIMARY KEY,
    Expiration DATE,
    Dosage VARCHAR(50),
    CurrentStock INT,
    Purpose VARCHAR(100)
);

-- Beholden table --
CREATE TABLE Beholden (
    PharmacistUsername VARCHAR(255),
    MedicineID INT,
    PRIMARY KEY (PharmacistUsername, MedicineID)
);

-- Medical_Equipment table --
CREATE TABLE Medical_Equipment (
    Res_ID INT PRIMARY KEY,
    Equipment_Type VARCHAR(50),
    Purchase_Date DATE,
    Current_Condition VARCHAR(100)
);

-- Utilizes table --
CREATE TABLE Utilizes (
    DoctorUsername VARCHAR(255),
    Res_ID INT,
    PRIMARY KEY (DoctorUsername, Res_ID)
);

-- Medical_History table --
CREATE TABLE Medical_History (
    MedHis_ID INT PRIMARY KEY,
    PatientSSN VARCHAR(20)
);

-- MedicalHistory_Diagnosis table --
CREATE TABLE MedicalHistory_Diagnosis (
    MedHis_ID INT,
    Diagnosis VARCHAR(100),
    PRIMARY KEY (MedHis_ID, Diagnosis)
);

-- Patient_Medication table --
CREATE TABLE Patient_Medication (
    MedHis_ID INT,
    Medicine_ID INT,
    PRIMARY KEY (MedHis_ID, Medicine_ID)
);

-- Treats table --
CREATE TABLE Treats (
    DoctorUsername VARCHAR(255),
    PatientSSN VARCHAR(20),
    PRIMARY KEY (DoctorUsername, PatientSSN)
);

-- MedicalHistory_Treatment table --
CREATE TABLE MedicalHistory_Treatment (
    Treatment INT,
    MedHis_ID INT,
    PRIMARY KEY (Treatment, MedHis_ID)
);

-- MedicalHistory_Procedures table --
CREATE TABLE MedicalHistory_Procedures (
    Procedures INT,
    MedHis_ID INT,
    PRIMARY KEY (Procedures, MedHis_ID)
);

-- MedicalHistory_Allergies table --
CREATE TABLE MedicalHistory_Allergies (
    Allergies INT,
    MedHis_ID INT,
    PRIMARY KEY (Allergies, MedHis_ID)
);

-- Writes table --
CREATE TABLE Writes (
    MedHis_ID INT,
    DoctorUsername VARCHAR(255),
    PRIMARY KEY (MedHis_ID, DoctorUsername)
);

-- Add Foreign Key Constraints --
ALTER TABLE HospitalManager
ADD FOREIGN KEY (Username) REFERENCES [User](Username);

ALTER TABLE SystemAdmin
ADD FOREIGN KEY (Username) REFERENCES [User](Username);

ALTER TABLE Doctor
ADD FOREIGN KEY (Username) REFERENCES [User](Username);

ALTER TABLE Nurse
ADD FOREIGN KEY (Username) REFERENCES [User](Username);

ALTER TABLE Pharmacist
ADD FOREIGN KEY (Username) REFERENCES [User](Username);

ALTER TABLE Patient
ADD FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber);

ALTER TABLE Room
ADD FOREIGN KEY (NurseUsername) REFERENCES Nurse(Username);

ALTER TABLE NHelpsD
ADD FOREIGN KEY (NurseUsername) REFERENCES Nurse(Username);

ALTER TABLE NHelpsD
ADD FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username);

ALTER TABLE NHelpsP
ADD FOREIGN KEY (NurseUsername) REFERENCES Nurse(Username);

ALTER TABLE NHelpsP
ADD FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN);

ALTER TABLE Medicine
ADD FOREIGN KEY (Res_ID) REFERENCES Resources(Res_ID);

ALTER TABLE Beholden
ADD FOREIGN KEY (PharmacistUsername) REFERENCES Pharmacist(Username);

ALTER TABLE Beholden
ADD FOREIGN KEY (MedicineID) REFERENCES Medicine(Res_ID);

ALTER TABLE Medical_Equipment
ADD FOREIGN KEY (Res_ID) REFERENCES Resources(Res_ID);

ALTER TABLE Utilizes
ADD FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username);

ALTER TABLE Utilizes
ADD FOREIGN KEY (Res_ID) REFERENCES Resources(Res_ID);

ALTER TABLE Medical_History
ADD FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN);

ALTER TABLE MedicalHistory_Diagnosis
ADD FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID);

ALTER TABLE Patient_Medication
ADD FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID);

ALTER TABLE Patient_Medication
ADD FOREIGN KEY (Medicine_ID) REFERENCES Medicine(Res_ID);

ALTER TABLE Treats
ADD FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username);

ALTER TABLE Treats
ADD FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN);

ALTER TABLE MedicalHistory_Treatment
ADD FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID);

ALTER TABLE MedicalHistory_Procedures
ADD FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID);

ALTER TABLE MedicalHistory_Allergies
ADD FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID);

ALTER TABLE Writes
ADD FOREIGN KEY (MedHis_ID) REFERENCES Medical_History(MedHis_ID);

ALTER TABLE Writes
ADD FOREIGN KEY (DoctorUsername) REFERENCES Doctor(Username);

                       --Triggers--
CREATE TABLE logs (
    action VARCHAR(20),
    [table] VARCHAR(20),
    [date] DATETIME
);

CREATE TRIGGER USER_INSERT AFTER INSERT ON [user]
BEGIN
    INSERT INTO logs VALUES ('INSERT', 'USER', DATETIME('now'));
END;

CREATE TRIGGER USER_DELETE AFTER DELETE ON [user]
BEGIN
    INSERT INTO logs VALUES ('DELETE', 'USER', DATETIME('now'));
END;

CREATE TRIGGER PATIENT_INSERT AFTER INSERT ON PATIENT
BEGIN
    INSERT INTO logs VALUES ('INSERT', 'PATIENT', DATETIME('now'));
END;

CREATE TRIGGER PATIENT_DELETE AFTER DELETE ON PATIENT
BEGIN
    INSERT INTO logs VALUES ('DELETE', 'PATIENT', DATETIME('now'));
END;

CREATE TRIGGER MEDICINE_INSERT AFTER INSERT ON MEDICINE
BEGIN
    INSERT INTO logs VALUES ('INSERT', 'MEDICINE', DATETIME('now'));
END;

CREATE TRIGGER MEDICINE_DELETE AFTER DELETE ON MEDICINE
BEGIN
    INSERT INTO logs VALUES ('DELETE', 'MEDICINE', DATETIME('now'));
END;
                                -- Stored Procedures --
/*
CREATE PROCEDURE GetUserInformation AS
BEGIN
    SELECT * FROM [User];
END;
CREATE PROCEDURE GetPatientInformation AS
BEGIN
    SELECT * FROM Patient;
END;
CREATE PROCEDURE GetMedicineInformation AS
BEGIN
    SELECT * FROM Medicine;
END;
 */
-------------------- in sql lite procedures are not supported --------------------
CREATE VIEW GetUserInformation AS
SELECT * FROM [User];
CREATE VIEW GetPatientInformation AS
SELECT * FROM Patient;
CREATE VIEW GetMedicineInformation AS
SELECT * FROM Medicine;
-----------------------------------------------------------------------------------
-- Retrieve User information
SELECT * FROM GetUserInformation;

-- Retrieve Patient information
SELECT * FROM GetPatientInformation;

-- Retrieve Medicine information
SELECT * FROM GetMedicineInformation;
-----------------------------------------------------------------------------------
--create non clustered index on patient table
CREATE INDEX patient_index ON Patient(SSN,DoB);
--create non clustered index on medicine table
CREATE INDEX medicine_index ON Medicine(Res_ID,Expiration);
--create non clustered index on user table
CREATE INDEX user_index ON [User](Username,DoB);
-----------------------------------------------------------------------------------

/*
-- Declare a cursor for the USER_INFO table
DECLARE user_cursor CURSOR FOR
    SELECT 'NewUser' AS USERNAME, 'UserRole' AS ROLE_USER, 'UserPassword' AS PASSWORD_USER, 1 AS SECURITY_CLEARANCE;

DECLARE @USERNAME VARCHAR(50);
DECLARE @ROLE_USER VARCHAR(60);
DECLARE @PASSWORD_USER VARCHAR(13);
DECLARE @SECURITY_CLEARANCE INT;
DECLARE @DYNAMICUSERNAME VARCHAR(50);
DECLARE @COUNTER INT = 8;
DECLARE @P_COUNTER INT = 0;

OPEN user_cursor;

FETCH NEXT FROM user_cursor INTO @DYNAMICUSERNAME, @ROLE_USER, @PASSWORD_USER, @SECURITY_CLEARANCE;

WHILE @P_COUNTER < 5
BEGIN
    -- Append counter to make the username unique
    SET @DYNAMICUSERNAME = 'NewUser' + CAST(@COUNTER AS VARCHAR(10));

    -- Insert data into USER_INFO table
    INSERT INTO USER_INFO (USERNAME, ROLE_USER, PASSWORD_USER, SECURITY_CLEARANCE)
    VALUES (@DYNAMICUSERNAME, @ROLE_USER, @PASSWORD_USER, @SECURITY_CLEARANCE);

    -- Increment counters
    SET @COUNTER = @COUNTER + 1;
    SET @P_COUNTER = @P_COUNTER + 1;

    -- Fetch the next row
    FETCH NEXT FROM user_cursor INTO @DYNAMICUSERNAME, @ROLE_USER, @PASSWORD_USER, @SECURITY_CLEARANCE;
END

CLOSE user_cursor;
DEALLOCATE user_cursor;

SELECT * FROM USER_INFO;
DELETE FROM  USER_INFO




*/
