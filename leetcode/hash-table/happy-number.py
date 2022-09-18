class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        digits = [int(i) for i in str(n)]
        c = 0
        while c != 1:
            for i in digits:
                c += i ** 2
            if c == 1:
                return True
            elif c in s:
                print(c)
                return False
            else:
                s.add(c)
                digits = [int(i) for i in str(c)]
                c = 0
        return True
