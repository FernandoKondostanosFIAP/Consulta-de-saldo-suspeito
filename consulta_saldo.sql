-- Corrija esta consulta sem mudar o nome da coluna "saldo".
SELECT c.nome, SUM(t.valor) AS saldo
FROM clientes c
JOIN transacoes t ON c.id = t.cliente_id
GROUP BY c.nome;
