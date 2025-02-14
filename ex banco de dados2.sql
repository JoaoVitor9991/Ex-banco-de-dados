create database crimes;

create table f (
	cidade varchar (40) not null,
    estado varchar (40) not null, 
    regiao varchar (40) not null, 
    dia varchar (8) not null,
    qnt_crimes int not null);
  
select * from f where cidade = 'Campo Grande';
select * from f where qnt_crimes >=3;
select cidade, qnt_crimes  from f where qnt_crimes=(select max(qnt_crimes) from f); 
select cidade, qnt_crimes  from f where qnt_crimes=(select min(qnt_crimes) from f);
select COUNT(*) AS total_registro from f;
select * from f where cidade LIKE 'C%';
select AVG(qnt_crimes) as media_crimes from f;





INSERT INTO f (cidade, estado, regiao, dia, qnt_crimes) VALUES
("Água Clara", "MS", "CENTRO-OESTE", "jan/21", 0),
("Alcinópolis", "MS", "CENTRO-OESTE",	"jan/21", 0),
("Amambai", "MS", "CENTRO-OESTE", "jan/21", 0),
("Anastácio", "MS",	"CENTRO-OESTE", "jan/21", 0),
("Anaurilândia", "MS", "CENTRO-OESTE", "jan/21", 0),
("Angélica", "MS", "CENTRO-OESTE", "jan/21", 0),
("Antônio João",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Aparecida Do Taboado",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Aquidauana", "MS", "CENTRO-OESTE", "jan/21", 0),
("Aral Moreira",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Bandeirantes",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Bataguassu", "MS", "CENTRO-OESTE", "jan/21" , 0),
("Batayporã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Bela Vista", "MS", "CENTRO-OESTE", "jan/21", 0),
("Bodoquena", "MS", "CENTRO-OESTE", "jan/21", 0),
("Bonito", "MS", "CENTRO-OESTE", "jan/21",0),
("Brasilândia",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Caarapó", "MS", "CENTRO-OESTE", "jan/21",	0),
("Camapuã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Campo Grande", "MS", "CENTRO-OESTE", "jan/21", 9),
("Caracol", "MS", "CENTRO-OESTE", "jan/21", 0),
("Cassilândia",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Chapadão Do Sul", "MS", "CENTRO-OESTE", "jan/21", 0),
("Corguinho", "MS", "CENTRO-OESTE", "jan/21", 0),
("Coronel Sapucaia", "MS", "CENTRO-OESTE", "jan/21", 1),
("Corumbá", "MS", "CENTRO-OESTE", "jan/21", 4),
("Costa Rica", "MS", "CENTRO-OESTE", "jan/21", 0),
("Coxim", "MS",	"CENTRO-OESTE",	"jan/21", 1),
("Deodápolis", "MS", "CENTRO-OESTE", "jan/21", 0),
("Dois Irmãos Do Buriti", "MS",	"CENTRO-OESTE",	"jan/21", 0),
("Douradina", "MS", "CENTRO-OESTE", "jan/21", 0),
("Dourados", "MS", "CENTRO-OESTE", "jan/21", 3),
("Eldorado", "MS", "CENTRO-OESTE", "jan/21", 0),
("Fátima Do Sul", "MS",	"CENTRO-OESTE", "jan/21", 1),
("Figueirão", "MS", "CENTRO-OESTE", "jan/21", 0),
("Glória De Dourados", "MS", "CENTRO-OESTE", "jan/21", 0),
("Guia Lopes Da Laguna", "MS", "CENTRO-OESTE", "jan/21", 0),
("Iguatemi", "MS", "CENTRO-OESTE", "jan/21", 0),
("Inocência", "MS", "CENTRO-OESTE", "jan/21", 0),
("Itaporã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Itaquiraí", "MS", "CENTRO-OESTE", "jan/21", 1),
("Ivinhema", "MS", "CENTRO-OESTE", "jan/21", 1),
("Japorã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Jaraguari", "MS", "CENTRO-OESTE", "jan/21", 0),
("Jardim", "MS", "CENTRO-OESTE", "jan/21", 0),
("Jateí", "MS",	"CENTRO-OESTE", "jan/21", 0),
("Juti", "MS", "CENTRO-OESTE", "jan/21", 0),
("Ladário", "MS", "CENTRO-OESTE", "jan/21",0),
("Laguna Carapã", "MS",	"CENTRO-OESTE",	"jan/21", 0),
("Maracaju", "MS", "CENTRO-OESTE", "jan/21", 1),
("Miranda", "MS", "CENTRO-OESTE", "jan/21", 2),
("Mundo Novo", "MS", "CENTRO-OESTE", "jan/21", 0),
("Naviraí", "MS", "CENTRO-OESTE", "jan/21", 0),
("Nioaque", "MS", "CENTRO-OESTE", "jan/21", 0),
("Nova Alvorada Do Sul", "MS", "CENTRO-OESTE", "jan/21", 0),
("Nova Andradina", "MS", "CENTRO-OESTE", "jan/21", 0),
("Novo Horizonte Do Sul", "MS",	"CENTRO-OESTE", "jan/21", 0),
("Paraíso Das Águas", "MS", "CENTRO-OESTE", "jan/21", 0),
("Paranaíba", "MS", "CENTRO-OESTE", "jan/21", 0),
("Paranhos", "MS", "CENTRO-OESTE", "jan/21", 1),
("Pedro Gomes",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Ponta Porã",	"MS", "CENTRO-OESTE", "jan/21",	5),
("Porto Murtinho", "MS", "CENTRO-OESTE", "jan/21", 0),
("Ribas Do Rio Pardo", "MS", "CENTRO-OESTE", "jan/21", 0),
("Rio Brilhante" , "MS", "CENTRO-OESTE", "jan/21", 0),
("Rio Negro", "MS", "CENTRO-OESTE", "jan/21", 0),
("Rio Verde De Mato Grosso", "MS", "CENTRO-OESTE", "jan/21", 0),
("Rochedo", "MS", "CENTRO-OESTE", "jan/21", 0),
("Santa Rita Do Pardo", "MS", "CENTRO-OESTE", "jan/21",	0),
("São Gabriel Do Oeste", "MS", "CENTRO-OESTE", "jan/21", 1),
("Sete Quedas",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Selvíria", "MS", "CENTRO-OESTE", "jan/21", 0),
("Sidrolândia",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Sonora", "MS", "CENTRO-OESTE", "jan/21", 0),
("Tacuru", "MS", "CENTRO-OESTE", "jan/21", 0),
("Taquarussu", "MS", "CENTRO-OESTE", "jan/21", 0),
("Terenos", "MS", "CENTRO-OESTE", "jan/21", 0),
("Três Lagoas",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Vicentina", "MS", "CENTRO-OESTE", "jan/21", 0);


        
        
	