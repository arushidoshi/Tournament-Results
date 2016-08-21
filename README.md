# Tournament-Results
submitted by [Arushi Doshi](https://github.com/arushidoshi), for completing the fourth project of :
[Full-Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004)

## About This project

A Database schema to store details of matches played between pairs of players. It ranks players in a game as per the Swiss ranking module, i.e no elimination.
Players are matched in subsequent matches as per their score in previous matches.

## Files 

**tournament.py** -- _Contains the implementation for the Swiss tournament_ 

**tournament.sql** -- _Contains the SQL queries to create the database, tables and views_  

**tournament_test.py** -- _Contains the test cases for tournament.py_  

## Prerequisites 

1. Download [Virtual Box](https://www.virtualbox.org/wiki/Downloads) to run the virtual machine
2. Download the latest build of [Vagrant](https://www.vagrantup.com/downloads.html)
3. Fork [this](https://github.com/arushidoshi/Tournament-Results) repository and download it on your computer

## Instructions

1. To start Vagrant
  1. Open Terminal or cmd and browse to the vagrant folder
  2. Type `vagrant up`
2. SSH into the vagrant VM
  1. In the same terminal type `vagrant ssh`
3. Change to the correct folder
  1. Type `cd /vagrant/tournament`
4. To run the tournament.sql 
  1. type `psql`
  2. type \i tournament.sql
  3. type `\q` to quit out of PSQL 
5. To run the tests
  1. In the terminal type `python tournament_test.py`

## Expected Outcome
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!

## License
The content of this repository is licensed under [MIT License](https://opensource.org/licenses/MIT)
