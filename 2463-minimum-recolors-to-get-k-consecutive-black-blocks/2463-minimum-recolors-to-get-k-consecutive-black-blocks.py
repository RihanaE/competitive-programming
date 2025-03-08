class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        numBlack = 0
        left = 0
        right = 0
        operation = len(blocks) + 1

        while right < len(blocks):
            if blocks[right] == "B":
                numBlack += 1
            right += 1

            if numBlack == k:
                return 0

            if right - left == k:
                operation = min(operation, k - numBlack)
                if blocks[left] == "B":
                    numBlack -= 1
                
                left += 1

            

        return operation