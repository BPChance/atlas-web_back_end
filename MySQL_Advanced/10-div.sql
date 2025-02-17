-- creates function SafeDiv that divides (and returns) first by
-- the second number or returns 0 if second number is equal to 0
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END //

DELIMITER ;
