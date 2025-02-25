CREATE DATABASE cadastro_cliente;
use cadastro_cliente;
create table cadastrar_cliente(
	CPF VARCHAR (11) PRIMARY KEY, 
    Nome VARCHAR(100) NOT NULL,
    RG VARCHAR (20),
    Fone VARCHAR(20),
    Id_cidade INT,
    Id_sexo INT,
    Id_raca int,
    ID_escolaridade INT,
    foreign key (Id_cidade) references cidade(Id_cidade),
    foreign key (Id_sexo) references sexo (Id_sexo),
    foreign key (Id_raca) references raca (Id_raca),
    foreign key (Id_escolaridade) references escolaridade(Id_escolaridade)
    );
    
create table estado (
		Id_estado INT primary key auto_increment,
        Estado varchar(50) not null
        );

create table cidade (
		Id_cidade INT PRIMARY KEY auto_increment,
        Cidade VARCHAR(50) NOT NULL,
        Id_estado INT,
        FOREIGN KEY (Id_estado) references estado(Id_estado)
        );

create table sexo (
	Id_sexo INT primary KEY auto_increment,
    Sexo VARCHAR(10) not null
    );
    
create table raca (
	Id_raca int primary key auto_increment,
    Raca VARCHAR (30) NOT NULL
    );
    
create table escolaridade (
	Id_escolaridade int primary key auto_increment,
    Escolaridade VARCHAR (50) not null
    );

create table nacionalidade (
	Id_nacionalidade INT PRIMARY KEY auto_increment,
	Nacionalidade VARCHAR (50) NOT NULL
    );
    

INSERT INTO estado (Estado) VALUES
('Acre'), ('Alagoas'), ('Amapá'), ('Amazonas'), ('Bahia'),
('Ceará'), ('Distrito Federal'), ('Espírito Santo'), ('Goiás'), ('Maranhão'),
('Mato Grosso'), ('Mato Grosso do Sul'), ('Minas Gerais'), ('Pará'), ('Paraíba'),
('Paraná'), ('Pernambuco'), ('Piauí'), ('Rio de Janeiro'), ('Rio Grande do Norte'),
('Rio Grande do Sul'), ('Rondônia'), ('Roraima'), ('Santa Catarina'), ('São Paulo'),
('Sergipe'), ('Tocantins');


INSERT INTO cidade (Cidade, Id_estado) VALUES
-- Acre
('Rio Branco', 1), ('Cruzeiro do Sul', 1), ('Sena Madureira', 1), ('Tarauacá', 1), ('Feijó', 1),
-- Alagoas
('Maceió', 2), ('Arapiraca', 2), ('Palmeira dos Índios', 2), ('Rio Largo', 2), ('Penedo', 2),
-- Amapá
('Macapá', 3), ('Santana', 3), ('Laranjal do Jari', 3), ('Oiapoque', 3), ('Porto Grande', 3),
-- Amazonas
('Manaus', 4), ('Parintins', 4), ('Itacoatiara', 4), ('Manacapuru', 4), ('Coari', 4),
-- Bahia
('Salvador', 5), ('Feira de Santana', 5), ('Vitória da Conquista', 5), ('Camaçari', 5), ('Juazeiro', 5),
-- Ceará
('Fortaleza', 6), ('Caucaia', 6), ('Juazeiro do Norte', 6), ('Maracanaú', 6), ('Sobral', 6),
-- Distrito Federal
('Brasília', 7), ('Taguatinga', 7), ('Ceilândia', 7), ('Gama', 7), ('Samambaia', 7),
-- Espírito Santo
('Vitória', 8), ('Vila Velha', 8), ('Serra', 8), ('Cariacica', 8), ('Guarapari', 8),
-- Goiás
('Goiânia', 9), ('Aparecida de Goiânia', 9), ('Anápolis', 9), ('Rio Verde', 9), ('Luziânia', 9),
-- Maranhão
('São Luís', 10), ('Imperatriz', 10), ('Caxias', 10), ('Timon', 10), ('Codó', 10),
-- Mato Grosso
('Cuiabá', 11), ('Várzea Grande', 11), ('Rondonópolis', 11), ('Sinop', 11), ('Tangará da Serra', 11),
-- Mato Grosso do Sul
('Campo Grande', 12), ('Dourados', 12), ('Três Lagoas', 12), ('Corumbá', 12), ('Ponta Porã', 12),
-- Minas Gerais
('Belo Horizonte', 13), ('Uberlândia', 13), ('Contagem', 13), ('Juiz de Fora', 13), ('Betim', 13),
-- Pará
('Belém', 14), ('Ananindeua', 14), ('Santarém', 14), ('Marabá', 14), ('Castanhal', 14),
-- Paraíba
('João Pessoa', 15), ('Campina Grande', 15), ('Santa Rita', 15), ('Patos', 15), ('Bayeux', 15),
-- Paraná
('Curitiba', 16), ('Londrina', 16), ('Maringá', 16), ('Ponta Grossa', 16), ('Cascavel', 16),
-- Pernambuco
('Recife', 17), ('Jaboatão dos Guararapes', 17), ('Olinda', 17), ('Caruaru', 17), ('Petrolina', 17),
-- Piauí
('Teresina', 18), ('Parnaíba', 18), ('Picos', 18), ('Floriano', 18), ('Piripiri', 18),
-- Rio de Janeiro
('Rio de Janeiro', 19), ('São Gonçalo', 19), ('Duque de Caxias', 19), ('Nova Iguaçu', 19), ('Niterói', 19),
-- Rio Grande do Norte
('Natal', 20), ('Mossoró', 20), ('Parnamirim', 20), ('São Gonçalo do Amarante', 20), ('Macaíba', 20),
-- Rio Grande do Sul
('Porto Alegre', 21), ('Caxias do Sul', 21), ('Pelotas', 21), ('Canoas', 21), ('Santa Maria', 21),
-- Rondônia
('Porto Velho', 22), ('Ji-Paraná', 22), ('Ariquemes', 22), ('Vilhena', 22), ('Cacoal', 22),
-- Roraima
('Boa Vista', 23), ('Rorainópolis', 23), ('Caracaraí', 23), ('Mucajaí', 23), ('Pacaraima', 23),
-- Santa Catarina
('Florianópolis', 24), ('Joinville', 24), ('Blumenau', 24), ('São José', 24), ('Chapecó', 24),
-- São Paulo
('São Paulo', 25), ('Campinas', 25), ('Guarulhos', 25), ('Santos', 25), ('São Bernardo do Campo', 25),
-- Sergipe
('Aracaju', 26), ('Nossa Senhora do Socorro', 26), ('Lagarto', 26), ('Itabaiana', 26), ('Estância', 26),
-- Tocantins
('Palmas', 27), ('Araguaína', 27), ('Gurupi', 27), ('Porto Nacional', 27), ('Paraíso do Tocantins', 27);

