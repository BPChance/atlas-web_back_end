-- script that creates a trigger that decreases the quantity of an item after adding a new order
DROP TRIGGER IF EXISTS  decrease_quantity;
CREATE TRIGGER decrease_quantity
AFTER EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
