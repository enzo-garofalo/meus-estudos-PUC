Create table exe_livros ( 
    Isbn number(17), 
    Titulo varchar2(50) not null, 
    NumPaginas number(4) not null, 
    Edicao number(2) not null, 
    Genero varchar2(20), 
    Idioma varchar2(15) not null,  
    Ano_publicacao number (4) not null, 
    Valor number (5,2) not null, 
    Editora varchar2(30)not null, 
    Cidade_editora varchar2(30), 
    Autor varchar2(30) not null, 
    Cidade_autor varchar2(30), 
    Constraint pk_isbn_livros primary key (isbn) 
); 


INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (9780862446864, 'Alabarme a mí mismo', 414, 3, 'autoajuda', 'Espanhol', 2020, 45.54, 'Primeshow', 'Barcelona', 'Isabel Sanchez', 'Múrcia');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2666230800748, 'creciendo bajo el sol', 548, 1, 'autoajuda', 'Espanhol', 2018, 60.28, 'Voltnamfan', 'Madrid', 'Laur Perez', 'Sevilha');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8792067819450, 'O Desafio das Montanhas', 520, 2, 'mistério', 'Português', 2007, 57.2, 'Leitramor', 'Rio de Janeiro', 'Andreia Queiroz', 'Belo Horizonte');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1138148089330, 'Signes du brouillard', 263, 2, 'terror', 'Francês', 2016, 28.93, 'Étoile du Griffon', 'Paris', 'Delight Filiatrault', 'Paris');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5224149118728, 'Still Breathing In The Commander\xa0', 422, 2, 'ficção científica', 'Inglês', 2000, 46.42, 'Primebit', 'Las Vegas', 'Warren Hines', 'Washington');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5483156887702, 'Todavía respirando en pesadillas', 95, 3, 'ficção científica', 'Espanhol', 2002, 10.45, 'Primeshow', 'Barcelona', 'Laur Perez', 'Sevilha');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5045846124746, 'Comer en el fuego', 381, 2, 'romance', 'Espanhol', 2014, 41.91, 'Nuevocon', 'Valência', 'Laur Perez', 'Sevilha');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (3431714146230, 'Além da Fronteira', 380, 2, 'mistério', 'Português', 2019, 41.8, 'Leitramor', 'Rio de Janeiro', 'Suzana Nascimento', 'São Paulo');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (9709730891073, 'Searching At The End\xa0', 537, 2, 'autoajuda', 'Inglês', 2007, 59.07, 'Boaraid', 'Ohio', 'Stuart Huerta', 'Houston');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4217242955429, 'Prepare For The Forest\xa0', 336, 2, 'biografia', 'Inglês', 2000, 36.96, 'Boaraid', 'Ohio', 'Sam Vincent', 'Houston');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (7873420106295, 'Tower Of The Void\xa0', 267, 1, 'terror', 'Inglês', 2004, 29.37, 'Tanfix', 'Ohio', 'Albert Gates', 'Londres');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4825908064766, 'Bataille du labyrinthe', 95, 2, 'aventura', 'Francês', 2023, 10.45, 'Bulltronique', 'Lyon', 'Delight Filiatrault', 'Lille');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6423076446180, 'Life At The Shadows', 381, 2, 'romance', 'Inglês', 2002, 41.91, 'Tanfix', 'Ohio', 'Anastasia Powell', 'Las Vegas');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2514870275756, 'Le défi de lempereur', 549, 3, 'autoajuda', 'Francês', 2015, 60.39, 'Maison naine', 'Marselha', 'Matilde Lhommedieu', 'Paris');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6830658794901, 'Saccrocher au sud', 348, 2, 'fantasia', 'Francês', 2023, 38.28, 'Bulltronique', 'Lyon', 'Cadencia Lesieur', 'Bordeaux');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4647431334465, 'Perdiendo mi final', 177, 2, 'fantasia', 'Espanhol', 2009, 19.47, 'Nuevocon', 'Valência', 'José González', 'Madrid');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4482819331954, 'Sanando el abismo', 143, 1, 'aventura', 'Espanhol', 2005, 15.73, 'Voltnamfan', 'Madrid', 'Manuel Rodriguez', 'Barcelona');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5263533175825, 'Pistas do Passado', 154, 1, 'romance', 'Português', 2018, 16.94, 'Leiturama', 'São Paulo', 'Suzana Nascimento', 'São Paulo');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (7673732309469, 'Symbols In The Maze', 176, 3, 'terror', 'Inglês', 1998, 19.36, 'Wavepaw', 'Los Angeles', 'Tricia Juarez', 'Ohio');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6269957152542, 'Starting The Town\xa0', 169, 3, 'romance', 'Inglês', 2015, 18.59, 'Wavepaw', 'Los Angeles', 'Albert Gates', 'Londres');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1255798057897, 'O Mistério das Ruínas Antigas', 183, 1, 'aventura', 'Português', 2023, 20.13, 'Leiturama', 'São Paulo', 'Brian Peres', 'Campinas');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8348116636769, 'O Tesouro das Profundezas', 256, 2, 'mistério', 'Português', 2004, 28.16, 'Paginéx', 'Belo Horizonte', 'Lucília Rebelo', 'Brasília');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (7268288676797, 'Na Rota do Desafio', 402, 2, 'terror', 'Português', 2000, 44.22, 'Leitramor', 'Rio de Janeiro', 'Tereza Albuquerque', 'Rio de Janeiro');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4568640980779, 'Sangre en la oscuridad', 461, 2, 'romance', 'Espanhol', 2007, 50.71, 'Luz de tifón', 'Valência', 'Laur Perez', 'Sevilha');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8747414847139, 'Escaping The End\xa0', 381, 1, 'terror', 'Inglês', 2008, 41.91, 'Arcanehive', 'Nova Iorque', 'Cory Carney', 'Los Angeles');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1633516481380, 'Rumo ao Desconhecido', 380, 1, 'romance', 'Português', 2017, 41.8, 'Leitouro', 'Rio de Janeiro', 'Cristiano Miranda', 'Curtiba');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6141876879000, 'Jornada Além do Mapa', 264, 3, 'fantasia', 'Português', 2005, 29.04, 'Quadworks', 'Sintra', 'Maximino Salgado', 'São Paulo');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8929580303107, 'O Despertar da Expedição', 355, 3, 'romance', 'Português', 2014, 39.05, 'Arcanegate', 'Fátima', 'Bernardino Pereira', 'Londrina');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2720365704266, 'Écrire sur les ténèbres', 547, 3, 'fantasia', 'Francês', 1999, 60.17, 'Homme alligator', 'Marselha', 'Jeremie Lebleu', 'Marselha');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4341068941601, 'Searching At The Void', 158, 2, 'autoajuda', 'Inglês', 1999, 17.38, 'Woodlife', 'Nova Iorque', 'Kerry Mercer', 'Nova Iorque');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8075705708294, 'Whispers Of History', 326, 1, 'aventura', 'Inglês', 2012, 35.86, 'Boaraid', 'Ohio', 'Tara West', 'Los Angeles');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6316126101711, 'Segredos do Horizonte', 113, 3, 'romance', 'Português', 2016, 12.43, 'Transtone', 'Porto', 'Maximino Salgado', 'São Paulo');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1410399749274, 'Arriver au labyrinthe', 286, 2, 'ficção científica', 'Francês', 2012, 31.46, 'Bulltronique', 'Lyon', 'Marlon Juneau', 'Lyon');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6280608887234, 'Trilhas do Desconhecido', 106, 3, 'fantasia', 'Português', 2002, 11.66, 'konplus', 'Porto', 'Diogo Abril', 'Petrópolis');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (9244690152355, 'O Legado do Explorador', 492, 1, 'ficção científica', 'Português', 2003, 54.12, 'Paginéx', 'Belo Horizonte', 'Marcos Lobo', 'Rio de Janeiro');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5660186522870, 'Em Busca da Cidade Perdida', 101, 3, 'terror', 'Português', 2001, 11.11, 'Versila', 'Curitiba', 'Branca Gonçalves', 'Porto Alegre');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1024043794472, 'Bienvenue dans la jungle', 371, 3, 'romance', 'Francês', 1998, 40.81, 'Bétahex', 'Paris', 'Madelon Tessier', 'Paris');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4697303455868, 'Aventuras do Horizonte', 404, 3, 'ficção científica', 'Português', 2007, 44.44, 'Escrivrox', 'São Paulo', 'Suzana Nascimento', 'São Paulo');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (7865317993449, 'Gritos al principio', 120, 3, 'romance', 'Espanhol', 1998, 13.2, 'Puente de agua', 'Barcelona', 'Isabel Sanchez', 'Múrcia');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1775321605882, 'Em Busca do Tesouro Perdido', 172, 1, 'ficção científica', 'Português', 2014, 18.92, 'Bigelectrics', 'Lisboa', 'Diogo Abril', 'Petrópolis');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (1146926204954, 'Rescue In Nightmares', 392, 3, 'romance', 'Inglês', 2002, 43.12, 'Primebit', 'Las Vegas', 'Anastasia Powell', 'Las Vegas');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4591071765340, 'Du sang aux secrets', 455, 3, 'terror', 'Francês', 2020, 50.05, 'Homme alligator', 'Marselha', 'Jeremie Lebleu', 'Marselha');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (3483816003226, 'O Enigma do Vale Oculto', 458, 3, 'aventura', 'Português', 1998, 50.38, 'Paginéx', 'Belo Horizonte', 'Andreia Queiroz', 'Belo Horizonte');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5717086105179, 'Faith Of My Future', 435, 1, 'aventura', 'Inglês', 1998, 47.85, 'Bluebar', 'Nova Iorque', 'Júlia Resendes', 'Ohio');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2868013374214, 'Ayudando a los sueños', 368, 3, 'fantasia', 'Espanhol', 2002, 40.48, 'Puente de agua', 'Barcelona', 'Maria Teresa Martin', 'Barcelona');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6045447770007, 'Caminhos Perdidos', 338, 3, 'aventura', 'Português', 2019, 37.18, 'Pixelshade', 'Lisboa', 'Anselmo Freitas', 'São Paulo');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (4557221025702, 'Criado por el principio', 239, 3, 'ficção científica', 'Espanhol', 2011, 26.29, 'Nuevocon', 'Valência', 'Maria Dolores Gomez', 'Múrcia');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6945346022982, 'Battle Of The Commander\xa0', 214, 3, 'mistério', 'Inglês', 2012, 23.54, 'Voidcloud', 'Lion', 'Albert Gates', 'Londres');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2852286587765, 'Evitar secretos', 265, 1, 'fantasia', 'Espanhol', 2015, 29.15, 'Primeshow', 'Barcelona', 'José González', 'Madrid');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8513293813946, 'Dead In The Fog\xa0', 175, 1, 'aventura', 'Inglês', 2001, 19.25, 'Bluebar', 'Nova Iorque', 'Moises Anthony', 'Chicago');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2452386482938, 'Cazado por los ángeles', 409, 2, 'fantasia', 'Espanhol', 2015, 44.99, 'Pétalosun', 'Madrid', 'Manuel Rodriguez', 'Barcelona');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (9756602610256, 'Perdiendo las sombras', 309, 3, 'aventura', 'Espanhol', 2017, 33.99, 'Pétalosun', 'Madrid', 'Maria Pilar Martinez', 'Madrid');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2023856133563, 'Bound To Nature\xa0', 378, 3, 'fantasia', 'Inglês', 2021, 41.58, 'Woodlife', 'Nova Iorque', 'Rigoberto Valdez', 'Madrid');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (3981944473091, 'Persiguiendo a Occidente', 221, 3, 'aventura', 'Espanhol', 2005, 24.31, 'Voltnamfan', 'Madrid', 'David Lopez', 'Barcelona');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (3254829215802, 'Welcome To The Light', 496, 3, 'aventura', 'Inglês', 2014, 54.56, 'Wavepaw', 'Los Angeles', 'Evangelina Barrera', 'Flórida');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6500120194075, 'Exploradores da Terra Proibida', 555, 2, 'romance', 'Português', 2007, 61.05, 'Leiturama', 'São Paulo', 'Adão do Rosário', 'Fortaleza');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (5670547985093, 'Sounds Of The King', 131, 2, 'fantasia', 'Inglês', 2006, 14.41, 'Woodlife', 'Nova Iorque', 'Patrica English', 'Nova Iorque');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6910517539370, 'Na Trilha da Coragem', 444, 2, 'ficção científica', 'Português', 2008, 48.84, 'Escrivrox', 'São Paulo', 'Júlia Resendes', 'Brasília');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6459288000899, 'Garder le pays', 440, 1, 'mistério', 'Francês', 2023, 48.4, 'Étoile du Griffon', 'Paris', 'Garon Lussier', 'Nice');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8793947618341, 'Crying In The Animals\xa0', 521, 3, 'mistério', 'Inglês', 2017, 57.31, 'Primebit', 'Las Vegas', 'Nelson Valenzuela', 'Cartagena');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2018109546366, 'Arriver à léternité', 472, 1, 'mistério', 'Francês', 2021, 51.92, 'Étoile du Griffon', 'Paris', 'Garon Lussier', 'Nice');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (8525446364516, 'Cazando el sol', 496, 1, 'aventura', 'Espanhol', 1999, 54.56, 'Luz de tifón', 'Valência', 'Javier Jimenez', 'Madrid');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (6464471186814, 'Dead At Secrets', 547, 2, 'ficção científica', 'Inglês', 2008, 60.17, 'Primebit', 'Las Vegas', 'Cassandra Newman', 'Washington');
INSERT INTO EXE_LIVROS (isbn, titulo, numPaginas, edicao, genero, idioma, ano_publicacao, valor, editora, cidade_editora, autor, cidade_autor) VALUES (2491972639650, 'Delaying The Immortals', 450, 2, 'mistério', 'Inglês', 2016, 49.5, 'Primebit', 'Las Vegas', 'Anastasia Powell', 'Las Vegas');

