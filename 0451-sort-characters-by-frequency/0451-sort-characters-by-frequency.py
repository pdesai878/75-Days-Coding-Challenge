class Solution:
    def frequencySort(self, s: str) -> str:
        dicti=Counter(s)
        res=""
        for key,freq in sorted(dicti.items(),key=lambda items: items[1], reverse=True):
            res+=(key)*freq
        return res
        
        