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

# 2. *Subtraction*

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


## Complexity

- **Time Complexity**: O(n), where n is the maximum number of digits between `a` and `b`.
- **Space Complexity**: O(n), where n is the maximum number of digits between `a` and `b`.

## Example Usage

```python
result = subtract(12345, 6789)
print(result)  # Output: 556
```
# 3. combination()

## Description

The `combination` function calculates the number of ways to choose `r` items from a set of `n` items, where the order of selection matters. The function returns an integer representing the number of combination.

## Inputs

The function `permutation` takes two integer arguments, `n` and `r`, where `n` is the total number of items and `r` is the number of items to be chosen.

## Outputs

The function returns an integer representing the number of combination of choosing `r` items from `n` items.

## Algorithm

The combinaiton algorithm is implemeted usign the following method from leelavati book 
![alt text](https://github.com/Kanishk-mittal/Project-Leelavati/blob/main/lilavati/Algebra/img/combination.png)
1. If r is greater than n, return 0.
2. If r is equal to 0 or r is equal to n, return 1.
3. Initialize a variable product to 1.
4. Iterate from i = 1 to r (inclusive):
    1. Multiply product by (n - i + 1).
    2. Divide product by i.
5. Return the value of product.


## Complexity

- **Time Complexity**: O(r)
- **Space Complexity**: O(1)

## Example Usage

```python
print(combination(5, 3))  # Output: 10
```

# 4. permutation()

## Description

The ` permutation` function calculates the number of ways to choose `r` items from a set of `n` items, where the order of selection matters. The function returns an integer representing the number of  permutation.

## Inputs

The function `permutation` takes two integer arguments, `n` and `r`, where `n` is the total number of items and `r` is the number of items to be chosen.

## Outputs

The function returns an integer representing the number of permutation of choosing `r` items from `n` items.

## Algorithm

The permutation algorithm is implemeted usign the following method from leelavati book 
![alt text](https://github.com/Kanishk-mittal/Project-Leelavati/blob/main/lilavati/Algebra/img/permutation.png)
1. If r is greater than n, return 0.
2. If r is equal to 0 or r is equal to n, return 1.
3. Initialize a variable product to 1.
4. Iterate from i = 1 to r (inclusive):
    1. Multiply product by (n - i + 1).
5. Return the value of product.


## Complexity

- **Time Complexity**: O(r)
- **Space Complexity**: O(1)

## Example Usage

```python
print(permutation(10, 3))  # Output: 20
```

# 4. sum_of_permutation()

## Description

The `sum_of_permutation` function takes a list of numbers as an input and returns the sum of all permutations of the numbers in the list.

## Inputs

The function `sum_of_permutation` takes a list of integers as input.

## Outputs

The function returns an integer representing the sum of all permutations of the numbers in the input list.

## Algorithm

- Initialize a variable number_sum to 0 to store the sum of numbers in the list.4
- Calculate the number of permutations of the list using the permutation function 
- Iterate through each number in the number_list.
- Add each number to number_sum.
- Create a string of '1's with the length equal to the number of elements in number_list.
- Convert this string to an integer (one_num) to represent the value of each permutation.
- Calculate the result as (number_of_permutations * number_sum) / len(number_list) * one_num.


## Complexity

- **Time Complexity**: O(n), where n is the number of elements in the list 
- **Space Complexity**: O(1)

## Example Usage

```python
print(sum_of_permutation([1, 2, 3]))  # Output: 1332
```

# 5.square()

# description
The method for obtaining the square according to Lilavati's technique offers a rapid solution while also presenting a distinctive and traditional approach to address the problem.
## input
we take only integers as an input for this function any other number shall raise error

## output
we obtain square of the corresponding input

## logical Explanation
1. Split the given input number as each digit and place it in an array whose length is number of digits present in the number.

2. for each digit stored in the array multiply the digit with it's corresponding place value and store in the same array again in the same position.

3. we have to run two loops through the array which we have
    3.1.The first loop iterates        through whole array while squaring each number present in the array and adding it and storing the obtained result in an variable called num_square

    3.2. The second loop consist of nested loops.Let the first loop iterate from array[0] to len(array)-1 as i.

    3.3. let the nested loop of second loop iterate from array[i+1] to len(array) as j.while iterating we generate value for 2*array[i]*array[j] and add it to the num_square variable.

    3.4. This iteration is done until i does'nt reach len(array)-1 value.

    3.5. for decimal point numbers we shift the decimal point to the end of the number such that the number becomes a whole number and find the square for it and return the user with the square value of that number by placing the decimal point in appropriate position.  

4. hence the obtained answer is stored in num_square value and returned to the user.
## Algorithm
The square algorithm is implemented using the following method from leelavati book
![alt text](https://github.com/Project-Leelavati/Leelavati/blob/main/lilavati/Algebra/img/square.png)

# 6.cube()
# description
The method for obtaining the cube according to Lilavati's technique offers a rapid solution while also presenting a distinctive and traditional approach to address the problem.
## input
we take only integers as an input for this function any other number shall raiseerror

## output
we obtain cube of the corresponding input

## logical Explanation
leelavati follows a particular method to find a cube of a number it involves 4 steps
    1.initially separate the number into 2 parts one is the least significant digit part and other digits as one number
    ex:if we are finding cube for number 125 separate it as 12 and 5
    2.here comes 4 steps to find the cube of the number(example to find cube for 125)
        2.1.cube the number separated from LSG i.e 12 and multiply with 1000 let it be x=1728*1000 
        2.2.now find 3*(x*x)*LSG*100--> 3*(12*12)*5*100
        2.3 find 3*(x)*(LSG*LSG)*10-->3*(12)*(5*5)*10
        2.4 find cube of LSG
    3.now add all the numbers obtained in 2.1,2.2,2.3,2.4 hence you will get the required number 
    4.for decimal point numbers we shift the decimal point to the end of the number such that the number becomes a whole number and find the cube for it and return the user with the cube value of that number by placing the decimal point in appropriate position.  

## Algorithm
The cube algorithm is implemented using the following method from leelavati book
![alt text](https://github.com/Project-Leelavati/Leelavati/blob/main/lilavati/Algebra/img/cube.png.png)

# 7.square root()  
# description
The square-root method given in leelavati gives a unique method to find square-root of given input it involves some complex mechanism but faster way to solve the problem mentally.
## input
we take only integers as an input for this function any other number shall raiseerror

## output
we obtain square root of the corresponding input

## logical Explanation
note:leelavati's method is distinguished for two type for numbers one which has odd number of digits and
other for even number of digits leelavati's method involves 3 steps which is used repeatedly until the answer is not found
1.find the length of the number and classify it as number with odd number of digits or even number of digits.

2.for the number whose length is odd number the most significant digit is a single digit subtract the single digit with
highest number which has a perfect square root and let that difference be d and the square root of that number be x and concatenate it in variable root_num_double.

3.In next step take concatenate the MSB digit with the next digit i.e x+next.digit and subtract it with 2*x*y where y is a variable
which will decide the appropriate digit to be used when 2*x*y is subtracted from x+next.digit(let that difference be d1) we don't get a negative number
also y that we obtain should be such that (y*y) should be less than d1 concatenated wit next digit

4.let d=d1 and x=y repeat process 3 and 4 to obtain the answer.

5.After every fourth step concatenate y in root_num_double.

6.note for the number whose length is even number the first 2 digits are considered as MSB and the same process is follows as step 2 3 and 4

## Algorithm
The square root algorithm is implemented using the following method from leelavati book
![alt text](https://github.com/Project-Leelavati/Leelavati/blob/main/lilavati/Algebra/img/squareroot.png-1.png)

# 8.cube root() 
# Description
The cube-root method given in leelavati gives a unique method to find cube_root of given input it involves 
some complex mechanism but faster way to solve the problem mentally.
## input
we take only integers as an input for this function any other number shall raise error

## output
we obtain cube root of the corresponding input

## logical Explanation
note:leelavati's cube_root method is distinguished for 3 type of numbers
1.the length of number exactly divisible by 3(ex length:3,6,9)
2.the length of number when divisible by 3 leaves remainder as one(ex length:4,7,10)
3.the length of number when divisible by 3 leaves remainder as two(ex length:5,8,11)

2.for the number whose length is 3n+1  the most significant digit(left-most digit) is a single digit subtract the single digit with the
highest number which has a perfect cube root and let that difference be d and the cube root of that number be x and concatenate it in variable called cube_of_num.

3.In next step concatenate the Most Significant digit with the next digit i.e x+next.digit and subtract it with 3*(x^2)*y where y is a variable
which will decide the appropriate digit to be used when 3*(x^2)*y is subtracted from x+next.digit(let that difference be d1) we don't get a negative number(i.e d1 is not negative) and
also y, that we obtain should be such that 3*x*(y^2) should be less than d1 concatenated with next digit

4.After obtaining 3*x*(y^2) concatenate it with the next-digit and subtract that number with y^3  the obtained difference should 
be positive and let it be d2 and now let d=d2,x=y and repeat the process 3 and 4 to obtain the answer.

5.note after every 4th step concatenate y obtained in cube_of_num variable 

6.note for the number whose length is 3n the first 3 digits are considered as MSB and for numbers having length 3n+2 the first 2 numbers are MSB and then same process is follows as step 2 3 and 4

## Algorithm
The cube root algorithm is implemented usi tnghe following method from leelavati book
![alt text](https://github.com/Project-Leelavati/Leelavati/blob/main/lilavati/Algebra/img/cube_root.png.png)