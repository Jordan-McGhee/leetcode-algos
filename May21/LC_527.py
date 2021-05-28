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
    sums = []
    total = 0

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


