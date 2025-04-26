def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the target value.

    Args:
        arr (list): A list of sorted elements (ascending order).
        target (any): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found the target, return index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


# Example usage
if __name__ == "__main__":
    sample = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(sample, target)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
