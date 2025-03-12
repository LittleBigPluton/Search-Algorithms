# Search-Algorithms
Search algorithm implementation with Python

## Table of Contents
- [Required Libraries](#required-libraries)
- [Installation](#installation)
- [Methods](#methods)
- [Usage](#usage)
- [Contribution](#contribution)
- [References](#references)

## Required Libraries
This project uses two standard Python libraries:
- `math`: Used for mathematical calculations.
- `random`: Used for generating random test cases.
Since these are built-in Python libraries, no additional installation is required.


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
4. To execute the main script, use the following command:
```bash
python3 main.py
```

## Methods
### Linear Search[(1)](https://en.wikipedia.org/wiki/Linear_search)
#### Theory
Linear search algorithm is a straightforward method. The element that needs to be found is sequentially checked with each element of the list until a match is found or the list ends. In the worst-case scenario, when the desired element is at the end of the list or does not exist, the linear search makes n comparisons. For the best-case scenario, the target element is in the first place. The linear search algorithm has O(n) time complexity, which is reasonable. In the following table, there is an illustration of given list with indexes. The searching value is -20. The algorithm starts to check with element at the first index, which is 46 in this scenario. Because there is no match in the first comparison, he algorithm moves to the next element to compare. This process keeps going until a match found or reaching end of the list.

|Index       |0 |1  |2  |3|4|5|6|7|8|9|
|------------|:-:|:-:|:-:|-|-|-|-|-|-|-|
|List        |46|11|-20|55|75|22|73|-90|-85|98|
|1.comparison|**46 ?= -20**| | | | | | | | | |
|2.comparison||**11 ?= -20**| | | | | | | | |
|3.comparison|||**-20 ?= -20**| | | | | | | |

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
To handle errors correctly, the try-except block is implemented to the linear search algorithm. If function could not find any match, it returns a None value by printing a message. Also, for any unexpected error, the function returns None instead of crashing.  
