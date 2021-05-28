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
    new_lst = []

    for i in range(len(nums)//2):
        new_lst.append(nums[i])
        new_lst.append(nums[i+n])

    return new_lst

# print(shuffle([2,5,1,3,4,7], 3))