

#given 3 numbers, we need to tell the total number of ways we can form a number 
#N using the sum of the given 3 numbers 


""" 
first write some code to calculate the factorial of a number using bottom up approach. 
Once, again as our general procedure to solve a DP we first define a state.
In this case, we define a state as dp[x], where dp[x] is to find the factorial of x.
""" 


def dp(n): 

    if n<1: 
        return 0 
    
    if n==1: 
        return 1 
    
    if dp[n]!=-1: #memoization
        return dp[n]

    return dp[n]=dp[n-1]+dp[n-3]+dp[n-5]


#tabulated version to find factorial x 

def dp(n): 

    dp[0]=1

    for i in range(i,n): 

        dp[i]=dp[i-1]*i 

#memoization version, top down 

def dp(n): 

    if n<1: 
        return 0 
    
    if n==1: 
        return 1 
    
    if dp[n]!=-1: #memoization
        return dp[n]

    return dp[n]=x*dp(n-1)


# Python3 implementation of the approach 
  
# Function to return the minimum number 
# of given operations required 
# to sort the array 
def getMinimumOps(ar): 
      
    # Number of elements in the array 
    n = len(ar) 
  
    # Smallest element in the array 
    small = min(ar) 
  
    # Largest element in the array 
    large = max(ar) 
  
    """ 
        dp(i, j) represents the minimum number 
        of operations needed to make the 
        array[0 .. i] sorted in non-decreasing 
        order given that ith element is j 
    """
    dp = [[ 0 for i in range(large + 1)]  
              for i in range(n)] 
  
    # Fill the dp[]][ array for base cases 
    for j in range(small, large + 1): 
        dp[0][j] = abs(ar[0] - j) 
    """ 
    /* 
        Using results for the first (i - 1) 
        elements, calculate the result 
        for the ith element 
    */ 
    """
    for i in range(1, n): 
        minimum = 10**9
        for j in range(small, large + 1): 
              
        # """ 
        #     /* 
        #     If the ith element is j then we can have 
        #     any value from small to j for the i-1 th 
        #     element 
        #     We choose the one that requires the 
        #     minimum operations 
        # """ 
            minimum = min(minimum, dp[i - 1][j]) 
            dp[i][j] = minimum + abs(ar[i] - j) 
    """ 
    /* 
        If we made the (n - 1)th element equal to j 
        we required dp(n-1, j) operations 
        We choose the minimum among all possible 
        dp(n-1, j) where j goes from small to large 
    */ 
    """
    ans = 10**9
    for j in range(small, large + 1): 
        ans = min(ans, dp[n - 1][j]) 
  
    return ans 
  
# Driver code 
ar = [1, 2, 1, 4, 3] 
  
print(getMinimumOps(ar)) 
  
# This code is contributed by Mohit Kumar 