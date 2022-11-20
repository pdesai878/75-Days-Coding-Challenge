class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popular_creator=defaultdict(int)
        popular_id={}
        mx=0
        for creator,id_,view in zip(creators,ids,views):
            popular_creator[creator]+=view
            mx=max(mx,popular_creator[creator])
            
            if creator not in popular_id or popular_id[creator][1]<view or (popular_id[creator][1]==view and popular_id[creator][0]>id_):
                popular_id[creator]=[id_,view]
        res=[]     
        for creator,totalViews in popular_creator.items():
            if totalViews==mx:
                res.append([creator,popular_id[creator][0]])
        return res
                    
                    
            
            
            
            

        
        