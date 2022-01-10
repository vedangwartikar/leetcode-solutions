#User function Template for python3


class Solution:
    def factorial (self, N):
        # code here
        if N == 0:
            return 1
        else:
            return N * self.factorial(N-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends