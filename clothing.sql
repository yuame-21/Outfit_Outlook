-- USE means that we are referencing this current database
USE recommendations;

-- CREATE TABLE : we are going to make one sql table with a few columns that will
    -- help us indicate what query is right
CREATE TABLE Clothing(
    clothingID varchar(255) PRIMARY KEY , -- PK = how to distinguish each data piece
    description varchar(255),
    tempReq int, -- temp needed to use this piece of clothing
    conditions int; -- the additional conditions of a piece of clothing?
)

-- creating instance of database

    -- cold weather based in F
    INSERT INTO Clothing values (100, 'Bundle up!', 32, 0)
    INSERT INTO Clothing values (101, 'Dont forget your hat', 45, 0)
    INSERT INTO Clothing values (102, 'Grab a warm jacket', 50, 0)
    INSERT INTO Clothing values (103, 'Grab a jacket but no hat needed today!', 60, 0)
    -- warm weather
    INSERT INTO Clothing values (200, 'Light jacket!', 70, 0)
    INSERT INTO Clothing values (201, 'No jacket during the day, maybe one at night', 80,0)
    INSERT INTO Clothing values (202, 'No jacket today and dress cooly', 90, 0)
    INSERT INTO Clothing values (203, 'Drink water today, its hot', 100, 0)
    INSERT INTO Clothing values (204, 'Why would you go outside', 150, 0)
    INSERT INTO Clothing values (205, 'Something is wrong', 200, 0)
    -- special weather statements
    INSERT INTO Clothing values (001, 'wear a mask today to protect your lungs', 700, 1)
