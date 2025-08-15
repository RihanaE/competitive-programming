class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def inBound(r, c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])

        queue = [[sr, sc]]
        visited = set({(sr, sc)})
        org = image[sr][sc]

        while queue:
            r, c = queue.pop()
            image[r][c] = color

            for rNew, cNew in dir:
                rn = rNew + r
                cn = cNew + c

                if inBound(rn, cn) and (rn, cn) not in visited and image[rn][cn] == org:
                    queue.append([rn, cn])
                    visited.add((rn, cn))

        return image