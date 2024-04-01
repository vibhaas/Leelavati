# Combination Calculation Algorithm

## Overview
The combination calculation algorithm is used to determine the number of ways to choose `r` items from a set of `n` items without regard to the order of selection. This is often referred to as "n choose r" or the binomial coefficient and is denoted as `nCr`.

## Algorithm
The combinaiton algorithm is implemeted usign the following method from leelavati book 
![alt text](image.png)

## Logical Explaination
- The first row represent number of ways in which 1 can be selected and having selected 1 , 2 can be selected and so on 
- The second row represent the orders in which they are selected
- The third row inplies that since the order of selection is immaterial, they are removed by respective division
- The last row represent the succesive products whic are the actual number of combination of selecting 1,2,3.... at a time from n items

## Complexity
The time complexity of the combination calculation algorithm is O(n) and the space complexity is O(1).

# Permutation Calculation Algorithm
It is same as combination calculation algorithm but the only difference is that the order of selection is important so we removed the division part from the algorithm and we got the permutation calculation algorithm

## sum_of_permutation
The above funciton takes an array of intigers as input and returns the sum of all the permutation of the array using following algorithm
1) First it calcualte the sum of all numbers in the array and save it in a variable number_sum
2) Then it creates a number with the length of the array and all the digits are 1
3) Finally, it computes the result by multiplying the number of permutations with the sum of the input list and dividing by the length of the list
