CREATE DATABASE cadastro_enderecos;
USE cadastro_enderecos;


CREATE TABLE Continente (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL
);


CREATE TABLE Pais (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    continente_id INT,
    FOREIGN KEY (continente_id) REFERENCES Continente(id)
);


CREATE TABLE Estado (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    pais_id INT,
    FOREIGN KEY (pais_id) REFERENCES Pais(id)
);


CREATE TABLE Cidade (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    estado_id INT,
    FOREIGN KEY (estado_id) REFERENCES Estado(id)
);

CREATE TABLE Bairro (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cidade_id INT,
    FOREIGN KEY (cidade_id) REFERENCES Cidade(id)
);


CREATE TABLE Rua (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    bairro_id INT,
    FOREIGN KEY (bairro_id) REFERENCES Bairro(id)
);


CREATE TABLE Endereco (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rua_id INT,
    bairro_id INT,
    cidade_id INT,
    estado_id INT,
    pais_id INT,
    continente_id INT,
    FOREIGN KEY (rua_id) REFERENCES Rua(id),
    FOREIGN KEY (bairro_id) REFERENCES Bairro(id),
    FOREIGN KEY (cidade_id) REFERENCES Cidade(id),
    FOREIGN KEY (estado_id) REFERENCES Estado(id),
    FOREIGN KEY (pais_id) REFERENCES Pais(id),
    FOREIGN KEY (continente_id) REFERENCES Continente(id)
);

SELECT 
    e.id AS endereco_id,
    r.nome AS rua,
    b.nome AS bairro,
    c.nome AS cidade,
    es.nome AS estado,
    p.nome AS pais,
    co.nome AS continente
FROM Endereco e
JOIN Rua r ON e.rua_id = r.id
JOIN Bairro b ON e.bairro_id = b.id
JOIN Cidade c ON e.cidade_id = c.id
JOIN Estado es ON e.estado_id = es.id
JOIN Pais p ON e.pais_id = p.id
JOIN Continente co ON e.continente_id = co.id;

INSERT INTO Continente (nome) VALUES 
('América'), 
('Europa'), 
('Ásia'), 
('África'), 
('Oceania');


INSERT INTO Pais (nome, continente_id) VALUES 
('Brasil', 1),
('Estados Unidos', 1),
('Argentina', 1),
('México', 1),
('Canadá', 1),
('França', 2),
('Alemanha', 2),
('Itália', 2),
('Espanha', 2),
('Reino Unido', 2),
('Japão', 3),
('China', 3),
('Índia', 3),
('África do Sul', 4),
('Austrália', 5);


INSERT INTO Estado (nome, pais_id) VALUES 
('São Paulo', 1),
('Minas Gerais', 1),
('Rio de Janeiro', 1),
('Califórnia', 2),
('Texas', 2),
('Nova York', 2),
('Buenos Aires', 3),
('Córdoba', 3),
('Cidade do México', 4),
('Jalisco', 4),
('Ontário', 5),
('Colúmbia Britânica', 5),
('Île-de-France', 6),
('Provence-Alpes-Côte d’Azur', 6),
('Baviera', 7),
('Renânia do Norte-Vestfália', 7),
('Catalunha', 8),
('Madri', 8),
('Lombardia', 9),
('Lácio', 9),
('Inglaterra', 10),
('Escócia', 10),
('Tóquio', 11),
('Osaka', 11),
('Pequim', 12),
('Xangai', 12),
('Maharashtra', 13),
('Uttar Pradesh', 13),
('Gauteng', 14),
('Nova Gales do Sul', 15);


INSERT INTO Cidade (nome, estado_id) VALUES 
('São Paulo', 1),
('Campinas', 1),
('Belo Horizonte', 2),
('Uberlândia', 2),
('Rio de Janeiro', 3),
('Niterói', 3),
('Los Angeles', 4),
('San Francisco', 4),
('Houston', 5),
('Austin', 5),
('Nova York', 6),
('Buffalo', 6),
('Buenos Aires', 7),
('Córdoba', 8),
('Cidade do México', 9),
('Guadalajara', 10),
('Toronto', 11),
('Vancouver', 12),
('Paris', 13),
('Marselha', 14),
('Munique', 15),
('Colônia', 16),
('Barcelona', 17),
('Madri', 18),
('Milão', 19),
('Roma', 20),
('Londres', 21),
('Edimburgo', 22),
('Tóquio', 23),
('Osaka', 24);


