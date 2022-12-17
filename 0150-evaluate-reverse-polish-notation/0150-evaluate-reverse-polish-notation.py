class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv, 
            '%' : operator.mod,
            '^' : operator.xor,
        }
        res=0
        stack=[]
        for ch in tokens:
            if ch not in op:
                stack.append(int(ch))
            else:
                n2=stack.pop()
                n1=stack.pop()
                temp=op[ch](n1,n2)
                stack.append(int(temp))
        return stack[0]
        