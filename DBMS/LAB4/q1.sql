DROP TRIGGER IF EXISTS student_calc;
DELIMITER //

CREATE TRIGGER student_calc
BEFORE INSERT ON student_marks
FOR EACH ROW
BEGIN
SET NEW.total = NEW.sub1 + NEW.sub2 + NEW.sub3 + NEW.sub4 + NEW.sub5; 
SET NEW.per_marks = NEW.total / 5; 
if (NEW.per_marks >= 90) then 
    set NEW.grade = "EXCELLENT";
elseif (NEW.per_marks >= 75) then 
    set NEW.grade = "VERY GOOD";
elseif (NEW.per_marks >= 60) then 
    set NEW.grade = "GOOD" ;
elseif (NEW.per_marks >= 40) then
    set NEW.grade = "AVERAGE";
else set NEW.grade = "NOT PROMOTED";
end if; 
END //
DELIMITER ; 