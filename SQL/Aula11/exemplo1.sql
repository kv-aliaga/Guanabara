-- DQL

-- SELEÇÃO POR COLUNAS
select * from curso; -- seleciona tudo

select * from curso
order by nome; -- seleciona tudo em ordem alfabética (por nome)

select * from curso
order by nome desc; -- seleciona tudo em ordem alfabética inversa

select nome, carga, ano from curso
order by ano, nome; -- mostra nome, carga e ano na ordem por ano e se houver ocorrências iguais de ano, por nome

-- SELEÇÃO POR LINHAS
select * from curso
where ano = 2016
order by nome; -- mostra só os cursos de 2016

select nome, descricao, ano from curso
where ano <= 2019
order by nome;

select nome, ano from curso
where ano between 2014 and 2018
order by ano desc, nome asc; -- mostra nome e ano na ordem por ano e se houver ocorrências iguais de ano decrescente entre 2014 e 2018, por nome crescente

select nome, ano from curso
where ano in(2014, 2019)
order by ano; -- mostra nome e ano, onde ano é ou 2014 ou 2019, ordenado por ano

select nome, carga, totaulas from curso
where carga > 35 and totaulas < 30; -- juntando com operadores lógicos

select nome, carga, totaulas from curso
where carga > 35 or totaulas < 30;