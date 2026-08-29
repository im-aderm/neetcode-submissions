class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return None

        return self.chars_counts(s) == self.chars_counts(t)

    def chars_counts(self, s: str) -> dict:
        characters = {}
        for char in s:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        return characters