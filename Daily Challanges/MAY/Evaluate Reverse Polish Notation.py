tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens2 = ["4", "13", "5", "/", "+"]
tokens3 = ["2", "1", "+", "3", "*"]


def evalRPN(tokens):
    stack = []

    def conditions(a, b, c):
        if c == '+': return a + b
        if c == '-': return b - a
        if c == '*': return a * b
        if c == '/': return int(b / a)

    for t in tokens:
        if t in '*/+-':
            stack.append(conditions(stack.pop(), stack.pop(), t))
        else:
            stack.append(int(t))
    return stack[-1] 


print(evalRPN(tokens3))
print(evalRPN(tokens2))
print(evalRPN(tokens))

def evalRPN2(tokens):
    stack = []
    for t in tokens:
        if t not in {"+", "-", "*", "/"}:
            stack.append(int(t))
        else:
            b, a = stack.pop(), stack.pop()
            if t == "+": stack.append(a + b)
            elif t == "-": stack.append(a - b)
            elif t == "*": stack.append(a * b)
            else: stack.append(int(a / b))
    return stack[0]


print(evalRPN2(tokens3))
print(evalRPN2(tokens2))
print(evalRPN2(tokens))
