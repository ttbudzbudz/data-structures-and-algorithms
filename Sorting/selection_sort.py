def selection_sort(arr):
    """
    Perform selection sort on a list to sort elements in ascending order.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print("Sorted array:", selection_sort(sample))
