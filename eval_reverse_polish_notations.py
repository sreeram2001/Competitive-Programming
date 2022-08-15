class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        char = ['+','-','*','/']
        
        for i in range(len(tokens)):
            if tokens[i] not in char:
                stack.append(int(tokens[i]))
            
            elif tokens[i] in char:
                if len(stack) >= 2:
                    l = len(stack)
                    
                    if tokens[i] == "+":
                        n1 = stack.pop()
                        n2 = stack.pop()
                        ans = n2 + n1
                        stack.append(ans)
                    
                    elif tokens[i] == "-":
                        n1 = stack.pop()
                        n2 = stack.pop()
                        ans = n2 - n1
                        stack.append(ans)
                        
                    elif tokens[i] == "/":
                        n1 = stack.pop()
                        n2 = stack.pop()
                        ans = int(n2/n1)
                        stack.append(ans)
                        
                    elif tokens[i] == "*":
                        n1 = stack.pop()
                        n2 = stack.pop()
                        ans = n2*n1
                        stack.append(ans)
        
        return stack[0]
                        
