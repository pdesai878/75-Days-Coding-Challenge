class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans=0
        dicti=defaultdict(int)
        count=0
        for no in rolls:
            dicti[no]+=1
            if dicti[no]==1:
                count+=1
            if count==k:
                ans+=1
                count=0
                dicti.clear()
        return ans+1
        