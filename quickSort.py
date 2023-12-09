def quick_sort(nums, low, high):
    if low < high:
        partioned_nums, i = partition(nums, low, high)
        quick_sort(nums, low, i -1)
        quick_sort(nums, i +1, high)
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return nums, i