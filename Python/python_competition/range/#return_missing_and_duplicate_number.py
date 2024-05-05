#return_missing_and_duplicate_number.py
def find_mismatch(nums):
    nums_set = set(nums)
    duplicate = -1
    missing = -1
    
    for num in range(1, len(nums) + 1):
        if num not in nums_set:
            missing = num
        if nums.count(num) > 1:
            duplicate = num
            
    return [duplicate, missing]
