# Capstone-Project-Courier-Optimization-System-DAA


# 🚚 Smart Courier Optimization System

A Python-based project that helps plan parcel packing and delivery routes using different algorithms.

The user can choose predefined sample data or enter their own parcel and location details.

## 📌 Project Overview

The system performs two main tasks:

1. **Parcel Packing:** Selects the best combination of parcels within the vehicle's weight and volume limits.
2. **Route Optimization:** Finds an efficient order for delivering parcels while reducing travel distance.

## 🎯 Objectives

- Sort parcels based on priority.
- Select parcels using Dynamic Programming.
- Generate a delivery graph automatically.
- Find shortest distances between locations.
- Generate and optimize delivery routes.
- Display a final delivery report.

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

## ⚙️ Algorithms Used

1. **Sorting:** Arranges parcels according to priority, value, and weight.
2. **Dynamic Programming (0/1 Knapsack):** Selects parcels within vehicle capacity.
3. **Graph Algorithms:** Represents delivery locations and distances.
4. **Dijkstra's Algorithm:** Finds shortest distances between locations.
5. **Nearest Neighbor:** Generates an initial delivery route.
6. **2-opt:** Improves the delivery route by reducing unnecessary travel.

## 🔄 Working of the Project

1. Choose sample data or enter custom data.
2. Enter vehicle capacity, if using custom data.
3. Sort the parcels.
4. Select parcels using Dynamic Programming.
5. Generate the weighted delivery graph automatically.
6. Calculate shortest distances using Dijkstra.
7. Generate a delivery route using Nearest Neighbor.
8. Improve the route using 2-opt.
9. Display the final delivery report.

## 🚀 How to Run

### Requirements

- Python 3.8 or above.
- VS Code, PyCharm, or any Python IDE.

No external libraries are required for the built-in Python version.

### Step 1: Open the project folder

```bash
cd smart_courier
```

### Step 2: Run the program

```bash
python main.py
```

## 📊 Input Options

When the program starts, it provides two options:

```text
SMART COURIER OPTIMIZATION

1. Use Sample Data
2. Enter Custom Data

Select an option:
```

**Option 1 – Sample Data**

- Loads predefined parcels and delivery locations.
- Uses predefined vehicle weight and volume limits.
- Runs the complete optimization process.

**Option 2 – Custom Data**

Allows users to enter:
- Vehicle maximum weight and volume.
- Delivery location names.
- X and Y coordinates.
- Parcel IDs and destinations.
- Parcel weight and volume.
- Delivery priority.
- Parcel value.

## 📈 Expected Output

The program displays:

- Sorted parcels.
- Selected parcels for delivery.
- Total parcel value.
- Total weight and volume.
- Automatically generated graph connections.
- Shortest distance matrix.
- Initial delivery route.
- Optimized delivery route.
- Total delivery distance.
- Final delivery manifest.

## ⏱️ Time Complexity

| Algorithm | Time Complexity |
|---|---|
| Sorting | O(n log n) |
| Knapsack DP | O(n × W × C) |
| Graph Construction | O(V²) |
| Dijkstra (using heap) | O((V + E) log V) |
| Nearest Neighbor | O(V²) |
| 2-opt | O(V³) per iteration |

### Variables

- n = Number of parcels.
- W = Maximum vehicle weight.
- C = Maximum vehicle volume.
- V = Number of delivery locations.
- E = Number of graph edges.
