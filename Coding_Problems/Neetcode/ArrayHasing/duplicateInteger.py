# Q: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


def duplicate(nums):
    """My thought  process is to create a dictionary that will store the value in nums. If that value is already in the dictionary than that means
    that the value appears more than once"""

    # create dictionary hashMap
    numOccurences = {}

    for number in nums:
        if number in numOccurences:
            return True

        else:
            numOccurences[number] = 1

    return False


# print(duplicate([1, 2, 3, 3]))

print(duplicate([1, 2, 3, 1, 2, 3]))
