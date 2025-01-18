def binary_search(arr: list[int], target: int):
    """
    :param arr: The sorted array of numbers to perform the operation on.
    :param target: The target number to find.
    :return: The index of the number, if successful / None, if unsuccessful.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return None

lst = input("Enter your array by separating the elements with commas:\n")
target_num = int(input("Your target:\n"))

input_arr = sorted(list(map(lambda x: int(x), lst.split(", "))))

print(f"Result: {binary_search(input_arr, target_num)}")