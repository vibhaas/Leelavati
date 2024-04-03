import math
def cube_root(num):
    cube_of_num=""
    duplicate=num
    len_of_num=len(str(num))
    if len_of_num%3==1:
        for i in range (len_of_num):
            digit=int(duplicate/math.pow(10,len_of_num-i-1))
            if(i==0):
                j=1
                while(j*j*j<=digit):
                    j+=1
                j-=1
                duplicate=duplicate-(j*j*j)*math.pow(10,len_of_num-i-1)
                cube_of_num+=str(j)
                continue
            
            elif(i%3==1):
                k=1
                while(3*(int(cube_of_num)*int(cube_of_num))*k<=digit):
                    k+=1
                    
                while True:
                    k-=1
                    second_term_number=3*((int(cube_of_num))**2)*k
                    duplicate1=duplicate-second_term_number*math.pow(10,len_of_num-i-1)
                    digit1=int(duplicate1/math.pow(10,len_of_num-i-2))
                    break
                
                while((3*(int(cube_of_num))*(k**2))>digit1):
                    k-=1
                    second_term_number=3*((int(cube_of_num))**2)*k
                    duplicate1=duplicate-second_term_number*math.pow(10,len_of_num-i-1)
                    digit1=int(duplicate1/math.pow(10,len_of_num-i-2))
                    
                duplicate=duplicate1
                
            elif(i%3==2):
                third_term_number=3*(int(cube_of_num))*(k**2)
                duplicate=duplicate-third_term_number*math.pow(10,len_of_num-i-1)
                
            else:
                duplicate=duplicate-(k*k*k)*math.pow(10,len_of_num-i-1)
                cube_of_num+=str(k)
                continue
    
    elif(len_of_num%3==0):
         for i in range (len_of_num-2):
            digit=int(duplicate/math.pow(10,len_of_num-i-3))
            if(i==0):
                j=1
                while(j*j*j<=digit):
                    j+=1
                j-=1
                duplicate=duplicate-(j*j*j)*math.pow(10,len_of_num-i-3)
                cube_of_num+=str(j)
                continue
            
            elif(i%3==1):
                k=1
                while(3*(int(cube_of_num)*int(cube_of_num))*k<=digit):
                    k+=1
                    
                while True:
                    k-=1
                    second_term_number=3*((int(cube_of_num))**2)*k
                    duplicate1=duplicate-second_term_number*math.pow(10,len_of_num-i-3)
                    digit1=int(duplicate1/math.pow(10,len_of_num-i-4))
                    break
                
                while((3*(int(cube_of_num))*(k**2))>digit1):
                    k-=1
                    second_term_number=3*((int(cube_of_num))**2)*k
                    duplicate1=duplicate-second_term_number*math.pow(10,len_of_num-i-3)
                    digit1=int(duplicate1/math.pow(10,len_of_num-i-4))
                    
                duplicate=duplicate1
                
            elif(i%3==2):
                third_term_number=3*(int(cube_of_num))*(k**2)
                duplicate=duplicate-third_term_number*math.pow(10,len_of_num-i-3)
                
            else:
                duplicate=duplicate-(k*k*k)*math.pow(10,len_of_num-i-3)
                cube_of_num+=str(k)
                continue
            
    else:
        for i in range (len_of_num-1):
            digit=int(duplicate/math.pow(10,len_of_num-i-2))
            if(i==0):
                j=1
                while(j*j*j<=digit):
                    j+=1
                j-=1
                duplicate=duplicate-(j*j*j)*math.pow(10,len_of_num-i-2)
                cube_of_num+=str(j)
                continue
            
            elif(i%3==1):
                k=1
                while(3*(int(cube_of_num)*int(cube_of_num))*k<=digit):
                    k+=1
                    
                while True:
                    k-=1
                    second_term_number=3*((int(cube_of_num))**2)*k
                    duplicate1=duplicate-second_term_number*math.pow(10,len_of_num-i-2)
                    digit1=int(duplicate1/math.pow(10,len_of_num-i-3))
                    break
                
                while((3*(int(cube_of_num))*(k**2))>digit1):
                    k-=1
                    second_term_number=3*((int(cube_of_num))**2)*k
                    duplicate1=duplicate-second_term_number*math.pow(10,len_of_num-i-2)
                    digit1=int(duplicate1/math.pow(10,len_of_num-i-3))
                    
                duplicate=duplicate1
                
            elif(i%3==2):
                third_term_number=3*(int(cube_of_num))*(k**2)
                duplicate=duplicate-third_term_number*math.pow(10,len_of_num-i-2)
                
            else:
                duplicate=duplicate-(k*k*k)*math.pow(10,len_of_num-i-2)
                cube_of_num+=str(k)
                continue
            
    return float(cube_of_num)


print(cube_root(125))
print(cube_root(166375))
print(cube_root(970299))
                
                    