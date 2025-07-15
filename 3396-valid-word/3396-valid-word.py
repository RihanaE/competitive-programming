class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: 
            return False

        lsVow = [ord("a"), ord("e"), ord("i"), ord("o"), ord("u"), ord("A"), ord("E"), ord("I"), ord("O"), ord("U")]   
        req = 0
        v = False
        c = False
        for i in word:
            if 65 <= ord(i) <= 90:
                if ord(i) in lsVow:
                    if not v:
                        v = True
                        req += 1

                else:
                    if not c:
                        c = True
                        req += 1

            elif 97 <= ord(i) <= 122:
                if ord(i) in lsVow:
                    if not v:
                        v = True
                        req += 1

                else:
                    if not c:
                        c = True
                        req += 1

            elif 48 <= ord(i) <= 57:
                continue

            else:
                return False

        print(req)
        return req == 2