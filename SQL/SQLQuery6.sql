create table aluno(
	matricula int identity,
	nome varchar(20)unique,
	constraint pk_aluno primary key (matricula)
);

create table prova(
	id int identity primary key, 
	nota int,
	matricula int foreign key references aluno (matricula)

);

insert into aluno (nome)
values
('Joao'), ('Eric')...

insert into prova (matricula)
values
(null)

select * from prova


