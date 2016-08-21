-- Table definitions for the tournament project.

-- Drop tournament database if it exists
DROP DATABASE IF EXISTS tournament;

-- Create Database 'Tournament'
CREATE DATABASE tournament;

-- Connect to the tournament database
\connect tournament

-- Players Table
CREATE TABLE Players (
    id SERIAL primary key,
    name varchar(255)
);

-- Matches Table
CREATE TABLE Matches (
    id SERIAL primary key,
    winner int references Players(id),
    loser int references Players(id)
);

-- Standings View shows number of wins and matches for each Player
CREATE VIEW Standings AS
SELECT Players.id, Players.name,
(SELECT count(*) FROM Matches WHERE Matches.winner = Players.id) as won,
(SELECT count(*) FROM Matches WHERE Players.id in (winner, loser)) as total_matches
FROM Players
GROUP BY Players.id;
