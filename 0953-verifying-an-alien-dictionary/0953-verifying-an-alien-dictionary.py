class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for index, char in enumerate(order):
            dictionary[char] = index

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False

                elif dictionary[word1[j]] < dictionary[word2[j]]:
                    break

                elif dictionary[word1[j]] > dictionary[word2[j]]:
                    return False

        return True
