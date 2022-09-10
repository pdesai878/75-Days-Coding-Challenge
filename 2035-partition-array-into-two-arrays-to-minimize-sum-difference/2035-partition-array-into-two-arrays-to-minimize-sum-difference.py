class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2      
        ans = abs(sum(nums[:N]) - sum(nums[N:]))
        total = sum(nums) 
        half = total // 2 
        
        for k in range(1, N // 2 + 1):
            left = [sum(comb) for comb in combinations(nums[:N], k)]
            right = [sum(comb) for comb in combinations(nums[N:], N-k)]
            right.sort()
            for x in left:
                r = half - x
                p = bisect.bisect_left(right, r) 
                for pp in [p, p-1]:
                    if 0 <= pp < len(right):
                        left_ans_sum = x + right[pp]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        ans = min(ans, diff) 
        return ans
       
        
        
       
            
            
        