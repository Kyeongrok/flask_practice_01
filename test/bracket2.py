from _collections import deque

def isPair(a, b):
    if a == '(' and b == ')':
        return True
    if a == '{' and b == '}':
        return True
    if a == '[' and b == ']':
        return True
    return False

def solution(s):
    st = deque()
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        else:
            if len(st) == 0:
                return False
            # st의 top에 있는 값이 s[i]와 pair면 pop
            if isPair(s[-1], s[i]):
                st.pop()
            else:
                # 아니라면 False
                return False
    return len(st) == 0

print(solution('({})'))
print(solution('({(){}})'))
print(solution('({({}{}})})'))
print(solution('({({){}})'))
print(solution('('))




