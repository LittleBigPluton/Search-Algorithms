# Sarch-Algorithms
Search algorithm implementation with Python

## Table of Contents
- [Required Libraries](#required-libraries)
- [Installation](#installation)
- [Methods](#methods)
- [Usage](#usage)
- [Contribution](#contribution)
- [References](#references)

## Required Libraries
Two standard libraries are used in this python project, math and random. No additional library installation needed.

## Installation
1. Open terminal (Linux,macOS)/command panel (Windows)
2. Clone the repository:
```bash
git clone https://github.com/LittleBigPluton/Search-Algorithms.git
```
3. Change directory:
```bash
cd Search-Algorithms
```
4. To run the python script on terminal/cmd:
```bash
python3 main.py
```

## Methods
### Linear Search[(1)](https://en.wikipedia.org/wiki/Linear_search)
#### Theory
Linear search algorithm is a straightforward method. The element that needs to be found is sequentially checked with each element of the list until a match is found or the list ends. In the worst-case scenario, when the desired element is at the end of the list or does not exist, the linear search makes n comparisons. For the best-case scenario, the target element is in the first place. The linear search algorithm has O(n) time complexity, which is reasonable. In the following table, there is an illustration of given list with indexes. The searching value is -20. The algorithm starts to check with element at the first index, which is 46 in this scenario. Because there is no match in the first comparison, the algorithm go to next element to compare. This process keeps going until a match found or reaching end of the list.

|Index|0|1|2|3|4|5|6|7|8|9|
|-----|:-:|:-:|:-:|-|-|-|-|-|-|-|
|List |46|11|-20|55|75|22|73|-90|-85|98|
|1.comparison|46 ?= -20| | | | | | | | | |
|2.comparison||11 ?= -20|||||||||
|3.comparison|||-20 ?= -20||||||||

#### Application
The linear search algorithm is really simple to apply and use. Every iteration of the list element with a for loop is examined whether they are desired element or not.
```python
try:
  for index in range(self.length):
    if self.searching_list[index] == self.searching_item:
      return index
  print(f"The item {self.searching_item} is not in the list.")
  return None
except Exception as e:
  print(f"An error occurred. Please check the inputs again. Error : {e}")
  return None
```
To handle errors correctly, the try-except block is implemented to the linear search algorithm. If function could not find any match, it returns a None value by printing a message. Also, for any unexpected error, the function return None value rather than executing itself.  

### Binary Search [(2)](https://en.wikipedia.org/wiki/Binary_search)

#### Theory

Binary search is a more efficient searching algorithm that works on sorted lists. It follows the divide-and-conquer approach by repeatedly dividing the list in half and comparing the middle element to the target. If the middle element matches the target, it is returned. Otherwise, the algorithm decides whether to continue searching in the left or right half of the list. Therefore, the searching list needs to be sorted. The best-case time complexity is O(1) when the element is in the middle. The worst and average time complexities are O(log n). Th following illustration shows how the binary search works. Because Binary search needs sorted list, first the list should be ordered. Then, the list is divided into two from the middle point.


|Index|0  |1  |2  |3 |4 |5 |6 |7  |8  |9 |
|-----|---|---|---|--|--|--|--|---|---|--|
|List |46 |11 |-20|55|75|22|73|-90|-85|98|


|Index       |0   |1   |2  |3 |4 |5 |6 |7  |8  |9 |
|------------|----|----|---|--|--|--|--|---|---|--|
|Sorted List |-90 |-85 |-20|11|22|46|55|73 |75 |98|

Then, the Binary search algorithm starts to look at the middle element in the list and compare if it smaller or bigger than target element. After the decision, the algorithm look left or right half of the list as an individual list and repeat the procedure again until found the target element.

|Step |Left |Right |Mid |Mid Element |Comparison |Action                       |
|-----|-----|------|----|------------|-----------|-----------------------------|
|1    |0    |9     |4   |22          | -20 < 22  | Search left half `right = 4`|
|2    |0    |4     |2   |-20         | -20 = -20 | Found at index 2




#### Application
The Binary search must to work on sorted list so the list is checked if sorted or not. If not, the list is sorted. Then, the middle point of the is calculated by making an integer division by 2. Variable `left` is assigned beginning of the list and variable `right` one is assigned to the end of the list. Later, element at this middle point is checked if it is smaller, bigger or equal to the searching item. As a result of this examination, either the function return to the current searching position or taking the left half of the list by assigning `right` variable to left side of the searching point or moving with the right half of the list by assigning `left` variable to the right side of the searching position. Then, the whole procedure is repeated with this side of the given list until searching element be found.
```python
try:
  # Check the given list is sorted or not
  if not sorted(self.searching_list) == self.searching_list:
    print("Given list is not sorted. To perform Binary search, it is sorted.")
    self.searching_list.sort()
    left,right = 0,self.length-1

  while left<=right:
    # Decide middlie point of the looking section of the sorted list
    searching_position = (left+right)//2
    # Check middle element of the list if it is searching item or not
    if self.searching_item == self.searching_list[searching_position]:
      return (self.searching_list,searching_position)
    # Check searching item if it is near to the left or not
    elif self.searching_item < self.searching_list[searching_position]:
      right = searching_position - 1
    else:
      left = searching_position + 1

  # If the item is not found, return this
  print(f"{self.searching_item} is not in the list.")
  return (self.searching_list, None)
except Exception as e:
  print(f"An error occurred: {e}")
  return (self.searching_list, None)
```
To handle the errors, same try-except block method used here as well. If there is an unexpected error or the item is not found, the function return None value rather than stopping.
