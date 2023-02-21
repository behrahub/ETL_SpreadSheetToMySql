use db;

CREATE TABLE People(
      ID int not null AUTO_INCREMENT,
      FirstName varchar(100) NOT NULL,
      LastName varchar(100) NOT NULL,
      Email varchar(100) NOT NULL,
      Gender varchar(100) NOT NULL,
      IPAddress varchar(100) NOT NULL,
      PRIMARY KEY (ID)
);



