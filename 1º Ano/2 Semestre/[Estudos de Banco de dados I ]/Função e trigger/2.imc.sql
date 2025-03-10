CREATE TABLE CLIENT_IMC(
     ID INTEGER,
     WEIGHT NUMBER(*, 2),
     HEIGHT NUMBER(*,2)
);

CREATE TABLE IMC(
     ID INTEGER,
     IMC NUMBER(*, 2)
)

CREATE OR REPLACE FUNCTION CALCULATE_IMC (WEIGHT NUMBER, HEIGHT NUMBER) RETURN NUMBER IS IMC NUMBER;
BEGIN
     IMC := WEIGHT/(HEIGHT*HEIGHT);
     RETURN IMC;
END CALCULATE_IMC;

INSERT INTO CLIENT_IMC (ID, WEIGHT, HEIGHT) VALUES (1, 105, 1.80);
INSERT INTO CLIENT_IMC (ID, WEIGHT, HEIGHT) VALUES (2, 67.90, 1.78);
INSERT INTO CLIENT_IMC (ID, WEIGHT, HEIGHT) VALUES (3, 87.00, 1.80);

INSERT INTO IMC(ID, IMC)
SELECT ID, CALCULATE_IMC(WEIGHT, HEIGHT) AS IMC
FROM CLIENT_IMC;

SELECT * FROM CLIENT_IMC;
SELECT * FROM IMC;