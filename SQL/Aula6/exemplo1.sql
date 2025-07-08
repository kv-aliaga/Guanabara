-- alterando tabelas
ALTER TABLE pessoas
ADD COLUMN profissao varchar(10); -- adiciona tabela profissão

ALTER TABLE pessoas
DROP COLUMN profissao; -- exclui a tabela profissão

-- altera a coluna profissão
ALTER TABLE pessoas
ALTER COLUMN profissao TYPE varchar(20),
ALTER COLUMN profissao SET DEFAULT 'desempregado';

UPDATE pessoas SET profissao = 'desempregado' WHERE profissao IS NULL;

-- muda o nome da coluna
ALTER TABLE pessoas
RENAME COLUMN profissao to emprego;

-- muda o nome da tabela
ALTER TABLE pessoas
RENAME to pessoa;

SELECT * FROM pessoa;