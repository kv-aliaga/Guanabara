-- DML

insert into curso values
('HTML5', 'Curso de HTML5', 40, 37, default, default),
('Algoritimo', 'Lógica de Programação', 20, 15, default, default),
('Photoshop', 'Curso de Photoshop', 40, 37, default, default),
('Python', 'Curso de Pyhton', 40, 20, default, default),
('SQL', 'Curso de SQL', 40, 15, default, default),
('PHP', 'Curso de PGP', 40, 37, default, default),
('Jarva', 'Curso de Java', 40, 12, default, default),
('Word', 'Curso de Word', 40, 37, default, default),
('Cozinha', 'Aprenda a fazer kibe', 40, 30, default, default),
('C#', '#CSharp!', 40, 12, default, default);

-- alterando linhas
UPDATE curso
SET nome = 'Novo HTML6'
WHERE id = 1;

UPDATE curso
SET descricao = 'Curso de PHP'
WHERE id = 6;

UPDATE curso
SET nome = 'Jacarias' 
WHERE carga = 40
AND total_aulas = 12;

-- deletando linhas
DELETE FROM curso
WHERE id = 6;

-- deletando todas as linhas
truncate curso;

select * from curso;