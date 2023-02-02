class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        if len(skill) == 2:
            return skill[0] * skill[1]
        
        chem = 0
        prev = skill[0] + skill[-1]
        left_p = 0
        right_p = len(skill) - 1
        
        while left_p < right_p:
            if skill[left_p] + skill[right_p] == prev:
                chem += skill[left_p] * skill[right_p]
                
            else:
                return -1
            
            left_p += 1
            right_p -= 1
            
        return chem