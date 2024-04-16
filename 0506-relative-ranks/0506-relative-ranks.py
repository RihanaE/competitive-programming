class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = defaultdict(int)
        ls = ["Gold Medal","Silver Medal","Bronze Medal"]
        res = []
        arr = sorted(score)
        pointer = len(arr) - 1
        rank = 4
        
        for i in ls:
            if pointer >= 0:
                dic[arr[pointer]] = i
                pointer -= 1
            
        while pointer >= 0:
            dic[arr[pointer]] = f"{rank}"
            pointer -= 1
            rank += 1
  
        for sc in score:
            
            res.append(dic[sc])
                
        return res