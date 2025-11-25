--  CRUD 실습 위한 CREATE TABLE DDL
CREATE TABLE IF NOT EXISTS todo (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            item VARCHAR(255) NOT NULL
        )

INSERT INTO todo (item)
VALUES ('Learn SQL'), ('Build a REST API'), ('Write Unit Tests');

SELECT id , item
FROM todo;

SELECT id , item
FROM todo
WHERE id = '65a8a77d-415d-47eb-b149-e0589100e2ac';

UPDATE todo
SET item = 'learn Advanced SQL'
WHERE id = '47c7adef-dc75-48d6-b705-10b6c035d728';

DELETE FROM todo
WHERE id = '0bf21a4b-836e-42b8-b9c1-35b5b084fe76';
