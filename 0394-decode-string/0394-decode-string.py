class Solution(object):
    def decodeString(self, s):
        stack = []
        curStr = ""
        curNum = 0

        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == '[':
                # Push current state and reset for the new bracket level
                stack.append((curStr, curNum))
                curStr = ""
                curNum = 0
            elif c == ']':
                prev_str, num = stack.pop()
                curStr = prev_str + (curStr * num)
            else: 
                curStr += c

        return curStr


                


        