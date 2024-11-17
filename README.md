# 8-Puzzle

## Problem Statement:
An instance of the 8-puzzle game consists of a board holding 8 distinct movable tiles plus an empty space. The empty space can be swapped with any tile horizontally or vertically adjacent to it. In this assignment, the blank space is represented as `0`.

**Objective**: Given an initial state of the board, find a sequence of moves that transitions this state to the goal state, where tiles are arranged in ascending order:  
`0, 1, 2, 3, 4, 5, 6, 7, 8`.

---

## Design Pattern:
- **Factory Design Pattern**: Used to choose the search technique.

---

## Data Structures Used:
1. **Deque**:
   - Used as a Queue (append, popleft) for BFS due to its full iterability.
   - Used as a Stack (append, pop) for DFS and Iterative DFS.
   - Used to reconstruct the path to the goal (appendleft) efficiently.

2. **Set**:
   - Stores explored states to avoid repetition.

3. **Dictionary**:
   - Stores each state’s parent and total cost for the A* algorithm.

4. **Priority Queue**:
   - Stores states with costs for efficient retrieval in the A* algorithm.

---

## Algorithms:

### **Uninformed Algorithms:**
1. **BFS (Breadth First Search)**:
   - **Purpose**: Explore states level by level to find the goal.
   - **Procedure**:
     1. Add the initial state to the frontier queue.
     2. Pop the first state, add it to the explored set.
     3. Add valid neighboring states to the frontier (if not already explored or in the frontier).
     4. Repeat until the goal is found.
   - **Time Complexity**: O(b^d)  
   - **Space Complexity**: O(b^d)
   <details>
    <summary> <b>Sample Runs:</b> </summary>
     
     ![{26D4D142-716C-4A3D-A307-3458BFE7EBCB}](https://github.com/user-attachments/assets/e0f4409f-5978-4806-9b70-aaee53c83669)
     ![{F9F5B7A3-17B8-499F-B7B8-7A246E2B3DD7}](https://github.com/user-attachments/assets/aceb06c9-791e-4e32-901d-b556a4edd713)
     

   </details>

2. **DFS (Depth First Search)**:
   - **Purpose**: Explore deeply until the end of a branch before backtracking.
   - **Procedure**:
     1. Add the initial state to the frontier stack.
     2. Pop the last state, add it to the explored set.
     3. Add valid neighboring states to the frontier (if not already explored or in the frontier).
     4. Repeat until the goal is found.
   - **Time Complexity**: O(b^m)  
   - **Space Complexity**: O(b * m)
   <details>
    <summary> <b>Sample Runs:</b> </summary>
     
    ![image](https://github.com/user-attachments/assets/d8810192-d4c7-481f-89d1-4d781e65175f)
    ![image](https://github.com/user-attachments/assets/134910b5-6707-4138-a25c-c59e423b4ff3)

   </details>

3. **Iterative DFS**:
   - **Purpose**: Combines DFS with increasing depth limits for memory efficiency.
   - **Procedure**:
     1. Use depth-limited DFS (DLS) for incremental depth limits until the goal is found.
     2. Track state depth to prevent redundant exploration.
   - **Time Complexity**: O(b^d)  
   - **Space Complexity**: O(b * d)  
    <details>
     <summary> <b>Sample Runs:</b> </summary>
     
    ![image](https://github.com/user-attachments/assets/940ad630-4aa5-43b7-874a-384b88bb2586)

   </details>
---

### **Informed Algorithm:**
1. **A***:
   - **Purpose**: Use heuristics to find the optimal path efficiently.
   - **Procedure**:
     1. Use a heuristic function (e.g., Manhattan or Euclidean Distance).
     2. Expand the state with the lowest priority (cost + heuristic).
     3. Check if the state is the goal before expansion.
   - **Time Complexity**: O(b^d)  
   - **Space Complexity**: O(b^d)     
   - **Heuristics**:
     - **Manhattan Distance**: Total moves needed to reach the goal based on grid constraints.
     - **Euclidean Distance**: Straight-line distance to the goal.

   **Conclusion**: Manhattan distance is preferred for its accuracy and efficiency.

   <details>
    <summary> <b>Sample Runs:</b> </summary>
     
     ![image](https://github.com/user-attachments/assets/5b0d33d5-7a80-4450-8bf8-78a4833c6ded)
     ![image](https://github.com/user-attachments/assets/432bece6-5c6d-41e5-a8ba-edf917e80d68)
     ![image](https://github.com/user-attachments/assets/9a643c2a-1bdc-4dad-9c14-a92a4d01a15b)
     ![image](https://github.com/user-attachments/assets/c90ce3b1-f28c-409d-a097-2addf335c782)

   </details>
---

### Notes:

- **Comparison of Manhattan and Euclidean Heuristics**: Both heuristics find the same optimal path; however, Manhattan is faster and requires fewer node expansions, making it more efficient.
- **Comparison of IDS and BFS**: BFS performs faster than IDS because IDS relies on a recursive approach, which is computationally more expensive.
- **Runtime Comparison of Algorithms**: Among all algorithms, A* with the Manhattan heuristic is the fastest, followed by A* with the Euclidean heuristic, BFS, and finally IDS. IDS is the slowest because it employs a brute-force approach, which is inefficient for this problem.

---

## GUI Implementation:
- **Library**: PyQt5.
- **Features**:
  1. Input validation using regex.
  2. Visualize the solution with next/prev buttons.
  3. check if the game is solvable by check number of inversions
     
   <details>
    <summary> <b>Sample Runs:<b> </summary>

   ![image](https://github.com/user-attachments/assets/861acc64-333a-4e5b-8c52-94b02d36f9a9)
   ![image](https://github.com/user-attachments/assets/7db1b788-1f49-443a-94c6-4a3ab1aa5dda)
   ![image](https://github.com/user-attachments/assets/861dd13f-7071-439f-b6f7-f114d284b061)
   ![image](https://github.com/user-attachments/assets/4b4ff89e-19f4-48d2-90c2-e5e781c8346b)  
   
   </details>
