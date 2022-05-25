#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        #find out #non conflicting intervals
        intervals=[]
        for i in range(n):
            intervals.append([start[i],end[i]])
        
        """
        sort intervals by end time.=> we'll be checking if starttime of current
        interval is greater than endLimit.
        if yes => count++
        """
        intervals.sort(key=lambda x:x[1])
        endLimit=intervals[0][1]
        count=1
        for i in range(1,n):
            st,en=intervals[i]
            if st>endLimit:
                endLimit=en
                count+=1
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