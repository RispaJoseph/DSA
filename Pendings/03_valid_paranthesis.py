# valid parethesis using stack


def valid_paranthesis(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue

    return not stack


print(valid_paranthesis("()"))