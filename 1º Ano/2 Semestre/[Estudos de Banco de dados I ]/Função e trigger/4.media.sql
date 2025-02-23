CREATE TABLE ALUNOS(  
     NOTA1 NUMBER(10,2), 
     NOTA2 NUMBER(10,2), 
     MEDIA NUMBER(10,2) 
); 

CREATE OR REPLACE FUNCTION CALCULAR_MEDIA(NOTA1 NUMBER, NOTA2 NUMBER) RETURN NUMBER IS MEDIA NUMBER; 
BEGIN 
     MEDIA := (NOTA1 + NOTA2)/2; 
     RETURN MEDIA; 
END CALCULAR_MEDIA; 

CREATE OR REPLACE TRIGGER MEDIA BEFORE INSERT OR UPDATE ON ALUNOS 
FOR EACH ROW 
BEGIN 
     :NEW.MEDIA := CALCULAR_MEDIA(:NEW.NOTA1, :NEW.NOTA2); 
END; 

INSERT INTO ALUNOS (NOTA1, NOTA2) VALUES (5.0, 9.0); 
INSERT INTO ALUNOS (NOTA1, NOTA2) VALUES (6.0, 7.5); 
INSERT INTO ALUNOS (NOTA1, NOTA2) VALUES (9.0, 7.5); 

SELECT * FROM ALUNOS;