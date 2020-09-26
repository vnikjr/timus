n, k = map(int,input().split())
ans = n // k
t1 = (n // k) * k
t0 = n - t1
if t0 != 0:
    ans += 1
    t = min(k - t0, t1)
    t1 = n - t
ans+=(t1+k-1)//k
print(ans)