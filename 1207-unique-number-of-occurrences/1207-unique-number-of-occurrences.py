class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        s=set()
        for key,freq in c.items():
            if freq in s:
                return False
            s.add(freq)
        return True
        