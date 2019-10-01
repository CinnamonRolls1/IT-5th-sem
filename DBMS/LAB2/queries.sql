\! echo "=================================================================================================";
\! echo "Q1____________________________________________________________";
SELECT Patient.name AS "Patient", PhysicianE.name AS "Physician" FROM Patient JOIN PhysicianE ON pcp=employeeid WHERE pcp NOT IN (SELECT head FROM Department);
\! echo "Q2____________________________________________________________";
SELECT Patient.name AS "Patient",
       PhysicianE.name AS "Primary Physician",
       Nurse.name AS "Nurse"
FROM Appointment
JOIN Patient ON Appointment.patient=Patient.ssn
JOIN Nurse ON Appointment.prepnurse=Nurse.employeeid
JOIN PhysicianE ON Patient.pcp=PhysicianE.employeeid
WHERE Appointment.patient IN
    (SELECT Patient
     FROM Appointment
     GROUP BY Appointment.patient
     HAVING count(*)>=2)
  AND Nurse.registered='true'
ORDER BY Patient.name;

\! echo "Q3____________________________________________________________";
SELECT Patient.name AS "Patient",
       PhysicianE.name AS "Primary Physician",
       Procedures.cost AS "Cost"
FROM Patient
JOIN Undergoes ON Undergoes.patient=Patient.ssn
JOIN PhysicianE ON Patient.pcp=PhysicianE.employeeid
JOIN Procedures ON Undergoes.Procedures=Procedures.code
WHERE Procedures.cost>5000;

\! echo "Q4____________________________________________________________";
SELECT PhysicianE.name AS "Physician",
       PhysicianE.position AS "Position",
       Procedures.name AS "Procedure",
       Undergoes.DateUndergoes AS "Date of Procedure",
       Patient.name AS "Patient",
       Trained_In.certificationexpires AS "Expiry Date of Certificate"
FROM PhysicianE, Undergoes, Patient, Procedures, Trained_In
WHERE Undergoes.Patient = Patient.ssn
  AND Undergoes.Procedures = Procedures.code
  AND Undergoes.Physician = PhysicianE.employeeid
  AND Procedures.code = Trained_In.treatment
  AND PhysicianE.EmployeeId = Trained_In.physician
  AND Undergoes.DateUndergoes > Trained_In.certificationexpires;

\! echo "Q5____________________________________________________________";
SELECT PhysicianE.name AS "Physician",
       Procedures.name AS "Procedure",
       Undergoes.DateUndergoes,
       Patient.name AS "Patient"
FROM PhysicianE,
     Undergoes,
     Patient,
     Procedures
WHERE Undergoes.Patient = Patient.SSN
  AND Undergoes.Procedures = Procedures.Code
  AND Undergoes.Physician = PhysicianE.EmployeeID
  AND NOT EXISTS
    ( SELECT *
     FROM Trained_In
     WHERE Trained_In.treatment = Undergoes.Procedures
       AND Trained_In.physician = Undergoes.Physician );

\! echo "=================================================================================================";



