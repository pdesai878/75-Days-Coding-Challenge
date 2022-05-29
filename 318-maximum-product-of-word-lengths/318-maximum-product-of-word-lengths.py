class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n=len(words)
        mask=[0]*n
        length=[0]*n
        bit=lambda xh: ord(ch)-ord('a')
        ind=0
        for word in words:
            bitmask=0
            l=0
            for ch in word:
                bitmask|=1<<bit(ch)
                l+=1
            mask[ind]=bitmask
            length[ind]=l
            ind+=1
        mx=0
        for i in range(n-1):
            for j in range(i+1,n):
                
                if mask[i]&mask[j]:
                    continue
                mx=max(mx,length[i]*length[j])
        return mx
        