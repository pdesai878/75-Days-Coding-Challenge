class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n=len(words)
        hashmap=defaultdict(int)
        bit=lambda ch: ord(ch)-ord('a')
        
        for word in words:
            bitmask=0
            l=0
            for ch in word:
                bitmask|=1<<bit(ch)
                l+=1
            hashmap[bitmask]=max(hashmap[bitmask],l)
           
        mx=0
        for x in hashmap:
            for y in hashmap:
                if x&y:
                    continue
                mx=max(mx,hashmap[x]*hashmap[y])
        return mx
        