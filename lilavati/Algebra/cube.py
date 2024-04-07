'''leelavati follows a particular method to find a cube of a number it involves 4 steps
    1.initially separate the number into 2 parts one is the least significant digit part and other digits as one number
    ex:if we are finding cube for number 125 separate it as 12 and 5
    2.here comes 4 steps to find the cube of the number(example to find cube for 125)
        2.1.cube the number separated from LSG i.e 12 and multiply with 1000 let it be x=1728*1000 
        2.2.now find 3*(x*x)*LSG*100--> 3*(1728*1728)*5*100
        2.3 find 3*(x)*(LSG*LSG)*10-->3*(1728)*(5*5)*10
        2.4 find cube of LSG
    3.now add all the numbers obtained in 2.1,2.2,2.3,2.4 hence you will get the required number '''
    
        

def cube(num):
    
    num_length=len(str(num))
    cube_num=0
    if(num_length==1):
        return num*num*num
    else:
        arr=[None]*2
        arr[0]=int(num/10)
        arr[1]=num%10
        for i in range (4):
            if(i==0):
                cube_num+=cube(arr[0])*1000
            elif(i==1):
                cube_num+=3*(arr[0]**2)*arr[1]*100
            elif(i==2):
                cube_num+=3*(arr[0])*(arr[1]**2)*10
            else:
                cube_num+=cube(arr[1])
        
    return cube_num

number=int(input())
print(cube(number))
    
'''note:algorithm only for int type number not for any other data type'''