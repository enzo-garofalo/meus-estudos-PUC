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


SELECT * FROM EXE_LIVROS;