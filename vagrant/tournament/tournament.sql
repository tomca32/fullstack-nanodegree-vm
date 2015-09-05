-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;
create database tournament;
\c tournament

create table players (
  id serial primary key,
  name text
);

create table matches (
  id serial primary key,
  players integer[],
  winner integer references players(id)
);

create view wins as select p.id as id, count(m.winner) as wins 
  from players as p left join matches as m on (p.id = m.winner) group by p.id;

create view matches_by_player as select p.id as id, count(m.players) as matches 
  from players as p left join matches as m on (p.id = any (m.players)) group by p.id;

create view player_standings as select players.id, players.name, wins, matches from players
  left join wins on (players.id = wins.id)
  left join matches_by_player on (players.id = matches_by_player.id);
