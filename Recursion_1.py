def Sum(nums):
    if len(nums) == 2:
        return nums[0] + nums[1]

    return Sum([nums[0], Sum(nums[1:])])

print(Sum([1,2,3,4,5]))