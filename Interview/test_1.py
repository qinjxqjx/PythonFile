import math

n = raw_input()
n = (n).split(' ')
m = int(n[1])
n = int(n[0])

dp = [m+1]*(m+1)
dp[n] = 0
for i in xrange(n, m):
    if dp[i] < m:
        for j in xrange(i/2, 1, -1):
            if i + j <= m and i % j == 0:
                dp[i+j] = min(dp[i+j], dp[i]+1)


if dp[m] > m:
    print -1
else:
    print dp[m]
