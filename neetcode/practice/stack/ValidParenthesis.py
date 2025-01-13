"""
Valid Explanation
neetcode question link: https://neetcode.io/problems/validate-parentheses
"""
def isValidParenthesis(string: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "}" : "{", "]" : "["}
    for char in string:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False

string = "{([])}"
print(isValidParenthesis(string))