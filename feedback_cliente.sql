CREATE DATABASE sistema_feedback;

create table feedbacks (
	id serial primary key,
    cliente_id int NOT NULL, 
    data timestamp default current_timestamp,
    comentario text not null,
    resposta TEXT
    );
    
    INSERT INTO feedbacks (cliente_id, comentario) values 
    (1, 'Ótimo atendimento, estou muito satisfeito!'),
    (2, 'O serviço poderia ser mais rápido.'),
    (3, 'Excelente produto, recomendo.'),
    (4, 'Tive problemas com a entrega do meu pedido.');
    
    select * from feedbacks 
    where data between '2024-03-01' and '2024-03-11';
    
    update feedbacks 
    set resposta = 'Agradecemos seu feedback! Vamos trabalhar na melhoria do serviço.'
    where id = 2;
    
    DELETE FROM feedbacks
    where id = 4;