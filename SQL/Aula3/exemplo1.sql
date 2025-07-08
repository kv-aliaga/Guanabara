/* Banco de Dados: registrar instancias diferentes de características semelhantes
TIPOS PRIMITIVOS
	Numérico: inteiro, real, lógico
	Data/Tempo
	Literal: caracteres (String), texto, binário, coleção
	Espaciais*/

CREATE TABLE pessoas(
	nome varchar(30), 
	idade smallint, -- ajuda a dimensionar melhor o banco de dados
	genero char(1),
	peso float,
	altura float,
	nacionalidade varchar(30)
);

SELECT * FROM pessoas