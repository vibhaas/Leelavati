from typing import List

def calculate_combinations(n: int, r: int) -> int:
    """
    Calculate the number of combinations of n things taken r at a time (nCr).

    Parameters:
    n (int): Total number of items.
    r (int): Number of items to choose.

    Returns:
    int: The number of combinations.
    """
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    product = 1
    for i in range(1, r + 1):
        product *= n - i + 1
        product //= i

    return product

# Example usage:
# print(calculate_combinations(5, 3))  # Output: 10
def calculate_permutations(n: int, r: int) -> int:
    """
    Calculate the number of permutations of n things taken r at a time (nPr).

    Parameters:
    n (int): Total number of items.
    r (int): Number of items to choose.

    Returns:
    int: The number of permutations.
    """
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    product = 1
    for i in range(r-1):
        product *= n - i # n * (n-1) * (n-2) * ... * (n-r+1)
    return product

# Example usage:
# print(calculate_permutations(5, 3))  # Output: 20

def sum_of_permutation(number_list: List)->int:
    """
    Calculate the sum of all permutations of a given list of numbers.

    Parameters:
    number_list (List): List of numbers.

    Returns:
    int: The sum of all permutations.
    """
    number_sum=0
    for i in number_list:
        number_sum+=i
    one_num=int("1"*len(number_list))
    number_of_permutations=calculate_permutations(len(number_list),len(number_list))
    return ((number_of_permutations*number_sum)/len(number_list))*(one_num)
