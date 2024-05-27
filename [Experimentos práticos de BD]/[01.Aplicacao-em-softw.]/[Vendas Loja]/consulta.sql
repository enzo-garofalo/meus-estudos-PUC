SELECT * FROM LOJA_PRODUTOS;
SELECT * FROM loja_cargos;
SELECT * FROM loja_funcionarios;
SELECT * FROM LOJA_VENDAS;

-- 1) Selecione todos os dados de todos os funcionários da loja e acrescente o nome do cargo e o salário que ele exerce.
SELECT FUN.*, CAR.NOME AS "NOME DO CARGO", CAR.SALARIO
FROM LOJA_FUNCIONARIOS FUN
JOIN LOJA_CARGOS CAR ON FUN.CARGO = CAR.COD_CARGO;

-- 2) Qual o cargo e o salário do vendedor 10008?
SELECT FUN.COD_FUNC, CAR.NOME, CAR.SALARIO
FROM LOJA_FUNCIONARIOS FUN
JOIN LOJA_CARGOS CAR ON FUN.CARGO = CAR.COD_CARGO
WHERE FUN.COD_FUNC = 10008;

--3) Qual o nome de todos os funcionários que trabalham como Caixa? Ordene o resultado em ordem alfabética
SELECT FUN.NOME, CAR.NOME
FROM LOJA_FUNCIONARIOS FUN
JOIN LOJA_CARGOS CAR ON FUN.CARGO = CAR.COD_CARGO
WHERE CAR.NOME = 'Caixa'
ORDER BY FUN.NOME;

-- 4) Qual o nome e o nome do cargo do vendedor 10001?
SELECT FUN.COD_FUNC, FUN.NOME, CAR.NOME AS "CARGO"
FROM LOJA_FUNCIONARIOS FUN
JOIN LOJA_CARGOS CAR ON FUN.CARGO = CAR.COD_CARGO
WHERE FUN.COD_FUNC = 10001;

-- 5) Qual o código e o nome do produto da venda cujo id_venda é 1130?
SELECT PRODUTOS.COD_PROD, PRODUTOS.NOME
FROM LOJA_VENDAS VENDAS
JOIN LOJA_PRODUTOS PRODUTOS ON VENDAS.PRODUTO = PRODUTOS.COD_PROD
WHERE VENDAS.ID_VENDA = 1130;

-- 6) Qual são os dados do funcionário que fez a venda cujo id_venda é 1351?
SELECT VENDAS.ID_VENDA, FUNC.*
FROM LOJA_VENDAS VENDAS
JOIN LOJA_FUNCIONARIOS FUNC ON VENDAS.FUNCIONARIO = FUNC.COD_FUNC
WHERE VENDAS.ID_VENDA = 1351;

-- 7) Liste o nome de todos os produtos que foram vendidos. Não repetir o dado.
SELECT DISTINCT PROD.NOME
FROM LOJA_VENDAS VENDAS
JOIN LOJA_PRODUTOS PROD ON VENDAS.PRODUTO = PROD.COD_PROD;

-- 8) Quais os nomes dos funcionários que venderam o ‘Produto K’?
SELECT FUNC.NOME
FROM LOJA_VENDAS VENDAS
JOIN LOJA_FUNCIONARIOS FUNC ON VENDAS.FUNCIONARIO = FUNC.COD_FUNC
JOIN LOJA_PRODUTOS PROD ON VENDAS.PRODUTO = PROD.COD_PROD
WHERE PROD.NOME = 'Produto K';

-- 9) Liste o nome de todos os produtos que foram vendidos e a quantas unidades de cada
-- um foram vendidos. Ordene os resultados pela ordem crescente do número de produtos vendidos
