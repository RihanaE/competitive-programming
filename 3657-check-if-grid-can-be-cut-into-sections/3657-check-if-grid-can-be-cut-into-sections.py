class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        yInterval = []
        xInterval = []

        for i in rectangles:
            yInterval.append([i[1], i[-1]])
            xInterval.append([i[0], i[2]])

        xInterval.sort()
        yInterval.sort()

        countX = 0
        preX = -1
        preY = -1
        countY = 0

        for i in range(len(xInterval)):
            if preX <= xInterval[i][0]:
                countX += 1
            preX = max(xInterval[i][1], preX)

            if preY <= yInterval[i][0]:
                countY += 1
            preY = max(yInterval[i][1], preY)
            
            # if i == 0:
            #     if xInterval[i][1] <= xInterval[i + 1][0]:
            #         countX += 1

            #     if yInterval[i][1] <= yInterval[i + 1][0]:
            #         countY += 1

            # elif i == len(xInterval) - 1:
            #     if xInterval[i][0] >= xInterval[i - 1][1]:
            #         countX += 1

            #     if yInterval[i][0] >= yInterval[i - 1][1]:
            #         countY += 1

            # else:
            #     if (xInterval[i - 1][1] <= xInterval[i][0] or xInterval[i][0] == xInterval[i - 1][0]) and xInterval[i][1] <= xInterval[i + 1][0]:
            #         countX += 1

            #     if (yInterval[i - 1][1] <= yInterval[i][0] or yInterval[i][0] == yInterval[i - 1][0]) and yInterval[i][1] <= yInterval[i + 1][0]:
            #         countY += 1
                
        # print(xInterval)
        # print(yInterval)
        # print(countX)
        # print(countY)


        return countX >= 3 or countY >= 3