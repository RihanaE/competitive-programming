class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        store = []
        for i in popped:
            for j in pushed:
                if i not in store and j not in store:
                    store.append(j)

                if i in store:
                    temp = store.pop()
                    pushed.remove(i)

                    if i != temp:
                        return False
                    
                    break

        if store == []:
            return True