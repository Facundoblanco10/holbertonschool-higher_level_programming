-- script that creates the table unique_id on your MySQL server.
-- task5
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL UNIQUE, name VARCHAR(256));
INSERT INTO unique_id (1)
