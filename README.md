# Capstone-Project-Courier-Optimization-System-DAA

# 🚚 Smart Courier Optimization System

A Python-based courier planning system that helps select parcels, pack them within vehicle capacity, and find an efficient delivery route.

This project uses different algorithms from **Design and Analysis of Algorithms (DAA)** to solve real-world delivery problems.

## 📌 Project Overview

The system performs two main tasks:

1. **Parcel Packing:** Selects the best combination of parcels without exceeding the vehicle's weight and volume limits.
2. **Route Optimization:** Finds an efficient order for delivering parcels to different locations while minimizing travel distance.

It combines sorting, Dynamic Programming, Graph Algorithms, and Approximation Algorithms.

## 🎯 Objectives

- Sort parcels according to their delivery priority.
- Select parcels based on vehicle capacity.
- Maximize the total value of selected parcels.
- Find shortest distances between delivery locations.
- Generate an efficient delivery route.
- Reduce unnecessary travel distance.
- Generate a final delivery report.

## 📂 Project Structure

```text
smart_courier/
│
├── main.py
│
├── data/
│   ├── __init__.py
│   └── sample_data.py
│
├── algorithms/
│   ├── __init__.py
│   ├── sorting.py
│   ├── packing.py
│   ├── graph.py
│   └── routing.py
│
├── services/
│   ├── __init__.py
│   └── courier_service.py
│
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `main.py` | Starts the application |
| `sample_data.py` | Contains parcel and location details |
| `sorting.py` | Sorts parcels by priority |
| `packing.py` | Selects parcels using Dynamic Programming |
| `graph.py` | Creates the delivery graph and finds shortest paths |
| `routing.py` | Generates and improves delivery routes |
| `courier_service.py` | Connects all the algorithms |

## ⚙️ Algorithms Used

### 1. Sorting Algorithm

Sorts parcels based on:
- Highest delivery priority.
- Highest parcel value.
- Lowest parcel weight.

### 2. Dynamic Programming (0/1 Knapsack)

Selects parcels that provide the maximum total value while staying within the vehicle's weight and volume limits.

Each parcel is either selected completely or not selected.

### 3. Graph Construction

Represents delivery locations as points (vertices) and the distances between them as edges.

### 4. Dijkstra's Algorithm

Finds the shortest distance from one delivery location to other locations.

### 5. Nearest Neighbor Algorithm

Starts from the depot and repeatedly visits the nearest unvisited delivery location.

### 6. 2-opt Algorithm

Improves the delivery route by changing the order of locations whenever a shorter route is found.

## 🔄 Working of the Project

```text
          START
            |
            v
      Enter Parcel Data
            |
            v
       Sort Parcels
            |
            v
     Optimize Parcel
         Packing
            |
            v
      Select Parcels
            |
            v
     Create Delivery
          Graph
            |
            v
    Apply Dijkstra's
        Algorithm
            |
            v
     Generate Initial
       Delivery Route
            |
            v
       Apply 2-opt
            |
            v
      Final Optimized
       Delivery Route
            |
            v
      Generate Delivery
          Report
            |
            v
           END
```

## 🚀 How to Run the Project

### Requirements

- Python 3.8 or above.
- VS Code, PyCharm, or any Python IDE.

### Step 1: Open the Project Folder

```bash
cd smart_courier
```

### Step 2: Run the Main File

```bash
python main.py
```

No additional libraries need to be installed.

## 📊 Sample Input

The project uses sample parcel data.

| Parcel ID | Destination | Weight | Volume | Priority | Value |
|---|---|---:|---:|---:|---:|
| P1 | A | 4 | 3 | 5 | 100 |
| P2 | B | 3 | 2 | 4 | 80 |
| P3 | C | 5 | 4 | 3 | 90 |
| P4 | D | 2 | 2 | 5 | 120 |
| P5 | A | 3 | 3 | 2 | 60 |
| P6 | E | 4 | 2 | 4 | 110 |
| P7 | C | 2 | 1 | 5 | 70 |

### Vehicle Capacity

- Maximum Weight: 15 units
- Maximum Volume: 12 units

## 📈 Expected Output

When the program runs, it displays:

1. Sorted parcels.
2. Selected parcels for delivery.
3. Total parcel value.
4. Total weight and volume.
5. Shortest distance matrix.
6. Initial delivery route.
7. Optimized delivery route.
8. Total delivery distance.
9. Delivery manifest showing parcels for each destination.

## ⏱️ Time Complexity

| Algorithm | Time Complexity |
|---|---|
| Sorting | O(n log n) |
| Knapsack DP | O(n × W × C) |
| Graph Construction | O(V²) |
| Dijkstra | O((V + E) log V) |
| Nearest Neighbor | O(V²) |
| 2-opt | O(V³) per iteration |

Where:

- n = Number of parcels.
- W = Maximum vehicle weight.
- C = Maximum vehicle volume.
- V = Number of locations.
- E = Number of graph edges.