INSERT INTO Bairro (nome, cidade_id) VALUES 
('Centro', 1),
('Moema', 1),
('Barra Funda', 1),
('Cambuí', 2),
('Savassi', 3),
('Pampulha', 3),
('Centro', 4),
('Ipanema', 5),
('Copacabana', 5),
('Santa Rosa', 6),
('Downtown LA', 7),
('Hollywood', 7),
('Fisherman', 8),
('Midtown', 11),
('Harlem', 11),
('Upper', 11),
('Recoleta', 13),
('Palermo', 13),
('Centro', 14),
('Polanco', 15),
('Zona Rosa', 16),
('Downtown Toronto', 17),
('Gastown', 18),
('Montmartre', 19),
('La Défense', 20),
('Schmabing', 21),
('Altstadt', 22),
('Eixample', 23),
('Triana', 24),
('Shinjuku', 28);


INSERT INTO Rua (nome, bairro_id) VALUES
('Avenida Brasil', 1),  
('Rua Augusta', 1),  
('Rua da Consolação', 1),  
('Rua Oscar Freire', 2),  
('Rua Domingo', 3),  
('Avenida Norte-Sul', 4),  
('Rua José Alencar', 5),  
('Rua Professor de Moraes', 6),  
('Avenida Afonso Pena', 7),  
('Rua Gonçalves', 8),  
('Rua Bahia', 9),  
('Avenida Atlântica', 10),  
('Rua Barata Ribeiro', 11),  
('Rua Voluntários da Pátria', 12),  
('Rua Dias Ferreira', 13),  
('Sunset Boulevard', 14),  
('Hollywood Boulevard', 15),  
('Rodeo Drive', 16),  
('Market Street', 17),  
('Grant Avenue', 18),  
('Broadway', 19),  
('Wall Street', 20),  
('5TH Avenue', 21),  
('Madison Avenue', 22),  
('Central Park West', 23),  
('Avenida 9 de Julio', 24),  
('Avenida de Mayo', 25),  
('Calle Florida', 26),  
('Rua Belgrano', 27),  
('Rua Rivadavia', 28),  
('Avenida Paseo de la Reforma', 29),  
('Avenida Insurgentes', 30),  
('Calle de Madero', 1),  
('Rua Universidad', 2),  
('Yonge Street', 3),  
('Queen Street', 4),  
('Robson Street', 5),  
('Granville Street', 6),  
('Champs-Élysées', 7),  
('Rue de Rivoli', 8),  
('Boulevard Saint-Michel', 9),  
('Avenue Montaigne', 10),  
('Unter den Linden', 11),  
('Kurfürstendamm', 12),  
('Friedrichstrasse', 13),  
('Nathan Road', 14),  
('Orchard Road', 15),  
('Bandra Kurla Complex', 16),  
('Marine Drive', 17),  
('Victoria Street', 18),  
('Pitt Street', 19);

SELECT * FROM Continente;
SELECT * FROM Pais;
SELECT * FROM Estado;
SELECT * FROM Cidade;
SELECT * FROM Bairro;
select nome from Rua where id = 27;
select nome FROM Bairro WHere id = 12;
select nome from Cidade Where id =29;
select nome From Estado where id = 9;
select nome FROM Pais WHERE i= 19;
select nome FROM Continente WHERE ID =4;
ALTER TABLE Continente ADD COLUMN populacao BIGINT;
ALTER TABLE Pais ADD COLUMN populacao BIGINT;
ALTER TABLE Estado ADD COLUMN populacao BIGINT;
ALTER TABLE Cidade ADD COLUMN populacao BIGINT;
SELECT * FROM Pais ORDER BY populacao DESC LIMIT 1;
SELECT * FROM Pais ORDER BY populacao ASC LIMIT 1;
SELECT * FROM Continente ORDER BY populacao DESC LIMIT 1;
SELECT * FROM Continente ORDER BY populacao ASC LIMIT 1;
SELECT * FROM Estado ORDER BY populacao DESC LIMIT 1;
SELECT * FROM Estado ORDER BY populacao ASC LIMIT 1;
SELECT * FROM Cidade ORDER BY populacao DESC LIMIT 1;
SELECT * FROM Cidade ORDER BY populacao ASC LIMIT 1;







