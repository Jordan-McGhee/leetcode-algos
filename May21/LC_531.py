"""

#1688
Count Matches in Tournament

You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

Example:
Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.

"""

def numberOfMatches(n):
    # establish variable to return at the end
    matches = 0

    # have a while loop that will run until we get down to 1 final team
    while n != 1:

        # if n is odd, go in this statement
        if n % 2 != 0:
            # matches will be increased by the number of teams minus one (so we don't get a decimal) divided by two
            matches += ((n-1)/2)
            # n now equals what we added to matches plus the one we subtracted from n to account for the random team
            n = (((n-1)/2)+1)
        
        # if n is even
        else:
            # matches will be increased by half the number of teams
            matches += (n/2)
            # n is now half as much because half the teams were elminated
            n = (n/2)

    # we could also just return n-1 since there will have to be that many games played, and the champion will never lose. Gets more complicated in a double-elimination tournament
    return matches

print(numberOfMatches(7))