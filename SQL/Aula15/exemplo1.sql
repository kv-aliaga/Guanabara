-- RELACIONAMENTO
-- N:1 -> Vários alunos estudam em uma escola
	--  PK de escola vai como FK em aluno

-- N:N -> Vários alunos participam de várias aulas
	--  Tabela intermediária com FKs dos dois

-- 1:1 -> Cada aluno tem uma matrícula e cada matrícula tem um aluno
	-- Unir as tabelas, colocar a PK de uma na FK de outra com UNIQUE

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos -- relaciona pk cursopreferido com fk idcurso
add foreign key (cursopreferido)
references curso(idcurso);

update gafanhotos
set cursopreferido = 6
where id = 1; -- muda o curso preferido de Daniel Morais para o 6

delete from curso
where idcurso = 6; -- não pode ser apagado porque alguém tem esse curso como favorito

-- MOSTRANDO NOMES AO INVÉS DE NÚMEROS NOS CURSOS FAVORITOS
select g.nome, c.nome as "curso preferido", c.ano
from gafanhotos g
join curso c on g.cursopreferido = c.idcurso
order by g.nome;

-- MOSTRA TODOS OS ALUNOS MESMO QUE SEUS VALORES SEJAM NULOS
select g.nome, c.nome as "curso preferido", c.ano
from gafanhotos g
left join curso c on g.cursopreferido = c.idcurso
order by g.nome;

-- MOSTRA TODOS OS CURSOS MESMO QUE SEUS VALORES SEJAM NULOS
select g.nome, c.nome as "curso preferido", c.ano
from gafanhotos g
right join curso c on g.cursopreferido = c.idcurso
order by g.nome;
