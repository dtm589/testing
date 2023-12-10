def selection_sort(nums):
    for i, num in enumerate(nums):
        smallest_index = i
        for index in range(smallest_index + 1, len(nums)):
            if nums[index] < nums[smallest_index]:
                smallest_index = index
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]

    return nums