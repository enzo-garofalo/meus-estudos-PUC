CREATE TABLE CURRENCY (
     ID INTEGER,
     REAL NUMBER(*,2),
     DOLAR NUMBER(*,2)
);

CREATE OR REPLACE FUNCTION REAL_TO_DOLAR (REAL NUMBER) RETURN NUMBER IS DOLAR NUMBER;
BEGIN
     DOLAR := REAL * 5.77;
     RETURN DOLAR;
END REAL_TO_DOLAR;

CREATE TABLE REAL_VALUES(
     ID INTEGER,
     REAL NUMBER(*,2)
);

INSERT INTO REAL_VALUES (ID, REAL) VALUES (1, 10);
INSERT INTO REAL_VALUES (ID, REAL) VALUES (2, 15);
INSERT INTO REAL_VALUES (ID, REAL) VALUES (3, 20);

INSERT INTO CURRENCY (ID, REAL, DOLAR)
SELECT ID, REAL, REAL_TO_DOLAR(REAL) AS DOLAR
FROM REAL_VALUES;

SELECT * FROM CURRENCY;