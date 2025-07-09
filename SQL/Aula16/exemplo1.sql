create table assiste(
	id serial primary key,
	data date,
	idgafanhoto int,
	idcurso int,
	-- declara idgafanhoto e idcurso como FK
	-- foreing key (nome do atributo) references nome da tabela(nome da pk)
	foreign key (idgafanhoto) references gafanhotos(id),
	foreign key (idcurso) references curso(idcurso)
);

insert into assiste
values 
	(default, '2025-07-09', 15, 3),
	(default, '2025-07-09', 2, 4),
	(default, '2025-07-09', 3, 12),
	(default, '2025-07-09', 4, 21),
	(default, '2025-07-09', 5, 23),
	(default, '2025-07-09', 6, 24),
	(default, '2025-07-09', 7, 23),
	(default, '2025-07-09', 8, 25),
	(default, '2025-07-09', 9, 27),
	(default, '2025-07-09', 10, 12),
	(default, '2025-07-09', 11, 28),
	(default, '2025-07-09', 12, 29),
	(default, '2025-07-09', 13, 6),
	(default, '2025-07-09', 14, 7);

select g.id, g.nome as "gafanhoto", c.nome as "nome do curso"
from gafanhotos g
join assiste a on g.id = a.idgafanhoto
join curso c on a.idcurso = c.idcurso
order by g.id;

select * from assiste