CREATE DATABASE resiliadata_steph
USE resiliadata_steph

CREATE TABLE Empresas_Parceiras (id int primary key auto_increment, Nome varchar (40), Endereco varchar (40), Contato varchar (40));

CREATE TABLE Tecnologias (id int primary key auto_increment, Nome varchar (40), Area varchar (40));

CREATE TABLE Colaboradores (id int primary key auto_increment, Nome varchar (40), Cargo varchar (40), Empresa_id int, Tecnologia_id int, foreign key (Empresa_id) references Empresas_Parceiras(id), foreign key (Tecnologia_id) references Tecnologias(id));

INSERT INTO Empresas_Parceiras (Nome, Endereco, Contato) values ('Stone', 'Cinelandia - Centro - RJ', '219965347624'), ('Santander', 'Irajá - Rio de Janeiro', '2199653427645');

INSERT INTO Tecnologias (Nome, Area) values ('HTML', 'Webdev'), ('Python', 'Dados');

INSERT INTO Colaboradores (Nome, Cargo, Empresa_id, Tecnologia_id) values ('Davi Moraes', 'Desenvolvedor', 1, 1), ('Stephane Nascimento', 'Analista', 2, 2);


