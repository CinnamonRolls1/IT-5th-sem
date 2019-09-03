-- 1 
\! echo "Q1____________________________________________________________";
SELECT Fname,Bdate,Address from EMPLOYEE inner join DEPARTMENT on DEPARTMENT.Dnumber = EMPLOYEE.Dno and DEPARTMENT.Dname = "Administration";
-- 2
\! echo "Q2____________________________________________________________";
SELECT SUM(Salary),MAX(Salary),MIN(Salary),AVG(Salary) from EMPLOYEE inner join DEPARTMENT on Dnumber=Dno and Dname="Research";
-- 3
\! echo "Q3____________________________________________________________";
SELECT COUNT(*) as "Administration Count"  from EMPLOYEE inner join DEPARTMENT on Dnumber=Dno and Dname="Administration";
-- 4
\! echo "Q4____________________________________________________________";
SELECT Pnumber,Pname,COUNT(*) from PROJECT inner join WORKS_ON on Pnumber=Pno group by Pno;
-- 5
\! echo "Q5____________________________________________________________";
SELECT Pnumber,Pname,COUNT(*) as Count from PROJECT inner join WORKS_ON on  Pnumber=Pno and PROJECT.Dnum=5 group by Pno;
-- 6
\! echo "Q6____________________________________________________________";
SELECT Pnumber,Dnum,Lname,Address from PROJECT inner join DEPARTMENT on Dnum=Dnumber inner join EMPLOYEE on Mgr_ssn=ssn where Plocation="Houston";
-- 7
\! echo "Q7____________________________________________________________";
SELECT ssn,Pno,Hours from EMPLOYEE inner join WORKS_ON on ssn=Essn order by Dno,Fname,Lname;
-- 8
\! echo "Q8____________________________________________________________";
SELECT Fname from EMPLOYEE where Super_ssn is NOT NULL;
-- 9
\! echo "Q9____________________________________________________________";
SELECT Fname from EMPLOYEE where Super_ssn in (SELECT ssn from EMPLOYEE where Super_ssn=987654321);
-- 10 
\! echo "Q10___________________________________________________________";
select Dname, Fname, Salary from EMPLOYEE inner join DEPARTMENT on ssn=Mgr_ssn;
-- 11
\! echo "Q11___________________________________________________________";
select Fname as name, (select Fname from EMPLOYEE where ssn=(select super_ssn from EMPLOYEE where Fname=name)) as "emp", Salary from EMPLOYEE inner join DEPARTMENT on Dno = Dnumber where Dname="Research";
-- 12
\! echo "Q12___________________________________________________________";
select Pname,Dname, (select COUNT(*) from WORKS_ON where Pno=Pnumber) as Count, (select COUNT(Hours) from WORKS_ON where Pno=Pnumber) as Hours from PROJECT inner join DEPARTMENT on Dnum=Dnumber;
-- 13
\! echo "Q13___________________________________________________________";
select Pname, Dname, (select COUNT(*) from WORKS_ON where Pno=Pnumber) as Count, (select COUNT(Hours) from WORKS_ON where Pno=Pnumber) as Hours from PROJECT inner join DEPARTMENT on Dnum=Dnumber where (select COUNT(*) from WORKS_ON where Pno=Pnumber)>1;
-- 14
\! echo "Q14___________________________________________________________";
select Fname from EMPLOYEE where ssn in (select Essn from WORKS_ON inner join PROJECT on Pnumber=Pno and Dnum=5);
-- 15
\! echo "Q15___________________________________________________________";
select Fname from EMPLOYEE where ssn in (select Essn from WORKS_ON inner join PROJECT  on Pnumber=Pno where Pname="ProductX" and Hours>10);
-- 16
\! echo "Q16___________________________________________________________";
select Fname from EMPLOYEE inner join DEPENDENT on ssn=Essn where Fname = Dependent_name;
-- 17
\! echo "Q17___________________________________________________________";
select Fname from EMPLOYEE where super_ssn=(select ssn from EMPLOYEE where Fname="Franklin" and Lname="Wong");
-- 18 
\! echo "Q18___________________________________________________________";
select Pname, SUM(Hours) from PROJECT inner join WORKS_ON on Pnumber=Pno group by Pno;
-- 19
\! echo "Q19___________________________________________________________";
select AVG(Salary) from EMPLOYEE where sex="F";




