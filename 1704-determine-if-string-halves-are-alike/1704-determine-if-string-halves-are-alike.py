class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def vowels(string):
            v=0
            for ch in string:
                if ch in {"a","e","i","o","u"}:
                    v+=1
            return v
        
        mid=len(s)//2
        return vowels(s[:mid].lower())==vowels(s[mid:].lower())
        