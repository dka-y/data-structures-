# Data Structures and Algorithms - Comprehensive Guide

## Overview
This repository contains Python implementations of various data structures based on the classification from the course notes, along with real-world applications and examples.

## Data Structure Classification

### 1. Primitive Data Structures
- Integer, Float, Character, Boolean
- Built-in Python types

### 2. Non-Primitive Data Structures

#### A. Linear Data Structures
Data structures where elements are arranged in linear order.

##### Static Linear Structures
- **Arrays**: Fixed-size collections

##### Dynamic Linear Structures
- **Linked Lists**: Dynamic size, nodes with pointers
- **Stacks**: LIFO (Last-In-First-Out)
- **Queues**: FIFO (First-In-First-Out)

#### B. Non-Linear Data Structures
Elements are not arranged in sequential order.

- **Trees**: Hierarchical structures
- **Graphs**: Networks of vertices and edges

---

## Applications and Real-World Usage

### 1. Arrays
**Where Applied:**
- Database indexing
- Image processing (pixel data)
- Mathematical computations
- Buffer storage

**Why:**
- O(1) random access time
- Cache-friendly (contiguous memory)
- Efficient for known-size data

**Examples:**
- **NumPy/Pandas**: Scientific computing
- **Image Processing Apps**: Photoshop, GIMP (store pixel matrices)
- **Games**: Unity, Unreal Engine (vertex arrays for 3D models)
- **Financial Systems**: Bloomberg Terminal (time-series data)

**Algorithm:** Binary Search (O(log n) on sorted arrays)

---

### 2. Linked Lists
**Where Applied:**
- Memory management (free memory blocks)
- Music/video playlists
- Undo functionality in applications
- Browser history

**Why:**
- Dynamic size
- Efficient insertion/deletion at beginning (O(1))
- No memory wastage

**Examples:**
- **Operating Systems**: Linux kernel (process scheduling)
- **Spotify/YouTube**: Playlist management
- **Text Editors**: VS Code, Sublime (undo/redo stacks)
- **Blockchain**: Bitcoin, Ethereum (block chains)

**Algorithm:** Floyd's Cycle Detection (detect loops in O(n) time)

---

### 3. Stacks
**Where Applied:**
- Function call management (call stack)
- Expression evaluation
- Backtracking algorithms
- Browser back button

**Why:**
- LIFO matches natural undo/function call behavior
- O(1) push/pop operations
- Simple implementation

**Examples:**
- **Compilers**: GCC, Clang (syntax parsing)
- **Web Browsers**: Chrome, Firefox (history navigation)
- **IDEs**: IntelliJ, PyCharm (code folding, matching brackets)
- **Calculator Apps**: Expression evaluation

**Algorithm:** Infix to Postfix conversion, Balanced Parentheses checking

---

### 4. Queues
**Where Applied:**
- Task scheduling
- Print spooling
- Breadth-First Search
- Asynchronous data transfer

**Why:**
- FIFO ensures fair ordering
- O(1) enqueue/dequeue
- Natural for waiting systems

**Examples:**
- **Operating Systems**: CPU scheduling, I/O buffering
- **Message Queues**: RabbitMQ, Apache Kafka (distributed systems)
- **Printers**: Print queue management
- **Customer Service**: Call center systems

**Algorithm:** BFS (Breadth-First Search) for shortest path

---

### 5. Trees
**Where Applied:**
- Database indexing (B-trees)
- File systems
- DOM in web browsers
- Decision making systems

**Why:**
- Hierarchical data representation
- O(log n) search in balanced trees
- Efficient range queries

**Examples:**
- **Databases**: MySQL, PostgreSQL (B-tree indexes)
- **File Systems**: NTFS, ext4 (directory structure)
- **Web Browsers**: Chrome, Firefox (DOM tree)
- **Machine Learning**: scikit-learn (Decision Trees, Random Forests)
- **Compilers**: Abstract Syntax Trees (AST)

**Algorithms:** 
- Binary Search Tree operations (O(log n) average)
- Tree Traversals (Inorder, Preorder, Postorder)
- AVL/Red-Black Tree balancing

---

### 6. Graphs
**Where Applied:**
- Social networks
- Maps and navigation
- Network routing
- Recommendation systems

**Why:**
- Represent complex relationships
- Model real-world networks
- Flexible structure

**Examples:**
- **Social Media**: Facebook, LinkedIn (friend networks)
- **Maps**: Google Maps, Waze (road networks)
- **E-commerce**: Amazon, Netflix (recommendation engines)
- **Networking**: Cisco routers (packet routing)
- **Transportation**: Uber, Lyft (route optimization)

**Algorithms:**
- Dijkstra's Algorithm (shortest path)
- PageRank (web page ranking)
- Minimum Spanning Tree (Kruskal's, Prim's)
- Topological Sort (dependency resolution)

---

## How Data Structures and Algorithms Work Within Systems

### 1. **Operating Systems**
- **Process Scheduling**: Queues (ready queue, waiting queue)
- **Memory Management**: Linked lists (free memory blocks)
- **File System**: Trees (directory hierarchy)
- **Page Replacement**: Stack/Queue (LRU, FIFO algorithms)

### 2. **Databases**
- **Indexing**: B-trees, B+ trees for fast lookups
- **Query Processing**: Hash tables for joins
- **Transaction Logs**: Linked lists
- **Cache**: LRU cache using doubly linked list + hash map

### 3. **Web Browsers**
- **DOM**: Tree structure
- **History**: Stack (back button) and Queue (forward)
- **Cache**: Hash tables with LRU eviction
- **Rendering**: Tree traversal algorithms

### 4. **Compilers**
- **Lexical Analysis**: Arrays/strings
- **Parsing**: Stacks (operator precedence)
- **AST**: Trees
- **Symbol Tables**: Hash tables

### 5. **Networking**
- **Routing Tables**: Graphs with shortest path algorithms
- **Packet Queues**: Priority queues
- **DNS**: Trees (hierarchical domain structure)
- **Load Balancing**: Queues with scheduling algorithms

### 6. **Machine Learning**
- **Feature Storage**: Arrays/matrices
- **Decision Trees**: Tree structures
- **Neural Networks**: Graphs (computational graphs)
- **Training Data**: Arrays with efficient indexing

## Contributors
Jimmy 
Collins 
Wallcott 
Maxwell 
Elton 
Vince
Eddie
Enock
Alvin

## References
- Course Notes from vlms.mku.ac.ke
- "Introduction to Algorithms" by Cormen et al.
- Python Documentation

## License
MIT License# data-structures-
