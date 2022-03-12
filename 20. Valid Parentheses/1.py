def isValid(self, s: str) -> bool:
        
    
    stack = []
    
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
            
        elif len(stack) != 0:
            if ch == ")" or ch == "]" or ch == "}" :
                curr = stack.pop()

                if ch == ")" and curr == "(":
                    continue
                elif ch == "]" and curr == "[":
                    continue
                elif ch == "}" and curr == "{":
                    continue
                else:
                    return False
        else:
            return False
            
    return True if len(stack) == 0 else False
                



# def isValid(s: str) -> bool:
#     while len(s) > 0:
#         l = len(s)
#         s = s.replace('()','')
#         s = s.replace('{}','')
#         s = s.replace('[]','')
#         if l==len(s): return False
#     return True


# isValid("([{}])")