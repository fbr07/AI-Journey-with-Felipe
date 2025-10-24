""" Q: Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first. """


'''def twoIntegerSum(nums, target):
    i = 0
    j = i + 1
    while i < len(nums) - 1 and j < len(nums):
        k = target - nums[i]

        if nums[j] == k:
            return [i, j]

        else:
            j += 1
    i += 1'''
    
    def twoIntegerSum(nums, target):
        
        #create our hashmap/dictionary that will store our indices as key and number as value  
        
        hashMap = {}
        
        #Python has a built-in function called enumerate that it allows you to iterates through list, tuple, dictionary or whatever and return in pair the index, value
        #Since in this problem we have keep track of what number (value) sums to target and then we need to return the indices of those numbers we will use enumerate
        for index, number in enumerate(nums):
             # I know that our target depend on i and j and we should initialize that inside the loop because are i and j will reset and be a new number after every iteration.
    


print(twoIntegerSum([3, 4, 5, 6], 7))
 