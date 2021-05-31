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

# print(numberOfMatches(7))

"""

#1859
Sorting the Sequence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

"""

def sortSentence(s):
    # split the s into a list so we can iterate over each word
    lst = s.split()
    
    # use enumerate to iterate, for each word, use slicing to move the number to the front of the word. Update the word at each index with the new words we created
    for i, word in enumerate(lst):
        word = word[-1] + word[:len(word)-1]
        lst[i] = word
    
    # sort the list with the numbers in front
    lst.sort()
    
    # iterate using enumerate again, use slicing to remove the number from the front of each word. Update the word at each index with the words missing the numbers
    for i, word in enumerate(lst):
        word = word[1:]
        lst[i] = word

    # return a new sentence using join
    return " ".join(lst)

# print(sortSentence("is2 sentence4 This1 a3"))


"""

#709
To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example:
Input: s = "Hello"
Output: hello

"""

def toLowerCase(s):
    # Easy problem. Use the lower function
    return s.lower()

"""

#1816
Truncate Sentence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

Example:
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

"""

def truncateSentence(s,k):
    # split up the given string into a list
    lst = s.split()

    # use join to create our truncated sentence, slicing off the words that come after k
    return " ".join(lst[:k])

# print(truncateSentence("Hello how are you Contestant", 4))

"""

#1732
Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

"""

def largestAltitude(gain):
    # establish two variables, one a running total we will iterate over. The other we will use to keep track of the highest altitude we have reached
    altitude = 0
    highest = 0

    # iterate over every number in gain and add it to altitude
    for num in gain:
        altitude += num

        # if altitude is greater than our current highest after adding a number, update highest to be our current altitude
        if altitude > highest:
            highest = altitude

    return highest

# print(largestAltitude([-5,1,5,0,-7]))