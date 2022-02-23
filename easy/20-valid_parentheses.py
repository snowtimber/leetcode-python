#2/22/22
#duration: 45 min
#looked at hints
class Solution:
    def isValid(self, s: str) -> bool:

        i = 0
        length = len(s)

        while i < length:
            if '()' in s:
                 s = s.replace('()','')
            if '[]' in s:
                s = s.replace('[]','')
            if '{}' in s:
                s = s.replace('{}','')
            i += 1

        if len(s) != 0:
            return False
        else:
            return True
