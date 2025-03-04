"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        valid = {")": "(", "}": "{", "]": "["}

        for x in s:
            if x in valid: 
                # check if st is not empty, and check if the top of the stack is 
                # a match. if it is, pop (valid pair)
                if st and st[-1] == valid[x]:
                    st.pop()
                else:
                    # break if not a valid pair
                    return False
            else:  
                # push the opener
                st.append(x)

        return not st  # Stack should be empty if valid
