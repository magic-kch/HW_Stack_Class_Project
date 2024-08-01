from my_class import Stack


def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.isEmpty() or stack.peek() != bracket_pairs[char]:
                return False
            stack.pop()
    return stack.isEmpty()

if __name__ == '__main__':

    assert is_balanced("[]") == True
    assert is_balanced("(((([{}]))))") == True
    assert is_balanced("[([])((([[[]]])))]{()}") == True
    assert is_balanced("{{[()]}}") == True

    assert is_balanced("}{}") == False
    assert is_balanced("{{[(])]}}") == False
    assert is_balanced("[[{())}]") == False
