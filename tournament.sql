-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
CREATE TABlE players (player_id SERIAL UNIQUE NOT NULL,
                      name TEXT );
CREATE TABLE matches (match_id SERIAL UNIQUE NOT NULL,player_1_id int, player_2_id int, winner int,loser int);
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE standings (standings_id int REFERENCES players(player_id), points integer);
