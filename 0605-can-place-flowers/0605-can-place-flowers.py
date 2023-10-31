class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) % 2 == 0:
            if sum(flowerbed) + n > len(flowerbed) // 2:
                return False
            
        else:
            if sum(flowerbed) + n > (len(flowerbed) // 2) + 1:
                return False
            
        
        pointer = 0
        while n != 0:
            if pointer + 1 < len(flowerbed) and pointer == 0 and flowerbed[pointer] == 0 and flowerbed[pointer + 1] == 0:
                flowerbed[pointer] += 1
                n -= 1
             
                
            elif pointer - 1 >= 0 and pointer == len(flowerbed) - 1 and flowerbed[pointer] == 0 and flowerbed[pointer - 1] == 0:
                flowerbed[pointer] += 1
                n -= 1
              
                
            else:
                if pointer - 1 >= 0 and pointer + 1 < len(flowerbed) and flowerbed[pointer - 1] == 0 and flowerbed[pointer] == 0 and flowerbed[pointer + 1] == 0:
                    flowerbed[pointer] += 1
                    n -= 1
            
                elif pointer - 1 < 0 and pointer + 1 >= len(flowerbed) and flowerbed[pointer] == 0:
                    flowerbed[pointer] += 1
                    n -= 1
                    
            pointer += 1
            
            if n == 0:
                return True
            
            elif pointer >= len(flowerbed):
                return False
            
        return True