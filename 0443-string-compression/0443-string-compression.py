class Solution:
    def compress(self, chars: List[str]) -> int:
        o = ""
        l, r = 0, 1
        check = 1
        count=0

        while r <= len(chars):
            if r <len(chars) and chars[l] == chars[r]:
                check += 1
                r += 1

            else:
                o = o + f"{chars[l]}"
                if check > 1:
                    o = o + f"{check}"

                l = r
                r += 1
                check = 1

        for i in o:
            chars[count]=i
            count+=1

        return count

