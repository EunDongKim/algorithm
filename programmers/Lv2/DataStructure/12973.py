'''
- 아이디어
스택에 집어넣는다. -1과 -2가 같으면 pop 후 s를 넣는다.
'''
def solution(s):
    stack = []
    stack.append(s[0])
    for i in range(1,len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if stack : return 0
    return 1
