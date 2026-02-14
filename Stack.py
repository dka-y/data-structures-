"""
STACKS - LIFO Data Structure (Simplified)
==========================================
Last-In-First-Out: Like a plate stack - remove from top only
"""

class Stack:
    """Basic Stack Implementation"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove item - O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """View top item - O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return f"Top -> {self.items[::-1]} <- Bottom"


# ==========================================
# KEY APPLICATIONS
# ==========================================

def is_balanced_parentheses(expr):
    """Check if brackets are balanced: (), [], {}"""
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expr:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def reverse_string(text):
    """Reverse string using stack"""
    stack = Stack()
    for char in text:
        stack.push(char)
    
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result


def undo_redo_system(actions):
    """Simulate undo functionality - Text editor example"""
    undo_stack = Stack()
    
    print("Actions performed:")
    for action in actions:
        undo_stack.push(action)
        print(f"  ✓ {action}")
    
    print("\nUndo (LIFO):")
    while not undo_stack.is_empty():
        print(f"  ↶ Undo: {undo_stack.pop()}")


# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":
    print("="*50)
    print("1. BASIC STACK OPERATIONS")
    print("="*50)
    
    stack = Stack()
    for val in [10, 20, 30, 40]:
        stack.push(val)
    
    print(stack.display())
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}\n")
    
    print("="*50)
    print("2. BALANCED PARENTHESES")
    print("="*50)
    
    tests = ["()", "([{}])", "(]", "[[()]]"]
    for expr in tests:
        result = "✓ Balanced" if is_balanced_parentheses(expr) else "✗ Not Balanced"
        print(f"{expr:15} -> {result}")
    
    print("\n" + "="*50)
    print("3. STRING REVERSAL")
    print("="*50)
    
    text = "STACK"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}\n")
    
    print("="*50)
    print("4. UNDO SYSTEM (Text Editor)")
    print("="*50)
    
    undo_redo_system(["Type 'Hello'", "Copy text", "Paste"])
    
    print("\n" + "="*50)
    print("APPLICATIONS:")
    print("="*50)
    print("""
✓ Function Call Stack (Program Execution)
✓ Undo/Redo (Text Editors)
✓ Browser Back Button
✓ Expression Evaluation (Calculators)
✓ Parentheses Matching (Compilers)
✓ Backtracking (Maze, Puzzle solving)
    """)
