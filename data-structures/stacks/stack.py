ex_strs = [
    "(())",
    "([[]])",
    "(]",
    "(((())))[",
    "()"
    ]

def check_balanced(s):
    stack = []
    for char in s:
        if char in ['(', '[']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (top == '[' and char != ']') or (top == '(' and char != ')'):
                return False
    return not bool(len(stack))

for s in ex_strs:
    print(check_balanced(s))