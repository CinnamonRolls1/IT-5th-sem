DROP TRIGGER IF EXISTS add_audit;
DELIMITER //

CREATE TRIGGER add_audit
AFTER INSERT ON blog
FOR EACH ROW
BEGIN
if (NEW.deleted = 0) then 
    insert into audit (blog_id, changetype) values (NEW.id, "NEW"); 
else 
    insert into audit (blog_id, changetype) values (NEW.id, "DELETE"); 
end if;
END //
DELIMITER ; 

DROP TRIGGER IF EXISTS edit_audit;
DELIMITER //

CREATE TRIGGER edit_audit
AFTER UPDATE ON blog
FOR EACH ROW
BEGIN
if (NEW.deleted = 0) then 
    insert into audit (blog_id, changetype) values (NEW.id, "EDIT"); 
else
    insert into audit (blog_id, changetype) values (NEW.id, "DELETE");
end if;
END //
DELIMITER ; 