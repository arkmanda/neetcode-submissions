class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)
        group = {}

        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1

            key = tuple(freq)

            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())
                