"""script: power.py
   action: a. get and validate user inputs for a base and power
           b. computes the exponential expression 
           c. prints the outcome to the user
   author: Mat Bakarich
   date:   03/31/2025
"""

# define recursive function
def power(base, exponent):
    """Calculate the value of an exponent expression. 
        action: calculate the expnoential expression for base^power    
        input: none
        output: none    
        paramaters:
            base (int): an integer
            exponent (int): a non-negative integer
            
        return: a recursive call to the function unless the base case is met or until the base case is met            
    """
    if exponent == 1:
       return base
    if exponent > 1:
        return power(base, exponent-1) * base
    if exponent == 0:
        return 1

    
# user program
def exponent():
    """Calculate and print the value of an exponent expression. 
    action: prompt user to input base and power
            validate user inputs
            call power() function and pass inputs as arguments
    input: base (int): an integer for the base
           base (int): a postive intrger for the exponent
    output: print the value of the exponential expression
    return: none
    """
  
    # get and validate base
    while True:
        try:
            your_base = (input("Please enther the base. "))
            your_base = int(your_base)
            break
           
        except ValueError:
            print("Base must be an integer.")
        
       
    # get and validate exponent
    while True:    
        try:
            your_exponent = input("Please enter the exponent. ")
            your_exponent = int(your_exponent)
            if your_exponent >= 0:
                break
            else:print("No negative exponents.")
        except ValueError:
            print("Exponent must be an integer.")


    # call power function and pass inputs, store the result in a variable
    your_answer = power(your_base,your_exponent)
    
    # print the answer
    print(f"\n{your_answer}")

# call exponent function
exponent()