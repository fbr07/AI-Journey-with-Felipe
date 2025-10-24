"""Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first."""


def twoSum(nums, target):
    dictionary = {}
    """Since in this problem we are both accessing the index and number in nums we have to use enumerate Python. Enumerate in Python
    creates an enumerator object that produces (index,value)"""
    for index, number in enumerate(nums):
        missingNumber = target - number
        if missingNumber in dictionary:
            return [dictionary[missingNumber], index]
        else:
            dictionary[number] = (
                index  # So in here we are stating the the dictionary, key is value
            )


print(twoSum([3, 4, 5, 6], 7))
