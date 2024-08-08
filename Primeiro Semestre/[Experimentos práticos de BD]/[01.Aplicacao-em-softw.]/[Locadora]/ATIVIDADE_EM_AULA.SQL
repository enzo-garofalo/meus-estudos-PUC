SELECT * FROM DVD_CLIENTE;
SELECT * FROM DVD_GENERO;
SELECT * FROM DVD_FILMES;
SELECT * FROM DVD_ALUGUEL;

-- 1)Qual o nome e gênero dos DVDs disponíveis?
SELECT f.NOME, g.DESCRICAO AS "Gênero"
FROM DVD_FILMES f
JOIN DVD_GENERO g ON f.ID_GENERO = g.ID_GENERO;

-- 2)Quais são os gêneros dos DVDs disponíveis? 
-- Não repetir o dado
SELECT DISTINCT G.DESCRICAO
FROM DVD_FILMES F
JOIN DVD_GENERO G on F.ID_GENERO = G.ID_GENERO;

-- 3)Quantos  DVD  de  cada  gênero  há  na  locadora?  
-- Exiba  o  nome  do  gênero  junto  com  a contagem.
SELECT G.DESCRICAO, COUNT(*) AS "Quantidade em Estoque"
FROM DVD_FILMES F
JOIN DVD_GENERO G on F.ID_GENERO = G.ID_GENERO
GROUP BY G.DESCRICAO;

-- 4)Qual  o  nome  de  cada  cliente  que  alugou  algum  DVD?  
-- Exiba  os  nomes  em  ordem alfabética sem repeti-los.
SELECT DISTINCT cliente.NOME
FROM DVD_ALUGUEL al
JOIN DVD_CLIENTE cliente ON al.ID_CLIENTE = cliente.ID_CLIENTE
ORDER BY cliente.NOME;

-- 5)Quantos reais cada cliente que alugou algum DVD gastou no total?
SELECT cliente.NOME, SUM(al.VALOR)
FROM DVD_ALUGUEL al
JOIN DVD_CLIENTE cliente ON al.ID_CLIENTE = cliente.ID_CLIENTE
GROUP BY cliente.NOME
ORDER BY cliente.NOME;

-- 6)Quais os gêneros dos DVDs que já foram alugados alguma vez? Não repetir o dado
SELECT DISTINCT G.DESCRICAO
FROM DVD_ALUGUEL AL 
JOIN DVD_FILMES F ON AL.ID_DVD = F.ID_DVD
JOIN DVD_GENERO G ON F.ID_GENERO = G.ID_GENERO;

-- 7)Qual a data de nascimento e o gênero do cliente que alugou o DVD TITAMIC?
SELECT CLI.NOME, CLI.DATA_NASC, CLI.SEXO, F.NOME
FROM DVD_ALUGUEL AL 
JOIN DVD_CLIENTE CLI ON CLI.ID_CLIENTE = AL.ID_CLIENTE
JOIN DVD_FILMES F  ON F.ID_DVD = AL.ID_DVD
WHERE F.NOME = 'Titanic';

-- 8)Qual o nome do DVD e o gênero do filme que cada cliente alugou? 
-- Exiba os resultados em ordem alfabética do nome do cliente.
SELECT CLI.NOME, F.NOME, G.DESCRICAO
FROM DVD_ALUGUEL AL
JOIN DVD_CLIENTE CLI ON CLI.ID_CLIENTE = AL.ID_CLIENTE
JOIN DVD_FILMES F  ON F.ID_DVD = AL.ID_DVD
JOIN DVD_GENERO G ON F.ID_GENERO = G.ID_GENERO
ORDER BY CLI.NOME;
