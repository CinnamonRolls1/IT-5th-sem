-- 1 --
DROP PROCEDURE IF EXISTS usp_get_employees_salary_above;
DELIMITER //
CREATE PROCEDURE usp_get_employees_salary_above (
    IN sal INT
)
BEGIN
    SELECT fname,lname FROM EMPLOYEE
    WHERE
        salary >= sal
    ORDER BY
        fname ASC,
        lname ASC;
END//
DELIMITER ;
CALL usp_get_employees_salary_above (48100);

-- 2 --
DROP PROCEDURE IF EXISTS usp_get_towns_starting_with;
DELIMITER //
CREATE PROCEDURE usp_get_towns_starting_with (
    IN town TEXT
)
BEGIN
    SELECT dlocation FROM DEPT_LOCATIONS
    WHERE
        dlocation LIKE CONCAT(town,'%');
END//
DELIMITER ;
CALL usp_get_towns_starting_with ('S');

-- 3 --
DROP PROCEDURE IF EXISTS ufn_get_salary_level;
DELIMITER //
CREATE PROCEDURE ufn_get_salary_level (
    IN sal INT,
    OUT SalLevel TEXT
)
BEGIN
    IF sal < 30000 THEN
        SET SalLevel = 'Low';
    END IF;
    IF sal>30000 AND sal <= 50000 THEN
        SET SalLevel = 'Average';
    END IF;
    IF sal > 50000 THEN
        SET SalLevel = 'High';
    END IF;
END//
DELIMITER ;
CALL ufn_get_salary_level(35000, @SalLevel);
SELECT @SalLevel;

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


