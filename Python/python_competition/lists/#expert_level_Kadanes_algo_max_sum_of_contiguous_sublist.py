#expert_level_Kadanes_algo_max_sum_of_contiguous_sublist
def max_sublist_sum(nums):

    for i in range(len(nums)):
        current_sum = 0
        max_sum = max(nums)

        for x in nums:
            current_sum += x
            if current_sum > max_sum:
                max_sum = current_sum
            elif current_sum < 0:
                current_sum = 0

    return max_sum