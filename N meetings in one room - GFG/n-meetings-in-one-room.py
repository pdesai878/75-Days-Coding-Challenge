#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        intervals=[]
        for i in range(n):
            intervals.append([start[i],end[i],i+1])
        intervals.sort(key=lambda x:(x[1],x[2]))
        
        endLimit=intervals[0][1]
        
        res=[]
        count=1
        for i in range(1,n):
            curr_start,curr_end,meet_no=intervals[i]
            if curr_start<=endLimit:
                pass
            else:
                count+=1
                res.append(meet_no)
                endLimit=curr_end   
        return count
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends