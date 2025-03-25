create database mercadin;
use mercadin;
create table produto (
    referencia varchar(3) primary key, 
    descricao varchar(50) unique,
    estoque int not null default 0
);

insert into produto values ('001', 'Feijão', 10);
insert into produto values ('002', 'Arroz', 5);
insert into produto values ('003', 'Farinha', 15); 

create table item_venda (
    venda int primary key,
    produto varchar(3), 
    quantidade int,
    foreign key (produto) references produto (referencia)
);

insert into item_venda values (1, '001', 3);
insert into item_venda values (2, '002', 1);
insert into item_venda values (3, '003', 5);

select * from item_venda;
select * from produto;
select venda, quantidade, descricao from item_venda join produto on produto = referencia;

DELIMITER $
create trigger tgr_item_venda_insert after insert 
on item_venda
for each row 
begin
update produto set estoque = estoque - new.quantidade
where referencia = new.produto;
end $
DELIMITER ;

insert into item_venda values(4, '001',3);
insert into item_venda values(5, '002', 1);
insert into item_venda values(6, '003', 5);

DELIMITER $
create trigger tgr_item_venda_delete after delete on item_venda
for each row 
begin 
update produto set estoque = estoque + old.quantidade
where referencia = old.produto;
end $

DELIMITER ;

delete from item_venda where venda =2 and produto = '002';
 show triggers 
 #drop trigger e nome da trigger para deletar

