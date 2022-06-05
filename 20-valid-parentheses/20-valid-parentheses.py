class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in ["(","{","["]:
                stack.append(ch)
            else:
                if ch==")":
                    if stack and stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                elif ch=="}": 
                    if stack and stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
                elif ch=="]":
                    if stack and stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True