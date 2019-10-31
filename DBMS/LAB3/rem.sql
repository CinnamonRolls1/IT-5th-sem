-- 4 --
DROP PROCEDURE IF EXISTS ufn_CalculateFutureValue;
DELIMITER //
CREATE PROCEDURE ufn_CalculateFutureValue (
    IN sum INT,
    IN rate FLOAT,
    IN years INT,
    OUT amount FLOAT
)
BEGIN
 SET amount = sum * POWER(1+rate,years);
END//
DELIMITER ;
CALL ufn_CalculateFutureValue(1000, 0.1, 5, @amount);
SELECT @amount;

-- 5 --
DROP PROCEDURE IF EXISTS usp_get_employees_with_department;
DELIMITER //
CREATE PROCEDURE usp_get_employees_with_department (
    IN department INT,
    OUT list TEXT
)
BEGIN
    DECLARE sname VARCHAR(300) DEFAULT "";
    DECLARE done INT DEFAULT 0;
    DECLARE name_list VARCHAR(4000) DEFAULT "";
    DECLARE list_all_employees CURSOR FOR 
    SELECT fname
    FROM 
        EMPLOYEE
    WHERE
        dno = department;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN list_all_employees;
    get_list: LOOP
        FETCH list_all_employees INTO sname;
        IF done = 1 THEN
            LEAVE get_list;
        END IF;
        SET name_list = CONCAT(sname,";",name_list);
    END LOOP get_list;
    SET list=name_list;
    CLOSE list_all_employees;
END//
DELIMITER ;
CALL usp_get_employees_with_department(8,@name_list);  
SELECT @name_list;

-- 6 --
DROP PROCEDURE IF EXISTS update_salary;
DELIMITER //
CREATE PROCEDURE update_salary()
BEGIN
    DECLARE sal INT DEFAULT 0;
    DECLARE essn INT DEFAULT 0;
    DECLARE done INT DEFAULT 0;
    DECLARE query VARCHAR(4000) DEFAULT "";
    DECLARE levels INT DEFAULT 0;
    DECLARE list_all_employees CURSOR FOR 
    SELECT salary,ssn
    FROM 
        EMPLOYEE;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN list_all_employees;
    get_list: LOOP
        SET levels = 0;
        FETCH list_all_employees INTO sal,essn;
        IF done = 1 THEN
            LEAVE get_list;
        END IF;
        IF sal < 30000 THEN
            SET levels = sal+10000;
        END IF;
        IF sal>30000 AND sal <= 50000 THEN
            SET levels = sal+20000;
        END IF;
        IF sal > 50000 THEN
            SET levels = sal+30000;
        END IF;
        SET @query = CONCAT(
            'UPDATE EMPLOYEE SET salary=',levels,
            ' WHERE ssn=',essn,';');
        PREPARE stmt FROM @query;
        EXECUTE stmt;
    END LOOP get_list;
    CLOSE list_all_employees;
END//
DELIMITER ;
CALL update_salary();
SELECT ssn,salary FROM EMPLOYEE;