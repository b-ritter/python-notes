DROP TABLE IF EXISTS department;

CREATE TABLE department
(
    DepartmentID integer PRIMARY_KEY,
    DepartmentName text
);

DROP TABLE IF EXISTS employee;

CREATE TABLE employee
(
    LastName text,
    DepartmentID integer,
        FOREIGN KEY (DepartmentID) REFERENCES department(DepartmentID)
);

INSERT INTO department VALUES(31, 'Sales');
INSERT INTO department VALUES(33, 'Engineering');
INSERT INTO department VALUES(34, 'Clerical');
INSERT INTO department VALUES(35, 'Marketing');

INSERT INTO employee VALUES('Rafferty', 31);
INSERT INTO employee VALUES('Jones', 33);
INSERT INTO employee VALUES('Heisenberg', 33);
INSERT INTO employee VALUES('Robinson', 34);
INSERT INTO employee VALUES('Smith', 34);
INSERT INTO employee VALUES('Williams', NULL);