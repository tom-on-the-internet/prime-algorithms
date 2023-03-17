my_array = [1, 2, 2, 1, 5]


def partition(nums: list[int], lo: int, hi: int) -> int:
    idx = lo - 1

    for i in range(lo, hi):
        val = nums[i]
        if val < nums[hi]:
            idx += 1
            tmp = nums[idx]
            nums[idx] = val
            nums[i] = tmp

    idx += 1
    nums[idx], nums[hi] = nums[hi], nums[idx]

    return idx


def quicksort(nums: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return

    pivot = partition(nums, lo, hi)

    quicksort(nums, lo, pivot - 1)
    quicksort(nums, pivot + 1, hi)


print(my_array)
quicksort(my_array, 0, len(my_array) - 1)
print(my_array)
