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

    -- casual
    -- cold weather based in F
    INSERT INTO Clothing values (000, 'Bundle up!', 32, 0)
    INSERT INTO Clothing values (001, 'Dont forget your hat', 45, 0)
    INSERT INTO Clothing values (002, 'Grab a warm jacket', 50, 0)
    INSERT INTO Clothing values (003, 'Grab a jacket but no hat needed today!', 60, 0)
    -- warm weather
    INSERT INTO Clothing values (020, 'Light jacket!', 70, 0)
    INSERT INTO Clothing values (021, 'No jacket during the day, maybe one at night', 80,0)
    INSERT INTO Clothing values (022, 'No jacket today and dress cooly', 90, 0)
    INSERT INTO Clothing values (023, 'Drink water today, its hot', 100, 0)
    INSERT INTO Clothing values (024, 'Why would you go outside', 150, 0)
    INSERT INTO Clothing values (025, 'Something is wrong', 200, 0)

    -- formal
    -- cold weather based in F
    INSERT INTO Clothing values (100, 'Bundle up! Dont be afraid to layer a thick jacket on top of formal wear', 32, 1)
    INSERT INTO Clothing values (101, 'Dont forget your hat! A nice hat will pair nicely with formal attire', 45, 1)
    INSERT INTO Clothing values (102, 'Grab a warm jacket over formal wear', 50, 1)
    INSERT INTO Clothing values (103, 'Grab a thicker jacket but no hat needed today!', 60, 1)
    -- warm weather
    INSERT INTO Clothing values (120, 'A sweater or blazer will do!', 70, 1)
    INSERT INTO Clothing values (121, 'No extra layer needed during the day, maybe one at night', 80,1)
    INSERT INTO Clothing values (122, 'Bring out your lightest formal wear', 90, 1)
    INSERT INTO Clothing values (123, 'Consider bringing water with your formal wear', 100, 1)
    INSERT INTO Clothing values (124, 'You should cancel your event', 150, 1)
    INSERT INTO Clothing values (125, 'No', 200, 1)


    -- special weather statements
