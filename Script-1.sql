create
database parsdata;

USE
parsdata;
CREATE SCHEMA limoo;

DROP TABLE IF EXISTS parsdata.limoo.users;
CREATE TABLE parsdata.limoo.users
(
    id         int         NOT NULL PRIMARY KEY IDENTITY(1,1),
    msisdn     varchar(12) NOT NULL UNIQUE,
    first_name varchar(50) NULL,
    last_name  varchar(50) NULL,
    avatar     varchar(50) NULL,
    created_at datetime    NOT NULL,
);


USE
parsdata;
DROP PROCEDURE IF EXISTS limoo.find_user_by_msisdn;
CREATE PROCEDURE limoo.find_user_by_msisdn @msisdn varchar(12)
AS
SELECT *
FROM parsdata.limoo.users u
WHERE u.msisdn = @msisdn;

DROP PROCEDURE IF EXISTS limoo.find_user_by_id;
CREATE PROCEDURE limoo.find_user_by_id @id int
AS
SELECT *
FROM parsdata.limoo.users u
WHERE u.id = @id;
FROM  WHERE u.id  = @id;


DROP PROCEDURE IF EXISTS limoo.update_first_name_last_name_by_id;
CREATE PROCEDURE limoo.update_first_name_last_name_by_id @id int,
    @first_name  varchar(50),
    @last_name varchar(50)
AS
UPDATE parsdata.limoo.users
SET first_name = @first_name,
    last_name  = @last_name
WHERE id = @id;



