class Solution:
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                number += roman[s[i + 1]] - roman[s[i]]
                i+=2
            else: 
                number += roman[s[i]]
                i+=1
        return number


numbers = [
    "CCXXVI",       # --> 226
    "CCCLXXVII",    # --> 377
    "CDLVI",        # --> 456
    "CCLVIII",      # --> 258
    "DCCLXXXVIII",  # --> 788
    "CCCLXXIII",    # --> 373
    "CCLXIX",       # --> 269
    "CDLXXXIX",     # --> 489
    "CXXVI",        # --> 126
    "DLXI"          # --> 561
];

sol = Solution()

for i in numbers:
    print(f"{i} --> {sol.romanToInt(i)}")