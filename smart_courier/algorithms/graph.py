
import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt


# Calculate Euclidean distance
def distance(a, b):

    return math.sqrt(
        (a.x - b.x) ** 2 +
        (a.y - b.y) ** 2
    )


# Generate weighted graph automatically
def build_graph(locations):

    graph = {}

    names = list(locations.keys())

    for name in names:
        graph[name] = {}

    for i in range(len(names)):

        for j in range(i + 1, len(names)):

            a = names[i]
            b = names[j]

            d = distance(
                locations[a],
                locations[b]
            )

            graph[a][b] = d
            graph[b][a] = d

    return graph


# Display graph connections in terminal
def display_graph(graph):

    print("\n========== GENERATED DELIVERY GRAPH ==========")

    for node, neighbors in graph.items():

        print(f"\n{node}:")

        for neighbor, weight in neighbors.items():

            print(
                f"  {node} --> {neighbor} "
                f"(Distance: {weight:.2f})"
            )


# Generate visual graph
def visualize_graph(graph, locations):

    G = nx.Graph()

    # Add nodes
    for name in locations:
        G.add_node(name)

    # Add edges and weights
    for node, neighbors in graph.items():

        for neighbor, weight in neighbors.items():

            G.add_edge(
                node,
                neighbor,
                weight=round(weight, 2)
            )

    # Use actual input coordinates
    pos = {
        name: (loc.x, loc.y)
        for name, loc in locations.items()
    }

    plt.figure(figsize=(10, 7))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=1800,
        font_size=11,
        font_weight="bold",
        edge_color="gray",
        width=1.8
    )

    # Display edge distances
    edge_labels = nx.get_edge_attributes(
        G, "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=9
    )

    plt.title("Smart Courier - Delivery Graph")

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    plt.tight_layout()

    plt.show()


# Dijkstra's shortest path algorithm
def dijkstra(graph, start):

    distances = {
        node: float("inf")
        for node in graph
    }

    previous = {
        node: None
        for node in graph
    }

    distances[start] = 0

    pq = [(0, start)]

    while pq:

        current_dist, current = heapq.heappop(pq)

        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph[current].items():

            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:

                distances[neighbor] = new_dist

                previous[neighbor] = current

                heapq.heappush(
                    pq,
                    (new_dist, neighbor)
                )

    return distances, previous


# Generate shortest distance matrix
def distance_matrix(graph):

    matrix = {}

    for node in graph:

        distances, _ = dijkstra(graph, node)

        matrix[node] = distances

    return matrix


# Display shortest distance matrix
def display_matrix(matrix):

    nodes = list(matrix.keys())

    print("\n========== DISTANCE MATRIX ==========")

    print(f"{'FROM/TO':<12}", end="")

    for node in nodes:
        print(f"{node:<12}", end="")

    print()

    for source in nodes:

        print(f"{source:<12}", end="")

        for target in nodes:

            print(
                f"{matrix[source][target]:<12.2f}",
                end=""
            )

        print()
