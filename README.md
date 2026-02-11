# BE AIML – Artificial Intelligence Lab Experiments  

This repository contains **Artificial Intelligence Laboratory experiments** for  
**B.E. Artificial Intelligence & Machine Learning (AIML)**.

**Student Name:** Kamesh  
**Subject:** Artificial Intelligence Lab  
**Languages Used:** Java, Python  

---

## 📂 Experiments List  

### Experiment 1  
**Title:** Solving N-Queens Problem  
**Description:** _To be added_  
**File:** `queens.py`  

---

### Experiment 2  
**Title:** A* Algorithm  
**Description:** _To be added_  
**File:** `a*.py`  

---

### Experiment 3  
**Title:** Hill Climbing Algorithm  
**File:** `hillclimb.java`  

**Aim:**  
To implement the Hill Climbing algorithm using Java.  

**Algorithm:**  
1. Start with an initial state  
2. Evaluate neighboring states  
3. Select the best neighbor  
4. Repeat until no improvement is possible  

**Output / Result:**  

![Experiment 3 Output](images/experiment3.png)

---

### Experiment 4  

## (i) Minimax Algorithm  

**Aim:**  
To implement the Minimax algorithm for decision-making in game theory.

**Description:**  
Minimax is a recursive algorithm used in two-player games.  
One player tries to maximize the score while the opponent tries to minimize it.

**Algorithm:**  
1. Define the game tree  
2. Assign utility values to terminal states  
3. Recursively evaluate nodes  
4. Choose the move with the optimal value  

**File:** `exp4/minmax.py`  

**Output / Result:**  

![Minimax Output](exp4/minmax.png)

---

## (ii) Alpha-Beta Pruning  

**Aim:**  
To implement Alpha-Beta Pruning to optimize the Minimax algorithm.

**Description:**  
Alpha-Beta pruning reduces the number of nodes evaluated in the Minimax algorithm by eliminating branches that do not affect the final decision.

**Algorithm:**  
1. Initialize alpha = -∞ and beta = +∞  
2. Apply Minimax logic  
3. Prune branches when beta ≤ alpha  
4. Return the optimal value  

**File:** `exp4/alpha-beta.py`  

**Output / Result:**  

![Alpha-Beta Output](exp4/alpha-beta.png)

---

### Experiment 5  
**Title:** _To be added_  
**Description:** _To be added_  

---

## 📁 Folder Structure  

AI-Lab-Experiments/
│
├── queens.py
├── a*.py
├── hillclimb.java
├── README.md
│
├── images/
│   ├── experiment1.png
│   ├── experiment2.png
│   ├── experiment3.png
│   ├── experiment4.png
│   └── experiment5.png
│
└── exp4/
    ├── minmax.py
    ├── alpha-beta.py
    ├── minmax.png
    └── alpha-beta.png

---

## ✅ Conclusion  

This repository is created for academic purposes to understand and implement various **Artificial Intelligence algorithms** as part of the BE AIML curriculum.
