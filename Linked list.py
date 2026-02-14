"""
SIMPLE REAL-WORLD APPLICATION: SHOPPING CART SYSTEM
Using Singly Linked List to manage items dynamically
"""

class Node:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.next = None


class ShoppingCart:
    """
    Shopping Cart using Singly Linked List
    
    Why Linked List for Shopping Cart?
    - Dynamic size: Add/remove items without pre-allocating space
    - Efficient insertion/deletion: O(1) at beginning, O(n) at specific position
    - No shifting required when adding/removing items (unlike arrays)
    - Memory efficient for varying cart sizes
    """
    
    def __init__(self):
        self.head = None
        self.item_count = 0
    
    def add_item(self, item_name, price, quantity=1):
        """Add item to cart"""
        new_node = Node(item_name, price, quantity)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.item_count += 1
        print(f"✓ Added {quantity}x {item_name} @ ${price}")
    
    def remove_item(self, item_name):
        """Remove item from cart"""
        if not self.head:
            print("Cart is empty!")
            return False
        
        if self.head.item_name == item_name:
            self.head = self.head.next
            self.item_count -= 1
            print(f"✓ Removed {item_name}")
            return True
        
        current = self.head
        while current.next and current.next.item_name != item_name:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.item_count -= 1
            print(f"✓ Removed {item_name}")
            return True
        
        print(f"✗ Item '{item_name}' not found")
        return False
    
    def update_quantity(self, item_name, new_quantity):
        """Update quantity of existing item"""
        current = self.head
        
        while current:
            if current.item_name == item_name:
                current.quantity = new_quantity
                print(f"✓ Updated {item_name} quantity to {new_quantity}")
                return True
            current = current.next
        
        print(f"✗ Item not found")
        return False
    
    def calculate_total(self):
        """Calculate total price"""
        total = 0
        current = self.head
        while current:
            total += current.price * current.quantity
            current = current.next
        return total
    
    def display_cart(self):
        """Display all items in cart"""
        if not self.head:
            print("\n🛒 Your cart is empty!\n")
            return
        
        print("\n" + "="*60)
        print("🛒 SHOPPING CART")
        print("="*60)
        
        current = self.head
        position = 1
        
        while current:
            item_total = current.price * current.quantity
            print(f"{position}. {current.item_name:20} | "
                  f"${current.price:6.2f} x {current.quantity:2} = "
                  f"${item_total:7.2f}")
            current = current.next
            position += 1
        
        print("-"*60)
        total = self.calculate_total()
        print(f"{'TOTAL':42} ${total:7.2f}")
        print("="*60 + "\n")


# ============================================
# DEMONSTRATION
# ============================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🛍️  SHOPPING CART SYSTEM - Using Linked Lists")
    print("="*60)
    
    cart = ShoppingCart()
    
    # Add items
    print("\n--- Adding Items ---")
    cart.add_item("Laptop", 999.99, 1)
    cart.add_item("Mouse", 29.99, 2)
    cart.add_item("Keyboard", 79.99, 1)
    cart.add_item("Monitor", 299.99, 1)
    
    cart.display_cart()
    
    # Modify
    print("--- Updating Quantity ---")
    cart.update_quantity("Mouse", 1)
    
    cart.display_cart()
    
    # Remove
    print("--- Removing Item ---")
    cart.remove_item("Keyboard")
    
    cart.display_cart()
    
    # Show benefits
    print("="*60)
    print("WHY LINKED LISTS FOR SHOPPING CART?")
    print("="*60)
    print("""
✓ Dynamic Size: Cart grows without pre-allocating memory
✓ Efficient Operations: Add/Remove items in O(1) at head
✓ No Array Shifting: Unlike arrays, no need to shift elements
✓ Memory Efficient: Only allocate space for actual items
✓ Real-World Fit: Matches real shopping behavior perfectly
    """)
