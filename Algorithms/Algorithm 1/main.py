# Method 1 : Find the factorial of the given number
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact


number = int(input("Enter the number : "))
print(f"Factorial of {number} is : {iterative_factorial(number)}")


# Method 2
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        temp = temp * n
    return temp


number = int(input("Enter the number : "))
print(recur_factorial(number))


# Method 3
def short_recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * short_recur_factorial(n - 1)


number = int(input("Enter the number : "))
print(short_recur_factorial(number))
