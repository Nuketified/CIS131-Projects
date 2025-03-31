# Exponent calculator

# define recursive function
def power(base, exponent):
    """Calculate the value of an esponent expression. 
            
            Paramaters:
                base (int): an integer
                exponent (int): a non-negative integer
            
            Returns:
                a recursive call to the function unless the base case is met or until the base case is met            
    """
    if exponent == 1:
       return base
    if exponent > 1:
        return power(base, exponent-1) * base
    if exponent == 0:
        return 1

    
# user program
def exponent():
    """Calculate and print the value of an exponent expression. Get then validate user inputs to ensure no negative esponents are passed to the power() function.
    
    
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

    # call power function and pass inputs
    your_answer = power(your_base,your_exponent)
    # print the answer
    print(f"\n{your_answer}")

# call exponent function
exponent()