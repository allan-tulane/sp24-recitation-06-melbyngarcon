# CMPS 2200 Recitation 06
## Answers

**Name:**___________Miles Bartholomew Gail III
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work W(n) of the recursive algorithm for computing the nth Fibonacci number F_n can be defined by the recurrence relation W(n) = W(n-1) + W(n-2) + C, where C is a constant. For base cases n = 0 and n = 1, W(n) = C. This leads to an exponential growth in work, closely mirroring the Fibonacci sequence itself, and making the algorithm's complexity approximately O(phi^n), where phi is the golden ratio (approximately 1.618). Without optimizations like memoization or dynamic programming, this recursive approach is highly inefficient for large n.

- **3)** The span S(n) of the recursive algorithm for computing the nth Fibonacci number represents the parallel time complexity, given by the recurrence relation S(n) = S(n-1) + C, assuming the two recursive calls can be made in parallel and C is the constant work for each operation. For the base cases n = 0 and n = 1, S(n) = C. This leads to a linear growth in the span, making the algorithm's parallel complexity O(n), indicating that the parallel time complexity increases linearly with n. The parallel execution significantly improves efficiency over serial recursion by leveraging concurrency, though it still requires optimization for large-scale computations.

- **4)**
inspecting the counts list, which tracks the number of times the fib_recursive function is called for each Fibonacci number, an interesting pattern of the Fibonacci sequence itself emerges in the counts. Each entry in the counts list represents the total calls made to compute its corresponding Fibonacci number, revealing that the number of calls for each position n closely follows the pattern of the Fibonacci sequence. This illustrates the exponential growth in the number of function calls for increasing values of n, highlighting the inefficiency of the recursive approach without memoization. The pattern underlines the recursive nature of the Fibonacci calculation, where each call spawns further calls in a manner directly tied to the sequence's properties.


- **6)**
using the fib_top_down function, fib_top_down(i) for any value i will be called at most once due to memoization, which stores the result of each computation and prevents duplicate calculations. Therefore, the work of this algorithm is O(n), as it computes each Fibonacci number up to n exactly once. The span, or parallel time complexity, of this algorithm remains O(n) because the deepest chain of recursive calls determines the overall time, even if parallel computation is used. This demonstrates a significant efficiency improvement over the basic recursive approach by reducing both the work and span to linear complexity.

- **8)** 
using the fib_bottom_up function, each Fibonacci number F_i for any value i will be read at most twice by the subsequent Fibonacci calculations. The work of this algorithm is O(n), as it iteratively computes each Fibonacci number up to n exactly once. The span, or parallel time complexity, of this algorithm is O(n) due to the sequential nature of the iteration. This efficient iterative approach ensures minimal reads and writes, making it highly efficient for computing large Fibonacci numbers.


