-- LIKE E ILIKE
select * from curso
where nome like 'P%'; -- procura nomes que tennham p

select * from curso
where nome ilike '%a%'; -- procura nomes com a em qualquer lugar ignorando serem ou não maiúsculas

select * from curso
where nome like '%p_'; -- exige que tenha algo depois de p

-- DISTINCT
select distinct nacionalidade from gafanhotos; -- pegar um de cada elemento

-- FUNÇÕES DE AGREGAÇÃO
select count(nome) from curso; -- conta quantos tem

select count(*) from curso
where carga > 40; -- conta quantos cursos tem a carga > 40

select max(carga) from curso
where ano > 2015; -- seleciona no ano de 2015 qual foi a maior carga 

SELECT nome, totaulas
FROM curso
WHERE ano = 2016
ORDER BY totaulas ASC
LIMIT 1; -- adapta para postgre

select sum(totaulas) from curso; -- soma qtd aulas

select avg(totaulas) from curso; -- média de aulas por curso

