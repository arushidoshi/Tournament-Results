-- Table definitions for the tournament project.

-- Drop tournament database if it exists
DROP DATABASE IF EXISTS tournament;

-- Create Database 'Tournament'
CREATE DATABASE tournament;

-- Connect to the tournament database
\connect tournament

-- DROP old Tables
DROP TABLE IF EXISTS Players CASCADE;
DROP TABLE IF EXISTS Matches CASCADE;

-- Players Table
CREATE TABLE Players (
    id SERIAL primary key,
    name varchar(255)
);

-- Matches Table
CREATE TABLE Matches (
    id SERIAL primary key,
    winner int references Players(id),
    loser int references Players(id),
    result int
);

-- Wins View shows number of wins for each Player
CREATE VIEW Wins AS
    SELECT Players.id, COUNT(Matches.winner) AS won
    FROM Players
    LEFT JOIN (SELECT * FROM Matches WHERE result>0) as Matches
    ON Players.id = Matches.winner
    GROUP BY Players.id;

-- Count View shows number of matches for each Player
CREATE VIEW Count AS
    SELECT Players.id, Count(Matches.loser) AS match_played
    FROM Players
    LEFT JOIN Matches
    ON Players.id = Matches.winner
    GROUP BY Players.id;

-- Standings View shows number of wins and matches for each Player
CREATE VIEW Standings AS
    SELECT Players.id,Players.name,Wins.won,Count.match_played
    FROM Players,Count,Wins
    WHERE Players.id = Wins.id and Wins.id = Count.id;
