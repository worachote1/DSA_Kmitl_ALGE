class Solution(object):
    def fib(self, n):
        if (n == 0 or n == 1):
            return n
        return self.fib(n-1) + self.fib(n-2)

test = Solution()
print(test.fib(2))
print(test.fib(3))
print(test.fib(4))