SELECT * FROM EXE_LIVROS;

-- 1) Quais os nomes dos livros?
SELECT DISTINCT TITULO FROM EXE_LIVROS;

-- 2) Quais são os livros de autoajuda?
SELECT DISTINCT TITULO, GENERO FROM EXE_LIVROS WHERE GENERO = 'autoajuda';

-- 3) Quais são os nomes dos autores presentes nessa base de dado? (não repetir o dado)
SELECT DISTINCT AUTOR FROM EXE_LIVROS;

-- 4) Quais as cidades dos autores que escreveram algum livro de romance? (não repetir  o dado)
SELECT DISTINCT AUTOR, GENERO FROM EXE_LIVROS WHERE GENERO = 'romance';

-- 5) Quais são as editoras cujos livros são em espanhol? (não repetir a informação) 
SELECT DISTINCT EDITORA, IDIOMA FROM EXE_LIVROS WHERE IDIOMA = 'Espanhol';

-- 6) Quais são os livros publicados entre os anos 2000 e 2010? 
SELECT * FROM EXE_LIVROS WHERE ANO_PUBLICACAO BETWEEN 2000 AND 2010;

-- 7) Quais  autores  publicaram  algum  livro  entre  os  anos  2020  e  2023?  (não repetir o dado)
SELECT DISTINCT TITULO, ANO_PUBLICACAO FROM EXE_LIVROS WHERE ANO_PUBLICACAO IN (2020, 2023); 

