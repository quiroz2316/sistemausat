CREATE database DB_PROYECTO;
-- usar base de datos
use DB_PROYECTO;
-- Creacion de Tablas
create table semestre_academico(
idSemestre int primary key not null,
nombreSe varchar(8) not null,
fechaI date not null,
fechaF date not null,
estado boolean not null
);
create table facultad(
idFacultad int primary key not null,
nombreFa varchar(100) not null,
descripcion varchar(100) not null,
estado boolean not null
);
-- Seleccion de Tablas
select * from db_proyecto.semestre_academico;


