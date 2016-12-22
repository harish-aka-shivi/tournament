#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db =  psycopg2.connect("dbname=tournament")
        return db
    except Exception as e:
        print "what the hell!!!"


def deleteMatches():
    """Remove all the match records from the database."""
    connection = connect()
    c  = connection.cursor();
    query = "DELETE FROM matches;"
    c.execute(query);
    connection.commit();

    query1 = "UPDATE standings SET matches = %s,wins = %s ;"
    c.execute(query1,(0,0));
    connection.commit();
    connection.close

def deletePlayers():
    """Remove all the player records from the database."""
    connection = connect()
    c  = connection.cursor();
    query = "DELETE FROM players;"
    c.execute(query);
    connection.commit();
    connection.close


def countPlayers():
    """Returns the number of players currently registered."""
    connection = connect()
    c  = connection.cursor();
    query = "SELECT count(*) from players;"
    c.execute(query);
    result = c.fetchall();
    connection.commit;
    connection.close
    print "result is ",result
    print "result[0][0] is --> " , result[0][0]
    return result[0][0]


def registerPlayer(name):
    """Returns the number of players currently registered."""
    connection = connect()
    c  = connection.cursor();
    query = "INSERT INTO players (name) VALUES (%s);"
    #print "insert query in register player is -->",query
    c.execute(query,(name,));
    connection.commit();

    query1 = "INSERT INTO standings (standings_id,name,wins,matches) VALUES ((SELECT player_id from players where name = %s),%s,0,0);"
    #print "insert query1 in register player is -->",query1

    c.execute(query1,(name,name));
    connection.commit();

    connection.close;

    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """


def playerStandings():

    db = connect();
    c = db.cursor();
    query = "SELECT * from standings ORDER BY wins DESC;"
    c.execute(query);
    result = c.fetchall();
    db.commit;
    db.close;
    print result;
    return result


    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):

    db = connect();
    cursor = db.cursor();
    query = "INSERT into matches (match_id,winner_id,loser_id) VALUES (DEFAULT,%s,%s);"
    cursor.execute(query,(winner,loser));
    db.commit();


    query1 = "UPDATE standings SET wins = wins + %s,matches = matches + %s where standings_id = %s;"
    cursor.execute(query1,(1,1,winner));

    query1 = "UPDATE standings SET matches = matches + %s where standings_id = %s;"
    cursor.execute(query1,(1,loser));

    db.commit();

    db.close;


    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


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
