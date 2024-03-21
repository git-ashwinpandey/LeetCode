import random

class RandomizedSet:
    def __init__(self):
        self.numDict = {} 
        self.numList = [] 

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.numDict:
            return False
        self.numDict[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.numDict:
            return False
        last_element, idx = self.numList[-1], self.numDict[val]
        self.numList[idx], self.numDict[last_element] = last_element, idx
        self.numList.pop()
        del self.numDict[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numList)
    

randomizedSet = RandomizedSet()
randomizedSet.insert(1)
randomizedSet.remove(2)
randomizedSet.insert(2)
randomizedSet.getRandom()
randomizedSet.remove(1)
randomizedSet.insert(2)
randomizedSet.getRandom()