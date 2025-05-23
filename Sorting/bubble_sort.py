def bubble_sort(arr):
    """
    Perform bubble sort on a list to sort elements in ascending order.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array:", bubble_sort(sample))
