#!/usr/bin/python3
import random
import search_algorithms

# Initialize length of the list
length = 10

# Create a random integer list to test functions
list = [random.randint(-100,100) for _ in range(length)]

# Select a integer randomly inside list
search_item = list[random.randint(0,length-1)]

# Create object
list_1 = search_algorithms.SearchAlgorithms(list,search_item)

# Call linear search algorithm
print("Linear search is called")
print(f"Index of searching item is {list_1.LinearSearch()}")

# Call binary search algorithm
print("Binary search is called")
result_BinarySearch = list_1.BinarySearch()
print(f"Searching list is {result_BinarySearch[0]} and Index of searching item is {result_BinarySearch[1]}")

# Call jump search algorithm
print("Jump search algorithm is called")
result_JumpSearch = list_1.JumpSearch()
print(f"Searching list is {result_JumpSearch[0]} and Index of searching item is {result_JumpSearch[1]}")

# Call Fibonacci search
print("Fibonacci search algorithm is called")
result_FibonacciSearch = list_1.FibonacciSearch()
print(f"Searching list is {result_FibonacciSearch[0]} and Index of searching item is {result_FibonacciSearch[1]}")
