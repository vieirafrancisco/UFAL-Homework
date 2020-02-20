INF = float('inf')
MAXN = 10
dp = [[INF for _ in range(MAXN)] for _ in range(MAXN)]

def solve(arr, i, j):
    if i == j:
        return 0
    if dp[i][j] != INF:
        return dp[i][j]
    if j == i + 1:
        dp[i][j] = arr[i-1] * arr[i] * arr[j]
        return dp[i][j]
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], solve(arr, i, k) + solve(arr, k+1,j) + arr[i-1]*arr[k]*arr[j])
    return dp[i][j]

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 30]
    print(solve(arr, 1, len(arr)-1))