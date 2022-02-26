N = int(input())
nums = set([x for x in range(10)])

def dfs(curr_num):
    for x in range(int(curr_num[-1])):
        new_num = curr_num+str(x)
        nums.add(int(new_num))
        dfs(new_num)

if N > 1023:
    print(-1)
else:
    for i in range(10):
        dfs(str(i))
    sorted_nums_arr = sorted(nums)
    print(sorted_nums_arr[N-1])
