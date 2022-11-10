create database car_tinder;

use car_tinder;


create table members
(ID int auto_increment primary key not null,
Firstname varchar(50) not null,
Lastname varchar(50) not null,
Age int not null,
Email varchar(50) not null);

describe members;


