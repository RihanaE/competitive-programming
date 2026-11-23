class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        ans = []
        #the array after this point are all sort no need to flip it
        pointer = len(arr) - 1
        for i in range(len(arr), 1, -1):
            #Find the max number that should reside in the current range
            idx = arr.index(i)
            arr[: idx + 1] = reversed(arr[: idx + 1])
            #Put the current max at it's right place by fliping
            arr[: pointer + 1] = reversed(arr[: pointer + 1])
            ans.append(idx + 1)
            ans.append(pointer + 1)
            pointer -=1

        return ans