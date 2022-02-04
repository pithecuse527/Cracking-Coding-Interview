class Solution:
    candidates = None
    def backtracking(self, l_size, r_size, n, q):

        # condition of backtracking
        if l_size < r_size or l_size > n:
            return None
        
        # condition of the result returning
        if l_size == r_size == n:
            return q
        
        # going left
        tmp1 = q.copy()
        tmp1.append('(')
        left_res = self.backtracking(l_size+1, r_size, n, tmp1)
        if left_res:
            self.candidates.append(left_res)
        
        # going right
        tmp2 = q.copy()
        tmp2.append(')')
        right_res = self.backtracking(l_size, r_size+1, n, tmp2)
        if right_res:
            self.candidates.append(right_res)
        
        # still need to be investigated with state space tree
        return None
    
    def generateParenthesis(self, n):
        self.candidates = []
        q = list()
        self.backtracking(0, 0, n, q)
        
        # generate the result
        result = list()
        for c in self.candidates:
            result.append("".join(c))
        return result
