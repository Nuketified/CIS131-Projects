def fibonacci(n):
    """Calculate the nth Fibonacci number and track the total number of function calls.
       Returns a tuple where the first element is the Fibonacci number and the second element is
       the total number of function calls made to fibonacci().
    """
   
    if n in (0, 1): # base cases
        return n, 1
           
    else:
        f1, n1 = fibonacci(n - 1) 
        f2, n2 = fibonacci(n - 2)
        return f1 + f2, n1 + n2 + 1
               
    
# call Fibonacci and store the result.
fib_10 = fibonacci(10)
fib_20 = fibonacci(20)
fib_30 = fibonacci(30)

# print Fibonacci number and number of function calls.
print(f"fibonacci(10) = {fib_10}")
print(f"fibonacci(20) = {fib_20}")
print(f"fibonacci(30) = {fib_30}")