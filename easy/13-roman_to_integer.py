class Solution:
    def romanToInt(self, s: str) -> int:

        inventory = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000}

        sum = 0
        for i in range(0,len(s)-1):
            if inventory[s[i]] < inventory[s[i+1]]:
                sum -= inventory[s[i]]
            else:
                sum += inventory[s[i]]
        return sum + inventory[s[-1]]
