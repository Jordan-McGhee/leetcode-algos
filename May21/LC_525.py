"""
#1431
Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

Example 1
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.

"""

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    test = []
    maximum = max(candies)
    for kid in candies:
        if kid + extraCandies >= maximum:
            test.append(True)
            continue

        test.append(False)

    return test

# print(kidsWithCandies([2,3,5,1,3], 3))

"""
#628
Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
Example 1:
Input: nums = [1,2,3]
Output: 6

"""

def maximumProduct(nums):

    nums.sort()

    # With the list sorted, we can grab the first two numbers, which if they're negative, multiplying them together might give us a larger product than just multiplying the three largest positive numbers
    test1 = nums[:2]+nums[len(nums)-1:] 

    # Grab the three largest positive numbers just in case their product is larger than the numbers in test1
    test2 = nums[len(nums)-3:]
    
    # Create our variables to multiply our numbers by for comparison
    product1 = 1
    product2 = 1

    #iterate over nums in test1 and 2, multiplying them by product1 and 2 respectively
    for num in test1:
        product1*=num

    for num in test2:
        product2 *= num

    #return the larger of the two products
    return max([product1, product2])

# print(maximumProduct([1,2,3]))
# print(maximumProduct([1,2,3,4]))
# print(maximumProduct([-100,-98,-1,2,3,4]))

"""

#1
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]

"""

def twoSum(nums, target):
    # create dictionary for values in nums that we will test
    tested = {}

    # iterate over nums with enumerate to track their indices as well
    for i, num in enumerate(nums):

        # subtract num from target to find possible pair
        possible = target - num

        # if possible is in our dictionary of tested numbers, return the value of tested[possible] as the first index, and i from our current iteration for the second
        if possible in tested:
            return [tested[possible], i]
        
        # if possible was not in tested yet, add the num as a key to tested with its index as its value
        tested[num] = i

    # if we reach this point, there is no solution. Returns an empty list
    return []
    

print(twoSum([11,15,2,7], 9))