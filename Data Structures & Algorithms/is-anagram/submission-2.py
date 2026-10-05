class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dup = list(s.lower()) if len(s) == len(t) else None
        t_dup = list(t.lower()) if len(t) == len(s) else None

        if s_dup and t_dup:
            count = {}

            for x in s.lower():
                count[x] = count.get(x, 0) + 1

            for x in t.lower():
                count[x] = count.get(x, 0) - 1

            return all(value == 0 for value in count.values())
        else :
            return False