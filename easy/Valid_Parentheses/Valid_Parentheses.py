class Solution(object):
    def isValid(self, s):
        st = []
        closingBrackets = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }

        for i in s:
            if i in closingBrackets.values():
                st.append(i)
            elif not st or st.pop() != closingBrackets[i]:
                return False

        return not st

sol = Solution()

tests = [
    "()",
    "()[]{}",
    "(]"
];

for i in tests:
    print(f"{i} --> {sol.isValid(i)}")