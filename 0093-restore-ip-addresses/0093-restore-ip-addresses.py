class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        res = []

        def backtrack(no_dots, pointer, ip):
            if no_dots == 4 and pointer == len(s):
                res.append(ip[:-1])
                return

            if no_dots > 4:
                return

            for i in range(pointer, min(pointer + 3, len(s))):
                num = int(s[pointer:i + 1])
                if 0 <= num <= 255 and (pointer == i or s[pointer] != '0'):
                    backtrack(no_dots + 1, i + 1, ip + str(num) + '.')

        backtrack(0, 0, '')
        return res
