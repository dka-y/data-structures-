"""
QUEUES - FIFO Data Structure (Simplified)
==========================================
First-In-First-Out: Like a waiting line - first served first
"""

from collections import deque

class Queue:
    """Efficient Queue using deque"""
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to rear - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """View front item - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return f"Front <- {list(self.items)} <- Rear"


# ==========================================
# KEY APPLICATIONS
# ==========================================

def bfs_graph_traversal():
    """Breadth-First Search using Queue"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }
    
    queue = Queue()
    visited = set()
    result = []
    
    queue.enqueue('A')
    visited.add('A')
    
    while not queue.is_empty():
        vertex = queue.dequeue()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    
    return result


def print_job_scheduler(jobs):
    """Simulate print queue (FIFO)"""
    queue = Queue()
    
    for job in jobs:
        queue.enqueue(job)
    
    results = []
    while not queue.is_empty():
        results.append(queue.dequeue())
    
    return results


def cpu_scheduling(processes, time_slices=2):
    """Round-robin CPU scheduling"""
    queue = Queue()
    
    for process in processes:
        queue.enqueue(process)
    
    executed = []
    
    while not queue.is_empty():
        process = queue.dequeue()
        executed.append(process)
        queue.enqueue(process)  # Re-add after execution
        
        if len(executed) >= len(processes) * time_slices:
            break
    
    return executed


# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":
    print("="*50)
    print("1. BASIC QUEUE OPERATIONS")
    print("="*50)
    
    queue = Queue()
    for val in [10, 20, 30, 40]:
        queue.enqueue(val)
    
    print(queue.display())
    print(f"Front: {queue.front()}")
    print(f"Dequeued: {queue.dequeue()}\n")
    
    print("="*50)
    print("2. BFS - GRAPH TRAVERSAL")
    print("="*50)
    
    bfs_result = bfs_graph_traversal()
    print(f"BFS Order: {' -> '.join(bfs_result)}")
    print("(Shortest path, level-order traversal)\n")
    
    print("="*50)
    print("3. PRINT JOB QUEUE")
    print("="*50)
    
    jobs = ["Doc1.pdf", "Image.jpg", "Report.docx"]
    print(f"Jobs: {jobs}")
    printed = print_job_scheduler(jobs)
    print(f"Printed (FIFO): {' -> '.join(printed)}\n")
    
    print("="*50)
    print("4. CPU SCHEDULING (Round-Robin)")
    print("="*50)
    
    processes = ["P1", "P2", "P3"]
    executed = cpu_scheduling(processes, time_slices=2)
    print(f"Execution order: {' -> '.join(executed)}\n")
    
    print("="*50)
    print("5. CUSTOMER SERVICE QUEUE")
    print("="*50)
    
    service_queue = Queue()
    customers = ["Alice", "Bob", "Charlie"]
    
    print("Customers joining:")
    for cust in customers:
        service_queue.enqueue(cust)
        print(f"  {cust} joined")
    
    print(f"\nQueue: {service_queue.display()}")
    
    print("\nServing (FIFO):")
    while not service_queue.is_empty():
        print(f"  Serving: {service_queue.dequeue()}")
    
    print("\n" + "="*50)
    print("APPLICATIONS:")
    print("="*50)
    print("""
✓ CPU Scheduling (Round-Robin)
✓ Print Job Queue
✓ Customer Service Lines
✓ Breadth-First Search (BFS)
✓ Network Packet Handling
✓ Streaming Data Processing
    """)
