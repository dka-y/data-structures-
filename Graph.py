"""
GRAPHS - Non-Linear Data Structure (Simplified)
===============================================
Vertices (nodes) connected by edges
"""

from collections import deque
import heapq

class Graph:
    """Undirected Graph using Adjacency List"""
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, v1, v2):
        """Add undirected edge"""
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def add_directed_edge(self, v1, v2):
        """Add directed edge"""
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append(v2)
    
    def bfs(self, start):
        """Breadth-First Search - O(V + E)"""
        visited = set()
        queue = deque([start])
        result = []
        
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start, visited=None):
        """Depth-First Search - O(V + E)"""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def has_path(self, start, end):
        """Check if path exists"""
        visited = set()
        return self._has_path_helper(start, end, visited)
    
    def _has_path_helper(self, current, end, visited):
        if current == end:
            return True
        visited.add(current)
        
        for neighbor in self.graph[current]:
            if neighbor not in visited:
                if self._has_path_helper(neighbor, end, visited):
                    return True
        return False
    
    def display(self):
        """Display adjacency list"""
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


class WeightedGraph(Graph):
    """Weighted Graph for Dijkstra's algorithm"""
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, v1, v2, weight):
        """Add weighted undirected edge"""
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        
        self.graph[v1].append((v2, weight))
        self.graph[v2].append((v1, weight))
    
    def dijkstra(self, start):
        """Dijkstra's shortest path - O((V + E) log V)"""
        distances = {v: float('inf') for v in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            curr_dist, curr = heapq.heappop(pq)
            
            if curr_dist > distances[curr]:
                continue
            
            for neighbor, weight in self.graph[curr]:
                distance = curr_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances


# ==========================================
# APPLICATIONS
# ==========================================

def social_network_suggestions():
    """Friend suggestions in social network"""
    social = Graph()
    
    edges = [("John", "Alice"), ("John", "Bob"), ("Alice", "Charlie"),
             ("Bob", "David"), ("Charlie", "Eve")]
    
    for p1, p2 in edges:
        social.add_edge(p1, p2)
    
    john_friends = set(social.graph["John"])
    suggestions = set()
    
    for friend in john_friends:
        for friend_of_friend in social.graph[friend]:
            if friend_of_friend != "John" and friend_of_friend not in john_friends:
                suggestions.add(friend_of_friend)
    
    return john_friends, suggestions


def web_crawler():
    """Web page crawling using BFS"""
    web = Graph()
    
    pages = [("PageA", "PageB"), ("PageA", "PageC"), 
             ("PageB", "PageC"), ("PageB", "PageD")]
    
    for p1, p2 in pages:
        web.add_directed_edge(p1, p2)
    
    return web.bfs("PageA")


# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":
    print("="*50)
    print("1. BASIC GRAPH OPERATIONS")
    print("="*50)
    
    g = Graph()
    
    print("\nFriendship network:")
    edges = [("Alice", "Bob"), ("Alice", "Charlie"), 
             ("Bob", "David"), ("Charlie", "David")]
    
    for p1, p2 in edges:
        g.add_edge(p1, p2)
        print(f"  {p1} <-> {p2}")
    
    print("\nAdjacency List:")
    g.display()
    
    print(f"\nBFS from Alice: {g.bfs('Alice')}")
    print(f"DFS from Alice: {g.dfs('Alice')}")
    print(f"Path Alice->David: {g.has_path('Alice', 'David')}\n")
    
    print("="*50)
    print("2. WEIGHTED GRAPH (DIJKSTRA)")
    print("="*50)
    
    wg = WeightedGraph()
    
    print("\nCity routes (distances in km):")
    routes = [("A", "B", 4), ("A", "C", 2), ("B", "D", 5),
              ("C", "D", 8), ("D", "E", 2)]
    
    for c1, c2, dist in routes:
        wg.add_edge(c1, c2, dist)
        print(f"  {c1} <-> {c2}: {dist} km")
    
    print("\nShortest paths from A:")
    distances = wg.dijkstra("A")
    for city in sorted(distances.keys()):
        print(f"  To {city}: {distances[city]} km")
    
    print("\n" + "="*50)
    print("3. SOCIAL NETWORK")
    print("="*50)
    
    friends, suggestions = social_network_suggestions()
    print(f"\nJohn's friends: {friends}")
    print(f"Friend suggestions: {suggestions}\n")
    
    print("="*50)
    print("4. WEB CRAWLER")
    print("="*50)
    
    crawl = web_crawler()
    print(f"\nPages crawled from PageA: {' -> '.join(crawl)}\n")
    
    print("="*50)
    print("APPLICATIONS:")
    print("="*50)
    print("""
✓ Social Networks (Friendships)
✓ GPS Navigation (Shortest Path)
✓ Web Crawler (BFS/DFS)
✓ Network Routing
✓ Recommendation Systems
✓ Game AI (Pathfinding)
    """)
