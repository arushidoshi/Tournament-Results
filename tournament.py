#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Connection failed")


@contextmanager
def get_cursor():
    """
    Query helper function using context lib. Creates a cursor from a database
    connection object, and performs queries using that cursor.
    """
    DB = connect()
    c = DB.cursor()
    try:
        yield c
    except:
        raise
    else:
        DB.commit()
    finally:
        c.close()
        DB.close()


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as c:
        c.execute("DELETE FROM Matches;")


def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as c:
        c.execute("DELETE FROM Players;")


def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as c:
        c.execute("SELECT count(id) FROM Players;")
        rows = c.fetchall()
        return rows[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as c:
        c.execute("INSERT INTO Players (name) VALUES (%s)", (name, ))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as c:
        c.execute("SELECT * FROM Standings ORDER BY won DESC;")
        results = c.fetchall()
        # If the top two results are equal
        # then check by overall wins on matches played
        if (results[0][2] != 0) and (results[0][2] == results[1][2]):
            c.execute("SELECT * FROM Standings"
                      " ORDER BY (cast(won AS DECIMAL)/total_matches) DESC;")
            results = c.fetchall()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as c:
        c.execute("INSERT INTO Matches (winner, loser) VALUES (%s,%s)",
                  (winner, loser,))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    with get_cursor() as c:
        c.execute("SELECT id,name,won FROM Standings ORDER BY won DESC;")
        rows = c.fetchall()
        i = 0
        pairings = []
        while i < len(rows):
            id1 = rows[i][0]
            name1 = rows[i][1]
            id2 = rows[i+1][0]
            name2 = rows[i+1][1]
            pairings.append((id1, name1, id2, name2))
            i = i + 2

    return pairings
