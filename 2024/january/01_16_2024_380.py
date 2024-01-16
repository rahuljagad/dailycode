'''
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # is it a dictionary of value to something (?)
        self.data_dict = {} # dictionary is used for O(1) of insert and remove
        self.data_list = [] # list is used for the GetRandom() scenario

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data_dict:
            self.data_list.append(val)
            self.data_dict[val] = len(self.data_list) - 1
            return True        
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data_dict:
            element_index = self.data_dict[val]
            last_element = self.data_list[-1]
            self.data_list[element_index] = last_element
            self.data_list.pop()
            self.data_dict[last_element] = element_index
            del self.data_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data_list)