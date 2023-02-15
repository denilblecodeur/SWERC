class RangeMinQuery: 
    def __init__(self, a):
        self.arr = a[:]
        self.n = len(a)
        self.t = [0] * 2 * self.n
        for i in range(self.n):
            self.t[self.n + i] = i
        for i in range(self.n - 1, 0, -1):
            self.t[i] = min(self.t[i << 1], self.t[(i << 1) | 1], key=lambda x:self.arr[x])
    
    def update(self, pos, val):
        i = pos + self.n
        self.arr[self.t[i]] = val
        while i > 1:
            self.t[i >> 1] = min(self.t[i], self.t[i ^ 1], key=lambda x:self.arr[x])
            i >>= 1
    
    def qmin(self, l, r):
        ans = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if (l & 1):
                ans = min(ans, self.t[l], key=lambda x:self.arr[x])
                l += 1
            if (r & 1):
                r -= 1
                ans = min(ans, self.t[r], key=lambda x:self.arr[x])
            l >>= 1
            r >>= 1
        return ans