class StaticArray:
    """
    Array implementation with fixed size
    Time Complexity:
        - Access: O(1)
        - Search: O(n)
        - Insertion: O(n) (need to shift elements)
        - Deletion: O(n) (need to shift elements)
    """
    
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.length = 0
    
    def insert(self, index, value):
        """Insert value at specific index"""
        if index < 0 or index > self.length or self.length >= self.size:
            raise IndexError("Index out of bounds or array is full")
        
        # Shift elements to the right
        for i in range(self.length, index, -1):
    ]        self.array[i] = self.array[i-1]
        
        self.array[index] = value
        self.length += 1
    
    def delete(self, index):
        """Delete element at specific index"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        
        value = self.array[index]
        
        # Shift elements to the left
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.length - 1] = None
        self.length -= 1
        return value
    
    def search(self, value):
        """Linear search for a value"""
        for i in range(self.length):
            if self.array[i] == value:
                return i
        return -1
    
    def get(self, index):
        """Get element at index - O(1)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def update(self, index, value):
        """Update element at index - O(1)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        self.array[index] = value
    
    def display(self):
        """Display the array"""
        return [self.array[i] for i in range(self.length)]


class DynamicArray:
    """
    Dynamic array that grows automatically (similar to Python list)
    """
    
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.array = [None] * self.capacity
    
    def _resize(self):
        """Double the capacity when full"""
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
    
    def append(self, value):
        """Add element at the end - Amortized O(1)"""
        if self.length == self.capacity:
            self._resize()
        self.array[self.length] = value
        self.length += 1
    
    def get(self, index):
        """Get element at index"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def display(self):
        return [self.array[i] for i in range(self.length)]


class MultiDimensionalArray:
    """
    2D Array (Matrix) implementation
    Used in image processing, game boards, etc.
    """
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def set(self, row, col, value):
        """Set value at position (row, col)"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
        else:
            raise IndexError("Position out of bounds")
    
    def get(self, row, col):
        """Get value at position (row, col)"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            raise IndexError("Position out of bounds")
    
    def display(self):
        """Display the matrix"""
        for row in self.matrix:
            print(row)


# Demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("STATIC ARRAY DEMONSTRATION")
    print("=" * 60)
    
    # Create array of size 10
    arr = StaticArray(10)
    
    # Insert elements
    print("\nInserting elements: 10, 20, 30, 40, 50")
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    arr.insert(3, 40)
    arr.insert(4, 50)
    print(f"Array: {arr.display()}")
    
    # Insert in middle
    print("\nInserting 25 at index 2")
    arr.insert(2, 25)
    print(f"Array: {arr.display()}")
    
    # Access element
    print(f"\nElement at index 3: {arr.get(3)}")
    
    # Search for element
    print(f"Index of value 40: {arr.search(40)}")
    
    # Delete element
    print("\nDeleting element at index 2")
    deleted = arr.delete(2)
    print(f"Deleted value: {deleted}")
    print(f"Array: {arr.display()}")
    
    print("\n" + "=" * 60)
    print("DYNAMIC ARRAY DEMONSTRATION")
    print("=" * 60)
    
    dyn_arr = DynamicArray()
    print("\nAppending elements: 5, 10, 15, 20, 25")
    for val in [5, 10, 15, 20, 25]:
        dyn_arr.append(val)
    print(f"Dynamic Array: {dyn_arr.display()}")
    print(f"Capacity: {dyn_arr.capacity}, Length: {dyn_arr.length}")
    
    print("\n" + "=" * 60)
    print("2D ARRAY (MATRIX) DEMONSTRATION")
    print("=" * 60)
    
    matrix = MultiDimensionalArray(3, 3)
    print("\nCreating a 3x3 identity matrix:")
    for i in range(3):
        matrix.set(i, i, 1)
    matrix.display()
    
    print("\n" + "=" * 60)
    print("REAL-WORLD APPLICATION EXAMPLES")
    print("=" * 60)
    
    # Example 1: Student grades (1D array)
    print("\n1. Student Grades System:")
    grades = StaticArray(5)
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    student_grades = [85, 92, 78, 95, 88]
    
    for i, grade in enumerate(student_grades):
        grades.insert(i, grade)
    
    print(f"Students: {students}")
    print(f"Grades: {grades.display()}")
    total = sum(grades.display())
    average = total / grades.length
    print(f"Class Average: {average:.2f}")
    
    # Example 2: Image representation (2D array)
    print("\n2. Simple 5x5 Grayscale Image (0=black, 255=white):")
    image = MultiDimensionalArray(5, 5)
    # Create a simple pattern
    pattern = [
        [0, 0, 255, 0, 0],
        [0, 255, 0, 255, 0],
        [255, 0, 0, 0, 255],
        [0, 255, 0, 255, 0],
        [0, 0, 255, 0, 0]
    ]
    for i in range(5):
        for j in range(5):
            image.set(i, j, pattern[i][j])
    image.display()
    
    print("\n" + "=" * 60)
