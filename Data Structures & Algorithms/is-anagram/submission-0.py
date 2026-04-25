class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        res_mas = [0] * 26
        const = ord('a')
        for i in range(n):
            res_mas[ord(s[i])-const] += 1
            res_mas[ord(t[i])-const] -= 1
        for i in res_mas:
            if i != 0:
                return False
        return True