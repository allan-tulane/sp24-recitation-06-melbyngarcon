def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """  
    if n <= 1:
      return n
    counts[n] += 1
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
# Check if the nth Fibonacci number has already been computed
  if fibs[n] != -1:
    return fibs[n]

# Base case: if n is 0 or 1, return n
  if n <= 1:
    fibs[n] = n
  else:
    # Compute the nth Fibonacci number by summing the (n-1)th and (n-2)th Fibonacci numbers
    # and store it in the fibs list for future reference
    fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)

  return fibs[n]


def fib_bottom_up(n):
    # Initialize a list of n + 1 values to 0, to store the Fibonacci sequence up to Fn
    fibs = [0] * (n + 1)

    # Base cases: F0 _= 0, F1 = 1
    if n > 0:
        fibs[1] = 1

    # Iteratively compute each Fibonacci number from 2 up to n
    for i in range(2, n + 1):
        fibs[i] = fibs[i-1] + fibs[i-2]

    # Return the nth Fibonacci number
    return fibs[n]




def fib_bottom_up_better(n):
    ###TODO
    pass
