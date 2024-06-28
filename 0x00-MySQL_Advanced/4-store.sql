-- trig
DELIMITER $$
CREATE TRIGGER sell
AFTER INSERT 
ON orders FOR EACH ROW
BEGIN
	UPDATE items
	set NEW.items.quantity = items.quantity - number
	WHERE name = item_name;
END $$
