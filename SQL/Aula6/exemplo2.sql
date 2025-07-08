-- DDL

DROP TABLE IF EXISTS curso; -- exclui tabela curso se ela existir

CREATE TABLE IF NOT EXISTS curso ( -- só cria cursos se ela não existir	
	nome varchar(10) not null unique, -- nome não pode ser nulo e é unico
	descricao text,
	carga int check (carga >= 0),
	total_aulas int,
	ano int default '2025'
);

ALTER TABLE curso
ADD COLUMN id serial primary key;

