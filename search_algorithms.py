import math

class SearchAlgorithms:
    # Initialize the list for searching and item to search
    def __init__(self,searching_list,searching_item):
        self.searching_list = searching_list
        self.searching_item = searching_item
        # Initilize length of the searching list
        self.length = len(self.searching_list)
        # Check list and search item are valid before passing them into the functions
        if not self.searching_list:
            raise ValueError("An empty list is given")
        if self.searching_item is None:
            raise ValueError("Searching item is not given")
        if not all(isinstance(self.searching_item, type(element)) for element in self.searching_list):
            raise ValueError("Searching item and list elements must be in same type. Please check !")
        print(f"Searching list is  {self.searching_list}")
        print(f"Searching item in the list is : {self.searching_item}")

    # Define linear search algorithm
    def LinearSearch(self):
        try:
            for index in range(self.length):
                if self.searching_list[index] == self.searching_item:
                    return index
            return None
        except Exception as e:
            print(f"An error occurred. Please check the inputs again. Error : {e}")
