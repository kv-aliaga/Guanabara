-- MANIPULAÇÃO: (DML)

-- id e nacionalidade se auto incrementam como 1, 2 e Brasil
INSERT INTO pessoas(nome, nascimento, genero, peso, altura)
	VALUES ('Jones', '2010-02-26', 'M', 50, 1.8);
INSERT INTO pessoas(id, nome, nascimento, genero, peso, altura, nacionalidade)
	VALUES (default, 'Eva', '0001-01-01', 'F', 46, 1.5, default); 

-- Se os valores inseridos forem na mesma ordem e quantidade do padrão da tabela, pode se fazer desse jeito
INSERT INTO pessoas VALUES (default, 'Ringo', '1940-07-07', 'M', 70, 1.8, 'Inglaterra'); 

-- Vários valores inseridos de uma vez só
INSERT INTO pessoas
	VALUES
		(default, 'Davi', '2010-02-26', 'M', 50, 1.8, default),
		(default, 'Bia', '2010-06-15', 'F', 40, 1.6, default);

SELECT * FROM pessoas;