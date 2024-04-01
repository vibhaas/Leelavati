'''importing math module to perform basic calculations'''


import math
def square(num):
    
    num_square=0
    length_num=len(num) 
    num_array=[None]*length_num 
    
    '''getting length of the number to store each digit of the number in an array multiplied
    with it's placevalue '''
    
    
    for i in range (length_num):
        num_array[i]=(int(num[i]))*math.pow(10,length_num-i-1);
        
        
    ''' once all the digits multiplied with it's placevalue is stored in an array according to leelavati method following
    steps take place
        1.squaring of each element present in the array and adding them to variable called num_square
        2.addition of 2*last_digit*next_digit to num_square'''
    
    
    for i in num_array:
        num_square+=i**2
        
    
    for i in range(len(num_array)-1):
        for j in range(i+1,len(num_array),1):
            num_square+=2*num_array[i]*num_array[j]
            
            
    ''' returning the final answer present in num_square'''
    return num_square
