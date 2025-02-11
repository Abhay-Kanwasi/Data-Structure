# If a positive integer is entered through the keyboard, write a recursive function to obtain the prime factors of the number.

def prime_factors(n, div = 2):
   if n ==1:
       return
   if n % div == 0:
       print(div, end=" ")
       prime_factors(n // div, div)
   else:
       prime_factors(n, div+1)

# number = int(input("Enter a number: "))
# print(f'Prime factors of {number} are: ', end="")
# prime_factors(number)
# print("\n")

# A positive integer is entered through the keyboard, write a recursive function to calculate sum of digits of the 5-digit number.

def calculate_sum(n):
    if n == 0:
        return 0
    else:
        new_rem = n % 10
        n = int(n / 10)
        sums = new_rem + calculate_sum(n)
        return sums


print(calculate_sum(23456))






