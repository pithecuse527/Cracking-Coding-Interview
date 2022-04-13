import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lans = []
for _ in range(K): lans.append(int(input()))
max_counts = 0
ans = 0
min_len, max_len = 1, max(lans)

def div_lans(small_lan):
    cnt = 0
    for large_lan in lans:
        cnt += large_lan // small_lan
    return cnt

def bin_search(min_len, max_len):
    global max_counts, ans
    if min_len > max_len:
        return
    mid = (min_len + max_len) // 2
    cnt = div_lans(mid)
    if N <= cnt:
        max_counts = cnt
        ans = mid
        bin_search(mid+1, max_len)
    else:
        bin_search(min_len, mid-1)
bin_search(min_len, max_len)
print(ans)