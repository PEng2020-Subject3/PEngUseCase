CREATE TABLE usecase (
    persID int PRIMARY KEY,
    typeID varchar (50) NOT NULL,
    speed int,
    performance int,
    speedev boolean,
    brakeev boolean,
    turnev boolean,
    crashev boolean,
    targetdate date NOT NULL
);

INSERT INTO usecase (persID, typeID, speed, performance, speedev, brakeev, turnev, crashev, targetdate) VALUES (666, 'prius', '33', '99', true, false, true, false, '1997-02-27')
