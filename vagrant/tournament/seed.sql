\c tournament
insert into players (name) values ('Ann Annah');
insert into players (name) values ('Bob Bobby');
insert into players (name) values ('Charlie Charl');
insert into players (name) values ('Donnie Don');

insert into matches (players, winner) values ('{1, 2}', 1);
insert into matches (players, winner) values ('{3, 4}', 3);
insert into matches (players, winner) values ('{1, 3}', 1);
insert into matches (players, winner) values ('{2, 4}', 2);