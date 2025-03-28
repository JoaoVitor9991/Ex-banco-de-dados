create database banco;
use banco;

create table clientes(
	id_cliente int primary key
    );
    
create table agencias (
	id_agencia int primary key
    );
    
create table conta (
	id_conta int primary key,
    id_cliente int,
    id_agencia int,
    saldo decimal (10, 2) default 0.00,
    foreign key (id_cliente) references clientes(id_cliente),
    foreign key (id_agencia) references agencias(id_agencia)
    );
    
create table saque (
	id_operacao int primary key,
    id_agencia int,
    id_conta int,
    valor decimal(10, 2),
    foreign key (id_agencia) references agencias(id_agencia),
    foreign key (id_conta) references conta(id_conta)
    );
    
create table deposito (
	id_operacao int primary key,
    id_agencia int,
    id_conta int,
    valor decimal (10,2),
    foreign key (id_agencia) references agencias(id_agencia),
    foreign key (id_conta) references conta(id_conta)
    );
    
DELIMITER $
Create trigger tgr_saque_insert after insert 
on saque 
for each row 
begin 
	update conta
    set saldo = saldo - new.valor
    where id_conta = new.id_conta;
END $
DELIMITER ;

DELIMITER $
create trigger tgr_deposito_insert after insert 
on deposito
for each row 
begin 
	update conta
    set saldo = saldo + new.valor
    where id_conta = new.id_conta;
END $
DELIMITER ;

insert into clientes (id_cliente) values (1);
insert into agencias (id_agencia) values (1);

insert into conta (id_conta, id_cliente, id_agencia, saldo) values (1, 1, 1, 1000.00);
insert into saque (id_operacao, id_agencia, id_conta, valor) values (1, 1, 1, 200.00);
insert into deposito (id_operacao, id_agencia, id_conta, valor) values(1, 1, 1, 300.00);

select * from conta;
select * from clientes;
select * from agencias;
select * from saque;
select * from deposito;

use agenda;

show tables;
describe usuarios;
describe contatos;
alter table contatos add column foto blob;


use agenda;

















