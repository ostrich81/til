--주석 
/* 여러줄 주석 ㅗㅗㅗ 
    ㅗㅗㅗㅗㅗㅗㅗㅗ
    기본 문법 -변하지 않는 부분- 대문자 
    변하는 부분 - 소문자 
*/ 
-- 데이터 전체조회는 select 
SELECT * FROM examples;
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT
);
-- 테이블 삭제 
DROP TABLE classmates;

create table classmates(
name TEXT,
age INT,
address TEXT
);

SELECT* FROM classmates;
-- 데이터 입력 
INSERT INTO classmates(name,age) VALUES('홍길동',23);
INSERT INTO classmates VALUES('홍길동',23,'서울');
SELECT* FROM classmates;
SELECT rowid,* FROM classmates;
--테이블 삭제 
DROP TABLE classmates;

create table classmates(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
INSERT INTO classmates VALUES('홍길동',23,'서울');
--error 
INSERT INTO classmates VALUES(1,'홍길동',23,'서울');
INSERT INTO classmates(name,age,address) VALUES('홍길',72,'지방');

DROP TABLE classmates;

create table classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('홍길동',30,'서울'),
('김철수',30,'대전'),
('이서피',26,'광주'),
('서댜서',88,'규미'),
('최조주',34,'뷰산');

SELECT rowid,name from classmates;
SELECT rowid,name from classmates limit 1;
SELECT rowid,name from classmates limit 1 offset 4;
SELECT rowid,name from classmates where address ='서울';
SELECT DISTINCT age from classmates;
DELETE from classmates where rowid =5;
insert into classmates VALUES('최조주',34,'뷰산');
update classmates set name ='홍길순', address='제주도' where rowid=5;

create table users(
first_name text not null,
last_name text not null,
age integer not null,
country text not null,
phone text not null,
balance integer not null
);
select *from users where age>=30;
select first_name from users where age>=30;
select age,last_name from users where age>=30 and last_name='김';

select count (*) from users; 
select avg(age) from users where age>=30;
select first_name,max(balance) from users;
select avg (balance) from users where age>=30;
select * from users where age like '2_';
select * from users where phone like '02%';
select * from users where first_name like '%준';
select * from users where phone like '%5114%';

select * from users order by age asc limit 10;
select * from users order by age ,last_name  limit 10;
select last_name, first_name from users order by balance desc limit 10;

select last_name, count(*) from users group by last_name;
select last_name, count(*) AS name_count from users group by last_name;

create table articles(
title text not null,
content text not NULL
);

insert into articles VALUES('1번제목','1번내용');

alter table articles RENAME to news;

alter table news add column created_at text ;
insert into news values ('제목','내용',datetime('now'));

select *from news;

alter table news add column subtitle text not null DEFAULT '임쉬제목' ;
--1
create table countries(
room_num TEXT NOT NULL,
check_in text NOT NULL,
check_out text NOT NULL,
grade text NOT NULL,
price integer NOT NULL
);
--2
INSERT INTO countries VALUES
('B203',2019-12-31,2020-01-03,'suite',900),
('1102',2020-01-04,2020-01-08,'suite',850),
('303',2020-01-01,2020-01-03,'deluxe',500),
('807',2020-01-04,2020-01-07,'superior',300);
--3
alter table countries rename to hotels;
--4
select room_num,price from hotels order by price desc limit 2;
--5
select grade ,count(*) as pass from hotels group by grade order by pass desc;
--6
select * from hotels where room_num like'B%' or grade ='deluxe';
--7
select * from hotels where room_num not like'B%' and check_in=2020-01-04 order by price ;

