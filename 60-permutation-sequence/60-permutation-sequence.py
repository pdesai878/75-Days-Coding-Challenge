class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def reverse(i,j):
            j-=1
            while i<=j:
                string[i],string[j]=string[j],string[i]
                i+=1
                j-=1
        
        def nextPermutation(string):
            left=None
            for i in range(n-2,-1,-1):
                if string[i]<string[i+1]:
                    left=i
                    break
            right=None
            for j in range(n-1,-1,-1):
                if string[j]>string[left]:
                    right=j
                    break
            if left!=right:
                string[left],string[right]=string[right],string[left]
                reverse(left+1,n)
                return string
            return string
        
        string=[str(i) for i in range(1,n+1)]
        for _ in range(k-1):
            string=nextPermutation(string)
        return "".join(string)
        
                       