class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:

                while stack and  ast < 0 and stack[-1] > 0:
                    if abs( ast ) > abs(stack[-1]):
                        stack.pop()
                    elif abs(stack[-1]) > abs( ast ):
                        break    
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(ast)
        return stack    