use login_formulario; 

create table usuario(
    id INT auto_increment primary key, 
	email varchar (40) not null UNIQUE,
    senha varchar(40) not null
    );
