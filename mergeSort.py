def merge_sort(nums):
    if len(nums) < 2:
        return nums
    middle = len(nums) // 2
    left_side = nums[0:middle]
    right_side = nums[middle:]
    sorted_left_side = merge_sort(left_side)
    sorted_right_side = merge_sort(right_side)
    sorted_list = merge(sorted_left_side, sorted_right_side)
    return sorted_list

def merge(first, second):
    final_list_of_integers = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final_list_of_integers.append(first[i])
            i += 1
        else:
            final_list_of_integers.append(second[j])
            j += 1

    final_list_of_integers.extend(first[i:])
    final_list_of_integers.extend(second[j:])

    return final_list_of_integers