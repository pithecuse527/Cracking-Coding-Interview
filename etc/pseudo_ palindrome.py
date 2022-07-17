import sys
input = sys.stdin.readline
T = int(input())

def is_palindrome(s):
    return s == s[::-1]

def judge(s):
    if is_palindrome(s):
        return 0
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            if left+1 < right and is_palindrome(s[left+1:right+1]):
                return 1
            if left < right-1 and is_palindrome(s[left:right]):
                return 1
            return 2
        left += 1
        right -= 1

for _ in range(T):
    print(judge(input().rstrip()))
