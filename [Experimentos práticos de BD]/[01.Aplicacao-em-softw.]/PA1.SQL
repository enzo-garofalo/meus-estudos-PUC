-- 1) Defina as tabelas a partir dos esquemas a seguir:
CREATE TABLE EDITORAS
(
    id_editora NUMBER(3) NOT NULL PRIMARY KEY,
    nome_editora VARCHAR2(30) NOT NULL,
    cidade_editora VARCHAR2(30),
    fone_editora VARCHAR2(30)
)
CREATE TABLE AUTORES
(
    id_autor NUMBER(5) NOT NULL PRIMARY KEY,
    nome_autor VARCHAR2(30) NOT NULL,
    data_nasc DATE,
    cidade_nasc VARCHAR2(30)
)
CREATE TABLE LIVROS
(
    isbn NUMBER(5) NOT NULL PRIMARY KEY,
    titulo VARCHAR2(50) NOT NULL,
    id_editora NUMBER(3) NOT NULL,
    CONSTRAINT fk_id_editora FOREIGN KEY (id_editora) REFERENCES EDITORAS (id_editora),
    valor NUMBER(5,2) NOT NULL,
    num_paginas NUMBER(4),
    id_autor NUMBER(5),
    CONSTRAINT fk_id_autor FOREIGN KEY (id_autor) REFERENCES AUTORES (id_autor)   
)
-- 2) Alterar o campo fone_editora na tabela Editoras para o tipo number(8). 
ALTER TABLE EDITORAS MODIFY fone_editora NUMBER(8);
-- 3) Adicionar o campo estado_editora do tipo varchar2(15) na tabela Editoras.
ALTER TABLE EDITORAS ADD estado_editora VARCHAR2(15);
-- 4) Remover o campo cidade_nasc da tabela Autores.
ALTER TABLE AUTORES DROP COLUMN cidade_nasc;

-- 5) Execute as seguinte linhas no SQLDeveloper (copiar, colar e executar):
INSERT INTO Editoras(id_editora, nome_editora, cidade_editora, fone_editora, estado_editora) VALUES (1, 'Cia das Letras','São Paulo', 77887879,'São Paulo');
INSERT INTO Editoras(id_editora, nome_editora, cidade_editora, fone_editora, estado_editora) VALUES (2, 'Contemporânea','Petrópolis',66333565,'Rio de Janeiro');
INSERT INTO Editoras(id_editora, nome_editora, cidade_editora, fone_editora, estado_editora) VALUES (3, 'ABC','Campinas',45459696,'São Paulo');
INSERT INTO Editoras(id_editora, nome_editora, cidade_editora, fone_editora, estado_editora) VALUES (4, 'Leitura Tech','Campinas',78129656,'São Paulo');
INSERT INTO Editoras(id_editora, nome_editora, cidade_editora, fone_editora, estado_editora) VALUES (5, 'Modernity','Belo Horizonte',12126356,'Minas Gerais');
INSERT INTO Editoras(id_editora, nome_editora, cidade_editora, fone_editora, estado_editora) VALUES (6, 'Caminho do Aprendizado','Curitiba',33665589,'Paraná');

INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (1, 'João Paulo', TO_DATE('15/02/1949', 'DD/MM/YYYY')); 
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (2, 'Ana Maria Martins', TO_DATE('18/04/1988', 'DD/MM/YYYY'));
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (3, 'Pedro Raimundo', TO_DATE('12/02/1948', 'DD/MM/YYYY')); 
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (4, 'José de Alencar Martins', TO_DATE('25/10/1950', 'DD/MM/YYYY'));
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (5, 'Tatiane Ribeiro', TO_DATE('12/12/1975', 'DD/MM/YYYY'));
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (6, 'Paulo Proença', TO_DATE('28/03/1962', 'DD/MM/YYYY'));
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (7, 'Joaquim Machado', TO_DATE('30/06/1949', 'DD/MM/YYYY')); 
INSERT INTO AUTORES(id_autor, nome_autor, data_nasc) VALUES (8, 'Flavia Mirante', TO_DATE('12/10/1980', 'DD/MM/YYYY'));

INSERT INTO Livros (isbn, titulo, id_editora, valor, num_paginas, id_autor) VALUES (9788533308873, 'Banco de Dados para Midias Digitais', 6, 150.00, 386, 5);
INSERT INTO Livros (isbn, titulo, id_editora, valor, num_paginas, id_autor) VALUES (5777533302083, 'A arte de definir banco de dados',1, 63, 33, 8); 
INSERT INTO Livros (isbn, titulo, id_editora, valor, num_paginas, id_autor) VALUES (6688533309987, 'Banco de dados: guia prático e introdutorio', 1, 75.50, 45, 2); 
INSERT INTO Livros (isbn, titulo, id_editora, valor, num_paginas, id_autor) VALUES (8588533878873, 'Álgebra Relacional para BD', 2, 100.00, 150, 4);
INSERT INTO Livros (isbn, titulo, id_editora, valor, num_paginas, id_autor) VALUES (9788536908873, 'Banco de dados Não Relacional', 5, 68.29, 40, 6);