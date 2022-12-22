class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)
        total=sum(salary[1:n - 1])
        output=total / (n - 2)
        
        return output