INSERT INTO cadastrar_cliente (CPF, Nome, RG, Fone, Id_cidade, Id_sexo, Id_raca, Id_escolaridade) 
VALUES
('12345678901', 'João Silva', '12345678', '999999999', 1, 1, 1, 1),
('23456789012', 'Maria Oliveira', '23456789', '988888888', 2, 2, 2, 2),
('34567890123', 'Carlos Santos', '34567890', '977777777', 3, 1, 3, 3),
('45678901234', 'Ana Costa', '45678901', '966666666', 4, 2, 4, 4),
('56789012345', 'Pedro Souza', '56789012', '955555555', 5, 1, 1, 5),
('67890123456', 'Beatriz Lima', '67890123', '944444444', 6, 2, 2, 6),
('78901234567', 'Lucas Pereira', '78901234', '933333333', 7, 1, 3, 7),
('89012345678', 'Mariana Silva', '89012345', '922222222', 8, 2, 4, 8),
('90123456789', 'Felipe Almeida', '90123456', '911111111', 9, 1, 1, 1),
('11223344556', 'Juliana Rodrigues', '11223344', '900000000', 10, 2, 2, 2),
('22334455667', 'Ricardo Costa', '22334455', '909999999', 11, 1, 3, 3),
('33445566778', 'Cláudia Fernandes', '33445566', '918888888', 12, 2, 4, 4),
('44556677889', 'Gabriel Rocha', '44556677', '927777777', 13, 1, 1, 5),
('55667788990', 'Laura Martins', '55667788', '936666666', 14, 2, 2, 6),
('66778899001', 'Thiago Oliveira', '66778899', '945555555', 15, 1, 3, 7),
('77889900112', 'Rafaela Pinto', '77889900', '954444444', 16, 2, 4, 8),
('88990011223', 'Gustavo Souza', '88990011', '963333333', 17, 1, 1, 1),
('99001122334', 'Isabela Silva', '99001122', '972222222', 18, 2, 2, 2),
('10111223345', 'André Costa', '10111223', '981111111', 19, 1, 3, 3),
('12122334456', 'Sofia Rocha', '12122334', '990000000', 20, 2, 4, 4);



Insert into sexo (Sexo) Values 
('Masculino'), 
('Feminino'), 
('Outro');

Insert into nacionalidade (Nacionalidade) VALUES
('Brasileiro(a)'),
('Estrangeiro(a)');

insert into raca (raca) VALUES
('Branco'),
('Pardo'),
('Negro'),
('Indígina'),
('Amarelo');

insert into escolaridade (Escolaridade) VALUES 
('Ensino Fundamental Incompleto'),
('Ensino Fundamental Completo'),
('Ensino médio incompleto'),
('Ensino médio completo'),
('Ensino Técnico'),
('Ensino Superior incompleto'),
('Ensino Superior Completo'),
('Pós-Graduação, Mestrado ou Doutorado');

SELECT * FROM cadastrar_cliente;
SELECT * FROM cidade;
select * from sexo;
select * from escolaridade;

select cadastrar_cliente.Nome, estado.Estado
from cadastrar_cliente
JOIN cidade on cadastrar_cliente.Id_cidade = cidade.Id_cidade
join estado on cidade.Id_estado = estado.Id_estado;

select cadastrar_cliente.Nome, cidade.Cidade
from cadastrar_cliente
Join cidade ON cadastrar_cliente.Id_cidade = cidade.Id_cidade;

select cadastrar_cliente.Nome, cadastrar_cliente.CPF, raca.Raca
from cadastrar_cliente
join raca on cadastrar_cliente.Id_raca = raca.Id_raca;

SELECT cadastrar_cliente.Nome, nacionalidade.Nacionalidade
FROM cadastrar_cliente
JOIN nacionalidade ON cadastrar_cliente.Id_nacionalidade = nacionalidade.Id_nacionalidade;



