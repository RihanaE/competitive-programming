class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        longest_chain_length = {}

        max_chain_length = -1

        for word in words:
            longest_chain_length[word] = 1

            for i in range(len(word)):
                reduced_word = word[:i] + word[i + 1:]

                if reduced_word in longest_chain_length:
                    longest_chain_length[word] = max(longest_chain_length[word], longest_chain_length[reduced_word] + 1)

            max_chain_length = max(max_chain_length, longest_chain_length[word])

        return max_chain_length