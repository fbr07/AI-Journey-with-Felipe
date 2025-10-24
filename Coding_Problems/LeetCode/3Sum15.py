def threeSum(nums):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Write your code here.
    nums.sort()
    triplets = []

    i = 0
    while i < len(nums) - 2:
        if i > 0 and nums[i] == nums[i - 1]:
            i += 1
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]

            if sum == 0:
                triplets.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif sum < 0:
                j += 1
            else:
                k -= 1

        i += 1

    return triplets


print(threeSum([-1, 0, 1, 2, -1, -4]))
