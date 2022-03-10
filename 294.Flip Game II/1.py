    def can_win(self, s: str) -> bool:
        if len(s) < 2:
            return False

        for i in range(1,len(s)):
            if s[i-1] == "+" and s[i] == "+":
                temp = list(s)
                temp[i-1] = "-"
                temp[i] = "-"
                temp = ''.join(temp)
                if not self.can_win(temp):
                    return True
                    
        return False