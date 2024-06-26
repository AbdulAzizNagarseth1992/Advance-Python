# #Q1 Calculate the Area of a Rectangle:
# # x = int(input("Enter the First Value ", ))
# # y = int(input("Enter the Second Value ", ))
# # multiplication = x*y
# # print("The area of rectangle is " , multiplication)

# #Q2 Check if a Number is Even or Odd:
# num = int(input("Enter the Number: " ,))
# if(
#     (num % 2) ==0,
#     print("EVEN")
# else:
#         print("ODD")    
# )

# #Q3 Reverse a String:
# # a = input("Enter a name: " ,)[::-1]
# # print(a)

# #Q4 Find the Factorial of a Number:

# import math

# def factorial(n):
#     return(math.factorial(n))
# num = int(input("Enter the Number:" ,))
# print("Factorial of", num, "is",
#       factorial(num))

#Q5 Check if a String is Palindrome or Not:

# function to check string is
# palindrome or not
# def isPalindrome(s):

#     # Using predefined function to
#     # reverse to string print(s)
#     rev = ''.join(reversed(s))

#     # Checking if both string are
#     # equal or not
#     if (s == rev):
#         return True
#     return False

# # main function
# s = input("Enter a WORD: " ,)
# ans = isPalindrome(s)

# if (ans):
#     print("Yes")
# else:
#     print("No")

#Q6 Generate Fibonacci Series up to n terms:
# unable to do 

#Q7 Find the Largest Among Three Numbers:
# def maximum(a, b, c): 

# 	if (a >= b) and (a >= c): 
# 		largest = a 

# 	elif (b >= a) and (b >= c): 
# 		largest = b 
# 	else: 
# 		largest = c 
		
# 	return largest 


# # Driven code 
# a = int(input("Enter a Number: " ,))
# b = int(input("Enter a Number: " ,))
# c = int(input("Enter a Number: " ,))
# print(maximum(a, b, c))

#Q8 Calculate Simple Interest:
# def simple_interest(p,t,r):
# 	print('The principal is', p)
# 	print('The time period is', t)
# 	print('The rate of interest is',r)
	
# 	si = (p * t * r)/100
	
# 	print('The Simple Interest is', si)
	
	
# # Driver code
# P = int(input("Enter the principal amount :"))
# T = int(input("Enter the time period :"))
# R = int(input("Enter the rate of interest :"))
# simple_interest(P,T,R)

#Q9 Convert Celsius to Fahrenheit:
# Temperature in celsius degree
# celsius = int(input("Enter the Temperature in Celcius: " ,))

# # Converting the temperature to
# # fehrenheit using the formula
# fahrenheit = (celsius * 1.8) + 32

# # printing the result
# print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
# 	% (celsius, fahrenheit))

#Q10 Check Leap Year:
# def checkYear(year): 
# 	import calendar
# 	return(calendar.isleap(year)) 
	
# # Driver Code 
# year = int(input("Enter a YEAR: " ,))
# if (checkYear(year)): 
# 	print("Leap Year") 
# else: 
# 	print("Not a Leap Year")


#PROGRAMMING CHALLANGES
#Q1 Find the Median of Three Numbers:

# a = int(input("Enter a Number: " ,))
# b = int(input("Enter a Number: " ,))
# c = int(input("Enter a Number: " ,))

# if a > b:
#     if a < c:
#         median = a
#     elif b > c:
#         median = b
#     else:
#         median = c
# else:
#     if a > c:
#         median = a
#     elif b < c:
#         median = b
#     else:
#         median = c
# print("The median is ", median)

#Q2 Count the Number of Words in a Sentence:

# length = len("The quick brown fox jumps over the lazy dog." . split())
# print("Number of Words:" , length)

#Q3 Calculate the Sum of Digits in a Number:

# def getSum(n): 
    
#     sum = 0
#     for digit in str(n):  
#       sum += int(digit)       
#     return sum
   
# n = int(input("Enter Multiple Numbers:" ,))
# print(getSum(n))

#Q4 Find the Longest Common Prefix in a List of Strings:

# def longestCommonPrefix( a):
	
# 	size = len(a)

# 	# if size is 0, return empty string 
# 	if (size == 0):
# 		return ""

# 	if (size == 1):
# 		return a[0]

# 	# sort the array of strings 
# 	a.sort()
	
# 	# find the minimum length from 
# 	# first and last string 
# 	end = min(len(a[0]), len(a[size - 1]))

# 	# find the common prefix between 
# 	# the first and last string 
# 	i = 0
# 	while (i < end and
# 		a[0][i] == a[size - 1][i]):
# 		i += 1

# 	pre = a[0][0: i]
# 	return pre

# if __name__ == "__main__":

# 	input = ["flower" , "flow" , "flight"]
# 	print("The longest Common Prefix is :" ,
# 				longestCommonPrefix(input))

#Q5 Check if a Number is a Prime Number:

# num = int(input("Enter the Number: " ,))
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

#Q6 Find the Longest Consecutive Sequence in a List of Integers: