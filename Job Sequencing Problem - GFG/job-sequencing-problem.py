#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x:x.profit, reverse=True)
        deadline_visited=[-1]*101
        count=0
        mx_profit=0
        for i in range(n):
            deadline,profit=Jobs[i].deadline, Jobs[i].profit
            # print(deadline,profit)
            for j in range(deadline,0,-1):
               if deadline_visited[j]==-1:
                   deadline_visited[j]=Jobs[i].id
                   count+=1
                   mx_profit+=profit
                   break
            # print(mx_profit)
                   
        return count,mx_profit
            
                
           
       
    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends