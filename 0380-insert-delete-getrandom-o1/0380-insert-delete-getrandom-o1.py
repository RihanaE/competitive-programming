class RandomizedSet:

    def __init__(self):
        self.sets = set()
        

    def insert(self, val: int) -> bool:
        if val in self.sets:
            return False
        
        self.sets.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.sets:
            return False
        
        self.sets.remove(val)
        return True
        

    def getRandom(self) -> int:
        lst = list(self.sets)
        return random.choice(lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()