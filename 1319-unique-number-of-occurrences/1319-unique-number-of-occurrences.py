from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurrences = list(count.values())
        return len(occurrences) == len(set(occurrences))