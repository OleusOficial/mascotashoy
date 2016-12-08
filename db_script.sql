create database mascotas_hoy;
use mascotas_hoy;
create table users(
id_user integer auto_increment not null primary key,
user_name varchar(50) not null,
email varchar(50) not null,
password_p varchar(8) not null);

insert into users(user_name, email, password_p) values('Oleus','androidkimbiso@gmail.com','password');