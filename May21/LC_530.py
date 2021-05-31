"""

#1221
Split a String Into Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

Example:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.


"""

def balancedStringSplit(s):
    # we need two variables, one to return the total number of balances, and the second, a variable we will change depending on if if the character we iterate over is an L or an R
    total = 0
    balance = 0

    # iterate over every character
    for char in s:
        # if the character is an L, we'll subtract 1 from balance
        if char == "L":
            balance -= 1

            # if balance == 0, we'll increment total. This means that there would have to be as many Rs as Ls to bring the balance back down to zero. 
            if balance == 0:
                total += 1

        # do the same thing for R, except we increment balance instead of subtracting 1
        if char == "R":
            balance += 1
            if balance == 0:
                total += 1

    return total

# print(balancedStringSplit("RLRRLLRLRL"))

"""

#1832
Check if the Sentence is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

"""

def pangramCheck(sentence):
    # establish variable with all letters in alphabet
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # iterate over every character in alpha
    for char in alpha:
        # if char in sentence, continue to next char
        if char in sentence:
            continue

        # else, return False and stop loop
        else:
            return False

    return True

# print(pangramCheck("thequickbrownfoxjumpsoverthelazydog"))


"""

#1614
Maximum Nesting Depth of Parentheses

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

Example:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

"""

def maxDepth(s):
    # create two variables, one that we'll return as our answer at the end, and the other to be a running count of open or closed parentheses
    maximum = 0
    count = 0

    # iterate over every character
    for char in s:
        
        # if we get an open parentheses, incrememnt our count variable
        if char == "(":
            count += 1

            # check if count is greater than maximum, if so, maximum = our new count
            if count > maximum:
                maximum = count

        # if we get a closed parentheses, decrement our count variable
        elif char == ")":
            count -= 1

    return maximum

# print(maxDepth("(1+(2*3)+((8)/4))+1"))