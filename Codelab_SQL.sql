--Exercicio 1--
SELECT nome,sobrenome,email FROM funcionarios f;

--Exercicio 2--
SELECT nome,sobrenome,email FROM funcionarios f;
WHERE cargo = 'Sales Rep';

--Exercicio 3--
SELECT DISTINCT cargo FROM funcionarios f;

--Exercicio 4--
SELECT DISTINCT cidade FROM lojas l; 

--Exercicio 5--
SELECT f.nome,f.sobrenome,f.email, l.cidade, l.pais,l.telefone
FROM funcionarios f INNER JOIN loja l ON f.codloja = l.codloja
WHERE f.cargo = 'President';
--Exercicio 6--
SELECT precosugerido, nomeproduto FROM produtos
ORDER BY precosugerido DESC LIMIT 1;

SELECT precocompra, nomeproduto FROM produtos
ORDER BY precocompra DESC LIMIT 1;


--Exercicio 7--
SELECT precosugerido FROM produtos
ORDER BY precosugerido ASC LIMIT 1;

SELECT precocompra FROM produtos;
ORDER BY precocompra ASC LIMIT 1;

--Exercicio 8--
SELECT nomeproduto, qtdestoque FROM produtos
ORDER BY qtdestoque ASC LIMIT 1;

--Exercicio 9--
SELECT nomeproduto,qtdestoque FROM produtos
ORDER BY qtdestoque DESC LIMIT 1;

--Exercicio 10--
SELECT p.nomeproduto, SUM(d.quantidadepedida) FROM produtos p 
INNER JOIN detalhespedidos d  ON p.codproduto = p.codproduto
GROUP BY p.nomeproduto 
