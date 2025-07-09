-- AGRUPANDO
select carga from curso
group by carga; -- mostra todos os valores de carga

select carga, count(nome) from curso
group by carga; -- conta quantos cursos tem essa quantidade de carga

select totaulas, count(*) from curso
group by totaulas
order by totaulas; -- conta quantos cursos tem a quantidade de aulas

select carga, count(nome) from curso
where totaulas = 30
group by carga; -- dos cursos que tem 30 aulas, quais são as cargas

-- HAVING: where para o group by, só pode ser usado pelo campo agrupado
select ano, count(*) from curso
group by ano
having count(*) >= 5 and ano > 2015
order by count(*); -- quantidade de cursos por ano, onde a quantidade de aulas é maior que 5 o ano é maior que 2015

select avg(carga) from curso;

select carga, count(*) from curso
where ano > 2015
group by carga
having carga > (select avg(carga) from curso); -- mostra a carga e a quantidade de cursos onde o ano é maior que 2015 e que a carga é maior que a média de cargas