-- 8) Quais livros estão na segunda edição? 
SELECT DISTINCT TITULO, EDICAO FROM EXE_LIVROS WHERE EDICAO = 2;

-- 9) Quais  as  cidades  das  editoras  cujo  autores  escreveram  livros  em  Português  ou  Francês? (não repetir o dado)
SELECT DISTINCT TITULO, CIDADE_EDITORA FROM EXE_LIVROS WHERE IDIOMA IN ('Português', 'Francês'); 

-- 10)  Quais são os livros de terror, mistério ou ficção científica que possuem mais de 250  páginas e estão na segunda edição?
SELECT DISTINCT TITULO, GENERO, NUMPAGINAS, EDICAO FROM EXE_LIVROS WHERE GENERO IN ('terror', 'mistério', 'ficção científica') AND NUMPAGINAS > 250 AND EDICAO = 2; 
 
-- 11)  Quais os livros publicados antes do ano 2000 e depois de 2010? 
SELECT DISTINCT Titulo, ANO_PUBLICACAO FROM EXE_LIVROS WHERE ANO_PUBLICACAO < 2000 OR ANO_PUBLICACAO > 2010;

-- 12)  Quais são livros de fantasia publicados depois de 2005 e que são em Espanhol ou Inglês?
SELECT DISTINCT Titulo, GENERO, ANO_PUBLICACAO, IDIOMA FROM EXE_LIVROS WHERE ANO_PUBLICACAO > 2005 AND IDIOMA IN ('Espanhol', 'Inglês') AND GENERO = 'fantasia';
 
-- 13)  Quais os idiomas dos livros disponíveis na base de dados? (não repetir o dado) 
SELECT DISTINCT IDIOMA FROM EXE_LIVROS;

-- 14)  Quais são os livros cujo título começa com alguma letra entre H e P e que foram publicados entre os anos 1995 e 2005? 
SELECT TITULO, ANO_PUBLICACAO FROM EXE_LIVROS WHERE TITULO BETWEEN 'H' AND 'P' AND  ANO_PUBLICACAO BETWEEN 1995 AND 2005;

-- 15)  Quais são os gêneros dos livros que estão na terceira edição? (não repetir o dado) 
SELECT DISTINCT GENERO, EDICAO FROM EXE_LIVROS WHERE EDICAO = 3;