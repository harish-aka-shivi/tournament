-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
CREATE TABlE players (player_id SERIAL UNIQUE NOT NULL,
                      name TEXT );
CREATE TABLE matches (match_id SERIAL UNIQUE NOT NULL, winner_id int,loser_id int);
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE standings (standings_id int REFERENCES players(player_id) ON DELETE CASCADE,name TEXT ,wins integer,matches integer);
