class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        mx=0
        for i in range(n-1):
            word1=words[i]
            for j in range(i+1,n):
                word2=words[j]
                if set(word1).intersection(set(word2)):
                    continue
                mx=max(mx,len(word1)*len(word2))
        return mx
        