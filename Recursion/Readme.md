# Recursion

Recursion is a programming technique where a function calls itself to solve a problem. To use recursion, you need to have a problem that can be divided into smaller, similar sub-problems. You then write a function that solves the problem for a small input, and calls itself with a smaller input to solve the larger problem.
Example

Let's say you want to calculate the sum of all numbers from 1 to n:

## python_code

> def sum(n):<br/>
    if n == 1:<br/>
        return 1<br/>
    else:<br/>
        return n + sum(n-1)

In this function, the base case is when n equals 1. In this case, the function returns 1. Otherwise, the function adds n to the result of calling sum(n-1). This recursive call continues until the base case is reached.

For example, to calculate sum(4), the function first checks if n is equal to 1. Since it's not, it calculates n + sum(n-1) as 4 + sum(3). It then calls sum(3), which in turn calls sum(2), sum(1), and returns 1. The function then returns 4 + 3 + 2 + 1 = 10.

### 2 type of recursion

1. Head Recursion: In this type of recursion the recursive call is made before other processing in the function.
2. Tail Recursion: In this type of processing done before recursive call.

## Conclusion

Recursion is a powerful and elegant way to solve problems that can be broken down into smaller, similar subproblems. It is often used to traverse and manipulate data structures such as trees and graphs. To use recursion effectively, you need to identify the base case and the recursive case, and make sure the function stops calling itself when the base case is reached.