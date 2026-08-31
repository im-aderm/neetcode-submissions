class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        stack = []

        for char in s:
            if char in close_to_open:
                if not stack:
                    return False
                pop = stack.pop()
                if close_to_open[char] != pop:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True