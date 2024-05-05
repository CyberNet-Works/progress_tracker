
def two_sum(nums, target):
    num1 = 0
    num2 = 0
    index1 = 0
    index2 = 0

    for x in nums:
        for y in nums:
            if x + y == target:
                num1 = x
                num2  = y

    for index, number_match in enumerate(nums):
        if number_match == num1:
            index1 = index
    
    for index, number_match in enumerate(nums):
        if number_match == num2:
            index2 = index

    if nums[0] == nums[1]:
        index2 = 0

    return [index2, index1]
    