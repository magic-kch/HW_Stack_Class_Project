class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


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
