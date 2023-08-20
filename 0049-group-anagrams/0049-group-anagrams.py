class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = []
        for i in range(len(strs)):
            store.append([sorted(strs[i]), i])
            
        store.sort()
            
        ans = []
        pointer = 0
        
        while pointer < len(strs):
            temp = [strs[store[pointer][1]]]
            pointer += 1
            
            while pointer < len(strs) and store[pointer][0] == store[pointer - 1][0]:
                temp.append(strs[store[pointer][1]])
                pointer += 1
                
            ans.append(temp)
            
        return ans