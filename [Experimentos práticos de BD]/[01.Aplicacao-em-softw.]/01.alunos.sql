 CREATE TABLE alunos 
( 
    RA number (8) NOT NULL PRIMARY KEY, 
    nome VARCHAR2(50), 
    idade number (2), 
    cidade VARCHAR2(50), 
    estado VARCHAR(50)
)  
ALTER TABLE alunos MODIFY nome NOT NULL;
ALTER TABLE alunos MODIFY idade NOT NULL;
ALTER TABLE alunos MODIFY cidade NOT NULL;

INSERT INTO alunos (RA, nome, idade, cidade, estado) 
    VALUES (24008914, 'Enzo Garofalo', 20, 'Hortolândia', 'São Paulo')

INSERT INTO alunos (RA, nome, idade, cidade, estado)
	VALUES (21010698, 'Pedro Daou', 25, 'Campinas', 'São Paulo')

UPDATE alunos
    SET nome = 'Fernandinho Abacates'
    WHERE ra = 24008914

DELETE FROM alunos
    WHERE ra = 21010698 
    
UPDATE alunos
    SET nome = 'Wandinho da Rua 7'
    WHERE ra = 21010698
    
SELECT * FROM alunos