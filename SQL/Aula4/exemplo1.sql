-- recriando banco de dados sql
create database sql
with
	encoding = 'utf8'
	lc_collate = 'en_US.UTF-8'
	lc_ctype = 'en_US.UTF-8';

-- recriando
-- ddl (comandos de definição)
CREATE TABLE pessoas (
	id serial primary key, -- primary key identifica que id é o identificador da tabela pessoas
	nome varchar(30) not null,
	nascimento date, -- forma mais fácil de calcular idade
	genero char(1) check (genero in ('M', 'F')), -- equivalente ao enum no mysql
	peso decimal(5, 2),
	altura decimal(3, 2), -- economiza quantidade de bytes
	nacionalidade varchar(30) default 'Brasil'
);