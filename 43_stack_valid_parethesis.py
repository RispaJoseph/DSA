def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue

    return not stack

print(is_valid_parentheses("()"))  # Output: True
print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("(]"))  # Output: False
print(is_valid_parentheses("([)]"))  # Output: False
print(is_valid_parentheses("{[]}"))  # Output: True
