def merge_sort(input_lst):
    # Check if there's anything to sort
    if len(input_lst) <= 1:
        return input_lst
    
    # Split the list at the midpoint
    mid = len(input_lst) // 2

    # Recursive call to sort the left subarray
    left = merge_sort(input_lst[:mid])
    # Recursive call to sort the right subarray
    right = merge_sort(input_lst[mid:])

    # Call the merge function to merge the sorted subarrays
    return merge(left, right)

def merge(left, right): 
    merged_lst = [] # Initialize empty list
    indx = 0 # Initialize left index
    jndx = 0 # Initialize right index

    # Merge the left and right subarrays
    while indx < len(left) and jndx < len(right):
        # Append element from the left subarray
        if left[indx] < right[jndx]:
            merged_lst.append(left[indx])
            indx += 1 # Progress to the next index
        # Append element from the right subarray
        else:
            merged_lst.append(right[jndx])
            jndx += 1 # Progress to the next index

    # Add remaining elements from the left and right subarrays
    merged_lst.extend(left[indx:])
    merged_lst.extend(right[jndx:])

    return merged_lst
