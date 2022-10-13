class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv, 
            '%' : operator.mod,
            '^' : operator.xor,
        }
        
        stack=[]
        res=0
        for el in tokens:
            if el not in ops:
                stack.append(int(el))
            else:
                a,b=stack.pop(),stack.pop()
                stack.append(int(ops[el](b,a)))
        return stack.pop()