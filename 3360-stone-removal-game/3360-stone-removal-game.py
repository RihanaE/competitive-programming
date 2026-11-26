class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        turn = 0 # 0 for alice 1 for bob

        while n > 0:
         
            if n - remove > 0:
                if turn == 0:
                    turn = 1
                else:
                    turn = 0

            elif n - remove == 0:
                if turn == 0:
                    return True

                return False

            else:
                if turn == 0:
                    return False

                return True

            n -=remove
            remove -=1