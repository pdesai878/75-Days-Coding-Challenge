class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(res):
            if len(res)==n:
                ans.append(res)
                return
                
            for i in range(n):
                if visited[i]:
                    continue
                visited[i]=True
                solve(res+[nums[i]])
                visited[i]=False
                
                
        ans=[]
        n=len(nums)
        visited=[False for i in range(n)]
        solve([])
        return ans
                
        
        
        