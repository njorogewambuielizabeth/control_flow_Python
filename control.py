# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50.
def even_numbers():
    x=0
    while x<=50:
        if x%2==0:
             x+=1
             continue
        print(x)
        x+=2
            
            
            
#Write a function that takes an integer argument and 
# "Prime" if the number is prime, and
# "Not prime" if the number is not prime            
def is_prime(num):
    if num < 2:
        print("Not prime")
        
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Not prime")
            
    print("Prime")
    
    #Write a function that takes a list of integers as input and 
    # prints the sum of all the even numbers in the list. 
def sum_of_even(list):
    sum=0
    for i in list:
        if i%2==0:
            sum+=i
            print(sum)
           
# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers between the two 
# integers (inclusive) that are divisible by 3.

def sum_divisible_by_3(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1  
    
    divisible_sum = 0
    for num in range(num1, num2+1):
        if num % 3 == 0:
            divisible_sum += num
    
    print("The sum of all numbers between", num1, "and", num2, "that are divisible by 3 is:", divisible_sum)
    
                
    
        
        


              
               