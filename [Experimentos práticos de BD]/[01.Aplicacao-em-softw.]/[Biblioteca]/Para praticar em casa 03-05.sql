-- 1. Quantos livros foram publicados?
SELECT COUNT(ISBN) as "Quantidade de livros" FROM EXE_LIVROS;

-- 2. Quantos livros há em cada edição (1ª, 2º, 3º etc)? Ordene os resultados em ordem crescente do número da edição. 
-- Formate a saída da edição de acordo com o seguinte padrão: <edicao>a edição. Ex.: 3a edição. 
-- Ainda, altere o nome da coluna de saída com o número da edição para "Edição".
-- QUESTIONAR ESSA PARADA!!
SELECT TO_CHAR(EDICAO, 'FM99') || 'ª Edição' AS "Edição", COUNT(*) AS "Qtde de publicação" 
FROM EXE_LIVROS 
GROUP BY EDICAO
ORDER BY EDICAO;

-- 3. Quantos livros foram publicados em cada idioma?
SELECT IDIOMA, COUNT(IDIOMA) AS "Qtde de livros publicados"
FROM EXE_LIVROS 
GROUP BY IDIOMA;

-- 4. Quantos livros foram publicados em cada ano? Exiba apenas os anos que tiveram 3  ou  mais  publicações.  
-- Ordene  os  resultados  por  ordem  crescente  do  ano  de  publicação
SELECT ANO_PUBLICACAO, COUNT(*) 
FROM EXE_LIVROS 
GROUP BY ANO_PUBLICACAO 
HAVING COUNT(*) >= 3 
ORDER BY ANO_PUBLICACAO;

-- 5. Quantos livros cada editora publicou entre os anos 2000 e 2020?
SELECT EDITORA, COUNT(*)
FROM EXE_LIVROS
WHERE ANO_PUBLICACAO BETWEEN 2000 AND 2020
GROUP BY EDITORA;

-- 6. Quantos livros cada autor publicou? Ordene os autores em ordem alfabética.
SELECT AUTOR, COUNT(*)
FROM EXE_LIVROS
GROUP BY AUTOR
ORDER BY AUTOR;

-- 7. Qual o número médio de páginas dos livros publicado em Espanhol ou Português? 
-- Arredonde o resultado para que sejam exibido um valor inteiro. 
SELECT IDIOMA, ROUND(AVG(NUMPAGINAS)) AS "Média de Páginas" 
FROM EXE_LIVROS
GROUP BY IDIOMA
HAVING IDIOMA IN ('Espanhol', 'Português');

-- 8. Qual o número mínimo e o número máximo de páginas dos livros publicados por cada  editora?  
-- Ordene  as  editoras  em  ordem  alfabética.  
-- Exiba  os  resultados  das editoras cujo número mínimo foi maior do que 150, e o número máximo foi maior do que 300.
SELECT EDITORA, MAX(NUMPAGINAS), MIN(NUMPAGINAS)
FROM EXE_LIVROS
GROUP BY EDITORA
HAVING MIN(NUMPAGINAS) > 150 AND MAX(NUMPAGINAS) > 300
ORDER BY EDITORA;

-- 9. Quantos  livros  de  cada  gênero  foram  publicados  por  cada  editora?  
-- Ordene  as  editoras em ordem alfabética.
SELECT EDITORA, GENERO, COUNT(*)
FROM EXE_LIVROS
GROUP BY EDITORA, GENERO
ORDER BY EDITORA;

-- 10.  Qual o número mínimo e o número máximo de páginas dos livros publicados por cada editora e por cada edição? 
-- Ordene os resultados em ordem crescente
SELECT EDITORA, EDICAO, MIN(NUMPAGINAS), MAX(NUMPAGINAS)
FROM EXE_LIVROS
GROUP BY EDITORA, EDICAO
ORDER BY  MIN(NUMPAGINAS), MAX(NUMPAGINAS);

-- 11.  Quantos livros cada autor publicou? Ordene os resultados em ordem decrescente do número de publicações.
SELECT AUTOR, COUNT(*)
FROM EXE_LIVROS
GROUP BY AUTOR
ORDER BY COUNT(*) DESC;

-- 12.  Qual  o  valor  médio  dos  livros  de  terror?  
-- Formate  o  resultado  (valor)  para  que apareça  o  $  a  pontuação  de  milhagem.  
-- Arredonde  o  resultado  para  que  sejam exibidas até duas casas decimais. 
--Chame a coluna de saída por "Valor Médio". 
SELECT GENERO, TO_CHAR(ROUND(AVG(VALOR), 2), '$99999.99') AS "Valor Médio"
FROM EXE_LIVROS
GROUP BY GENERO
HAVING GENERO = 'terror';

-- 13.  Qual o valor médio dos livros de cada editora? 
-- Formate o resultado (valor) para que apareça o $ e a pontuação de milhagem. 
-- Arredonde o valor com duas casas decimais. 
-- Ordene os resultados pelo valor médio em ordem crescente.
SELECT EDITORA, TO_CHAR (ROUND(AVG(VALOR)), '$99999.99') AS "VALOR"
FROM EXE_LIVROS
GROUP BY EDITORA
ORDER BY VALOR;

-- 14.  Qual o número médio de páginas dos livros de cada gênero? 
-- Arredonde o resultado para que seja um valor inteiro.
SELECT GENERO, ROUND(AVG(NUMPAGINAS))
FROM EXE_LIVROS
GROUP BY GENERO;

-- 15.  Qual  o  total  de  páginas  de  todos  os  livros  publicados  por  cada  autor?  
-- Ordene  o resultado pelo número de páginas.
SELECT AUTOR, SUM(NUMPAGINAS)
FROM EXE_LIVROS
GROUP BY AUTOR
ORDER BY SUM(NUMPAGINAS);

-- 16.  Quantos livros em cada edição e de cada gênero são em Português ou Espanhol? 
-- Exiba os resultados cuja edições sejam a segunda ou terceira.
SELECT IDIOMA, EDICAO, GENERO, COUNT(*)
FROM EXE_LIVROS
GROUP BY IDIOMA, GENERO, EDICAO
HAVING IDIOMA IN ('Português', 'Espanhol') AND EDICAO IN (2, 3);

-- 17.  Quantos livros cada editora publicou por ano e por gênero? Ordene os resultados 
-- em  ordem  alfabética  da  editora,  seguida  pela  ordem  crescente  do  ano,  e  por  fim, pela ordem do gênero.
SELECT EDITORA, ANO_PUBLICACAO, GENERO, COUNT(*)
FROM EXE_LIVROS
GROUP BY EDITORA, ANO_PUBLICACAO, GENERO
ORDER BY EDITORA, ANO_PUBLICACAO, GENERO;

-- 18.  Qual o valor médio dos livros publicados de cada gênero e por cada idioma? 
-- Ordene os  resultados  por  ordem  alfabética  do  gênero   e  pela  ordem  decrescente  de  valor médio. 
-- Formate o resultado (valor) para que apareça o $ e a pontuação de milhagem. 
-- Arredonde o resultado para que sejam exibidas até duas casas decimais. 
SELECT  IDIOMA, GENERO, TO_CHAR(ROUND(AVG(VALOR), 2), '$99999.99') AS "Valor médio"
FROM EXE_LIVROS
GROUP BY GENERO, IDIOMA
ORDER BY IDIOMA;
 
SELECT * FROM EXE_LIVROS;