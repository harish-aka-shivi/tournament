# Tournament
Database design for swiss styles tournament. Written in python. Its uses postgres Sql for database operations
Swiss Style tournament has different method of selecting a winner. No one is elminated and almost everyone winns atleast one match.

## **Structure of project:**
* tournament.sql has all the table creation files
* tournament.py has all the function which deals with database and returns the approprate outputs. 
* tournament_test.sql has been provided as a part of Udacity course : Intro to Relational Databases. Its has test cases to     	 validate the database operations.

## **Example of a 16 Player Swiss Tournament:**
First round pairing is by random draw. For example, with 16 players they would be matched into 8 random pairs for the first round. 
For now, assume all games have a winner, and there are no draws.
## After the first round, 
* there will be a group of 8 players with a score of 1 (win), 
* and a group of 8 players with a score of 0 (loss). 
* For the 2nd round, players in each scoring group will be paired against each other – 1’s versus 1’s and 0’s versus 0’s.

## After round 2, there will be three scoring groups:
* 4 players who have won both games and have 2 points
* 8 players who have won a game and lost a game and have 1 point
* 4 players who have lost both games and have no points.

## Again, for round 3, players are paired with players in their scoring group. After the third round, 
  the typical scoring groups will be:
* 2 players who have won 3 games (3 points)
* 6 players with 2 wins (2 points)
* 6 players with 1 win (1 point)
* 2 players with no wins (0 points)

## For the fourth (and in this case final) round, the process repeats, and players are matched with others in their scoring group. 
* Note that there are only 2 players who have won all of their games so far – 
* they will be matched against each other for the "championship" game.
* After the final round, we’ll have something that looks like this:
* 1 player with 4 points – the winner!
* 4 players with 3 points – tied for second place
* 6 players with 2 points
* 4 players with 1 point
* 1 player with 0 points 

