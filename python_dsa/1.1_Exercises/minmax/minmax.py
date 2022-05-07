from numpy import iterable


def minmax(nums: iterable(int or float)) -> tuple:
    """
    ### Takes in an iterable of numbers and returns the largest and smallest elements
    
    Args:
        iterable: containing int or float values

    Returns:
        tuple: smallest and largest number
    """

    if len(nums) == 0:
        print("Empty iterable")
        return

    min = nums[0]
    max = nums[0]

    for n in nums:
        if n < min:
            min = n
        if n > max:
            max = n

    return min, max


print(minmax(range(-10, 1000)))
