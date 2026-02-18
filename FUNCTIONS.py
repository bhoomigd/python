# %%
#1.CHECK IF ODD OR EVEN
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(4))


# %%
def factorial(n):
    if n<0:
     return "factorial not defined for negative numbers"
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(3))


# %%
#3. Write a function that takes a string and returns the reversed string.
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# %%
#4. Write a function that checks whether a number is prime.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n*0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

# %%
#5. Write a function that takes a list of numbers and returns the largest number.
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
print(find_largest([1, 27, 2, 10, 25]))


# %%
#6. Write a function that takes a list and returns the sum of all elements without using the built-in sum() function.
def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(list_sum([1, 2, 3, 4]))

# %%
#7. Write a function that counts the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count
print(count_vowels("My peace"))

# %%
#8. Write a function that returns the Fibonacci sequence up to n terms.
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(8))

# %%
#9. Write a function that checks whether a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("rare"))


# %%
#10. Write a function that takes two numbers and returns their greatest common divisor (GCD).
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(20, 40))


# %%
#11. Write a function that removes duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))


# %%
#12. Write a function that takes a list of numbers and returns a new list containing only even numbers.
def get_even_numbers(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
print(get_even_numbers([1, 2, 8, 4, 5, 6]))


# %%
#13. Write a function that finds the frequency of each character in a string.
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(char_frequency("hello"))


# %%
#14. Write a function that swaps two numbers without using a third variable.
def swap_numbers(a, b):
    a, b = b, a
    return a, b
print(swap_numbers(5, 10))


# %%
#15. Write a function that converts a temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(celsius_to_fahrenheit(25))


# %%



