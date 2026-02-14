"""
TREES - Hierarchical Non-Linear Data Structure (Simplified)
===========================================================
Nodes connected in parent-child relationship (root to leaves)
"""

from collections import deque

class TreeNode:
    """Node for Binary Tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Binary Tree: Each node has at most 2 children"""
    
    def __init__(self):
        self.root = None
    
    def insert_level_order(self, data):
        """Insert nodes level by level"""
        new_node = TreeNode(data)
        
        if not self.root:
            self.root = new_node
            return
        
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            
            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)
    
    def inorder(self, node, result=None):
        """Left -> Root -> Right"""
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        return result
    
    def level_order(self):
        """Breadth-first traversal"""
        if not self.root:
            return []
        
        queue = deque([self.root])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node):
        """Get tree height"""
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


class BinarySearchTree:
    """BST: Left < Parent < Right"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert node maintaining BST property"""
        self.root = self._insert_rec(self.root, data)
    
    def _insert_rec(self, node, data):
        if not node:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_rec(node.left, data)
        elif data > node.data:
            node.right = self._insert_rec(node.right, data)
        
        return node
    
    def search(self, data):
        """Search for value - O(log n) average"""
        return self._search_rec(self.root, data)
    
    def _search_rec(self, node, data):
        if not node or node.data == data:
            return node is not None
        
        if data < node.data:
            return self._search_rec(node.left, data)
        return self._search_rec(node.right, data)
    
    def inorder(self):
        """Inorder gives sorted output"""
        result = []
        self._inorder_rec(self.root, result)
        return result
    
    def _inorder_rec(self, node, result):
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.data)
            self._inorder_rec(node.right, result)


# ==========================================
# APPLICATIONS
# ==========================================

def file_system_demo():
    """File system hierarchy"""
    class FileNode:
        def __init__(self, name, is_file=False):
            self.name = name
            self.is_file = is_file
            self.children = []
        
        def add_child(self, child):
            self.children.append(child)
        
        def display(self, level=0):
            indent = "  " * level
            symbol = "📄" if self.is_file else "📁"
            print(f"{indent}{symbol} {self.name}")
            for child in self.children:
                child.display(level + 1)
    
    root = FileNode("C:")
    documents = FileNode("Documents")
    root.add_child(documents)
    
    documents.add_child(FileNode("report.pdf", is_file=True))
    documents.add_child(FileNode("notes.txt", is_file=True))
    
    return root


def expression_tree_demo():
    """Evaluate (3 + 5) * 2"""
    root = TreeNode('*')
    root.left = TreeNode('+')
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    
    def evaluate(node):
        if not node.left and not node.right:
            return node.data
        
        left = evaluate(node.left)
        right = evaluate(node.right)
        
        if node.data == '+':
            return left + right
        elif node.data == '*':
            return left * right
    
    return evaluate(root)


# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":
    print("="*50)
    print("1. BINARY TREE OPERATIONS")
    print("="*50)
    
    bt = BinaryTree()
    
    print("\nInserting: 1, 2, 3, 4, 5, 6, 7")
    for val in [1, 2, 3, 4, 5, 6, 7]:
        bt.insert_level_order(val)
    
    print(f"Inorder:      {bt.inorder(bt.root)}")
    print(f"Level-order:  {bt.level_order()}")
    print(f"Height:       {bt.height(bt.root)}\n")
    
    print("="*50)
    print("2. BINARY SEARCH TREE")
    print("="*50)
    
    bst = BinarySearchTree()
    
    print("\nInserting: 50, 30, 70, 20, 40, 60, 80")
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    print(f"Inorder (sorted): {bst.inorder()}")
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 25: {bst.search(25)}\n")
    
    print("="*50)
    print("3. FILE SYSTEM HIERARCHY")
    print("="*50)
    print()
    
    root = file_system_demo()
    root.display()
    
    print("\n" + "="*50)
    print("4. EXPRESSION TREE")
    print("="*50)
    
    result = expression_tree_demo()
    print(f"\nExpression: (3 + 5) * 2 = {result}\n")
    
    print("="*50)
    print("APPLICATIONS:")
    print("="*50)
    print("""
✓ Binary Search Trees (Searching/Indexing)
✓ File System Directories
✓ Expression Evaluation (Compilers)
✓ Decision Trees (ML/AI)
✓ DOM (Document Object Model)
✓ Game AI (Minimax Trees)
    """)
