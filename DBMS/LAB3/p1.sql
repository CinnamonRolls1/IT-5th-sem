DELIMITER //
CREATE PROCEDURE usp_GetEmployeesSalaryAbove(IN num INT)
BEGIN	 
SELECT fname,lname 
	   FROM EMPLOYEE 
	  WHERE  Salary >= num;
END//
DELIMITER ;
call usp_GetEmployeesSalaryAbove(48100);

DELIMITER //
CREATE PROCEDURE ufn_GetSalaryLevel(IN Salary INT,OUT SalaryLevel VARCHAR(10)) 
BEGIN 
	IF(Salary < 30000) THEN  
	 SET SalaryLevel = 'Low';
    END IF;
	IF(Salary >= 30000 AND Salary <= 50000) THEN
	 SET SalaryLevel = 'Average';
    ELSE
	 SET SalaryLevel = 'High';
    END IF;
END//
DELIMITER ;
call ufn_GetSalaryLevel(35000, @out);
select @out;