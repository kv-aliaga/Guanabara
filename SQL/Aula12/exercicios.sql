select * from gafanhotos

-- EXERCICIO 1
select nome, profissao, sexo, nacionalidade from gafanhotos
where sexo = 'F';

-- EXERCICIO 2
select nome, profissao, nascimento, nacionalidade from gafanhotos
where nascimento between '2000-01-01' and '2015-12-31'
order by nascimento;

-- EXERCICIO 3
select nome, profissao, sexo, nacionalidade from gafanhotos
where profissao = 'Programador' and sexo = 'M'
order by nome;

-- EXERCICIO 4
select nome, sexo, nacionalidade from gafanhotos
where sexo = 'F' and nacionalidade = 'Brasil' and nome like 'J%';

-- EXERCICIO 5
select nome, nacionalidade from gafanhotos
where sexo = 'M' and nacionalidade != 'Brasil' 
	and peso < 100 and nome like '%_Silva%';

-- EXERCICIO 6
select max(altura) from gafanhotos
where nacionalidade = 'Brasil' and sexo = 'M';

-- EXERCICIO 7
select avg(peso) from gafanhotos;

-- EXERCICIO 8
select min(peso) from gafanhotos
where sexo = 'F' and nacionalidade != 'Brasil' and 
nascimento between '1990-01-01' and '2000-12-31';

-- EXERCICIO 9
select count(*) from gafanhotos
where sexo = 'F' and altura > 1.9;