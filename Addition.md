# Arithmetic

# *1. Addition*

## Description

The `add` function takes any number of integer arguments (`*args`), representing the numbers to be added column-wise. These integers can be positive, negative, or zero. The function adds these numbers column-wise as if they were aligned on the right side (like in addition) and returns the sum.

## Inputs

The function `add` takes any number of integer arguments. These arguments represent the numbers to be added column-wise.

## Outputs

The function returns an integer, which represents the sum of the numbers added column-wise.

## Algorithm

1. Find the maximum length of the input numbers by iterating through each number in `args` and finding the length of the string representation of each number.
2. Create a list of lists called `sum_columns`, where each inner list represents a column and contains the digits of the numbers at that column position, reversed. If a number is shorter than the maximum length, pad the digits with zeros.
3. Calculate the sum of each column by summing up the digits at each position in `sum_columns`.
4. Compute the final result by iterating through the sums of each column, multiplying each sum by 10 raised to the power of its column position, and adding them together.
5. Return the final result.

## Process

![WhatsApp Image 2024-04-06 at 13 58 17_2225b16b](https://github.com/Aditya-AG7/Leelavati/assets/147618452/5ed8ea9f-10b4-45a1-b6fe-92ba0e37df0c)

## Complexity

- **Time Complexity**: O(n), where n is the total number of digits across all input numbers.
- **Space Complexity**: O(n), where n is the total number of digits across all input numbers.

## Example Usage

```python
result = add(1234, 2341, 1234, 134, 3251, 531465, 1346)
print(result)  # Output: 963, 852, 741
```

*# 2. Subtraction*

## Description

The `subtract` function takes two integers `a` and `b` and performs subtraction. It returns an integer representing the result of the subtraction.

## Inputs

The function `subtract` takes two integer arguments, `a` and `b`, which are the numbers to be subtracted.

## Outputs

The function returns an integer representing the result of the subtraction.

## Algorithm

1. Convert the input numbers `a` and `b` into lists of digits.
2. Ensure that `num1` (representing the larger number) is at least as long as `num2`.
3. Pad the shorter list `num2` with leading zeros if necessary.
4. Iterate through the digits of `num1` and `num2` from right to left.
5. Perform subtraction for each pair of digits, taking borrow into account if necessary.
6. Store the result digits in a list.
7. Remove any leading zeros from the result list.
8. Convert the result list back to an integer.
9. Return the result integer.

## Process

Shown in the image along with addition.

## Complexity

- **Time Complexity**: O(n), where n is the maximum number of digits between `a` and `b`.
- **Space Complexity**: O(n), where n is the maximum number of digits between `a` and `b`.

## Example Usage

```python
result = subtract(12345, 6789)
print(result)  # Output: 556

