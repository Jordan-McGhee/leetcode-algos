"""

#1480
Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example: 

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""

def runningSum(nums):
    # create empty list to append to and running total
    sums = []
    total = 0

    # iterate over every num in nums, adding that num to total, then appending total
    for num in nums:
        total += num
        sums.append(total)

    return sums

# print(runningSum([1,2,3,4]))

"""

#1108
Defanging and IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

"""

def deFangIPAddr(address):
    # return address.replace('.','[.]')

    # OR

    return "[.]".join(address.split('.'))

# print(deFangIPAddr("1.1.1.1"))


"""

#1470
Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example: 
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

"""

def shuffle(nums, n):
    # Create empty list to return at the end
    new_lst = []

    # iterate over half the length of nums due to algo constraints
    for i in range(len(nums)//2):

        # basically split the list in half, append the num at the ith index of nums, then append the num at the i+nth index of nums. Constraints made it clear n would be the halfway point, so we don't have to worry about an out of range error
        new_lst.append(nums[i])
        new_lst.append(nums[i+n])

    return new_lst

# print(shuffle([2,5,1,3,4,7], 3))

"""

#1672
Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Example:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

"""

def maximumWealth(accounts):
    # every list in the main list is a different customer
    # every item in that list needs to be summed up to account for their wealth
    # keep track of customer and their wealth with dictionary
    wealth_dict = {}
    max_wealth = 0

    # iterate over every customer in list and create key in dictionary
    for i in range(len(accounts)):
        wealth_dict[i] = 0
        # iterate over account in list and add to that customer's total
        for account in accounts[i]:
            wealth_dict[i] += account
    
    # iterate over values, have variable that tracks largest value
    for value in wealth_dict.values():
        if value > max_wealth:
            max_wealth = value
    
    # return that variable
    return max_wealth

# print(maximumWealth([[1,2,3],[3,2,1]]))