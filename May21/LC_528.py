"""

#1603
Design Parking System

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

Example:
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

"""

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        # instantiate the class with the arguments in __init__
        self.big = big
        self.medium = medium
        self.small = small        

    def addCar(self, carType):
        # for each car type, check if there's space in the parking system. If so, subtract one space and return True. If not, return False

        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            return False
            
        if carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            return False
        
        if carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            return False


"""

#1365
How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

"""

def smallerNumbersThanCurrent(nums):
    # establish empty list to append counts to
    answer = []

    # iterate over length of nums list to grab index
    for i in range(len(nums)):
        # count variable for smaller numbers, resets with every iteration of outer for loop
        smaller = 0
        # iterate again to get each individual num
        for num in nums:
            # check if number is smaller than the number at index i
            if num < nums[i]:
                # if it is, increment smaller
                smaller += 1
        
        # append smaller to answer after iterating through each number
        answer.append(smaller)

    return answer

# print(smallerNumbersThanCurrent([8,1,2,2,3]))

"""

#1342
Number of Steps to Reduce a Number to Zero

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example:
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

"""

def numberOfSteps(num):
    # counter for number of steps before num = 0
    steps = 0
    # while loop to run continuously until num == 0
    while num != 0:
        # condition for when num is even: divide number by 2, increment steps
        if num % 2 == 0:
            num = num/2
            steps += 1
        # condition for when num is odd: subtract 1 from number, increment steps
        else:
            num -= 1
            steps += 1

    return steps

# print(numberOfSteps(14))