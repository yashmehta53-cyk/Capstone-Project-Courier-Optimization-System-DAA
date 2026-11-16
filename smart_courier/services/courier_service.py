
from algorithms.sorting import sort_parcels

from algorithms.packing import optimize_packing

from algorithms.graph import (
    build_graph,
    display_graph,
    visualize_graph,
    distance_matrix,
    display_matrix
)

from algorithms.routing import (
    nearest_neighbor,
    two_opt,
    calculate_route_distance
)


def run_courier_system(
    parcels,
    locations,
    max_weight,
    max_volume
):

    print("\n========== SMART COURIER SYSTEM ==========")

    print("\n--- 1. SORTED PARCELS ---")

    sorted_parcels = sort_parcels(parcels)

    for p in sorted_parcels:

        print(
            f"{p.parcel_id} | Destination: {p.destination} "
            f"| Priority: {p.priority} "
            f"| Value: {p.value}"
        )

    print("\n--- 2. OPTIMIZED PACKING ---")

    selected, total_value = optimize_packing(
        sorted_parcels,
        max_weight,
        max_volume
    )

    total_weight = sum(p.weight for p in selected)
    total_volume = sum(p.volume for p in selected)

    print("\nSelected parcels:")

    for p in selected:

        print(
            f"{p.parcel_id} -> {p.destination} "
            f"| Weight: {p.weight} "
            f"| Volume: {p.volume}"
        )

    print("\nTotal Value:", total_value)

    print(
        f"Total Weight: {total_weight}/{max_weight}"
    )

    print(
        f"Total Volume: {total_volume}/{max_volume}"
    )

    destinations = sorted({
        p.destination for p in selected
    })

    if not destinations:

        print("\nNo parcels fit the vehicle capacity.")

        return None

    print("\n--- 3. GRAPH GENERATION ---")

    graph = build_graph(locations)

    display_graph(graph)

    print("\nOpening delivery graph...")

    visualize_graph(graph, locations)

    print("\n--- 4. DIJKSTRA SHORTEST DISTANCES ---")

    matrix = distance_matrix(graph)

    display_matrix(matrix)

    print("\n--- 5. INITIAL DELIVERY ROUTE ---")

    initial_route = nearest_neighbor(
        "DEPOT",
        destinations,
        matrix
    )

    initial_distance = calculate_route_distance(
        initial_route,
        matrix
    )

    print(
        "Initial Route:",
        " -> ".join(initial_route)
    )

    print(
        "Initial Distance:",
        round(initial_distance, 2)
    )

    print("\n--- 6. OPTIMIZED DELIVERY ROUTE ---")

    optimized_route = two_opt(
        initial_route,
        matrix
    )

    optimized_distance = calculate_route_distance(
        optimized_route,
        matrix
    )

    print(
        "Optimized Route:",
        " -> ".join(optimized_route)
    )

    print(
        "Optimized Distance:",
        round(optimized_distance, 2)
    )

    improvement = (
        (initial_distance - optimized_distance)
        / initial_distance * 100
        if initial_distance > 0 else 0
    )

    print(
        "Distance Improvement:",
        round(improvement, 2),
        "%"
    )

    print("\n--- 7. DELIVERY MANIFEST ---")

    for stop in optimized_route[1:-1]:

        stop_parcels = [
            p.parcel_id
            for p in selected
            if p.destination == stop
        ]

        print(
            f"{stop} -> Parcels: {', '.join(stop_parcels)}"
        )

    print("\n========== FINAL DELIVERY SUMMARY ==========")

    print("Selected Parcels:", len(selected))
    print("Total Parcel Value:", total_value)
    print("Total Weight:", total_weight)
    print("Total Volume:", total_volume)

    print(
        "Final Route:",
        " -> ".join(optimized_route)
    )

    print(
        "Total Travel Distance:",
        round(optimized_distance, 2)
    )

    print("\n========== PLANNING COMPLETE ==========")

    return {
        "selected_parcels": selected,
        "total_value": total_value,
        "total_weight": total_weight,
        "total_volume": total_volume,
        "initial_route": initial_route,
        "optimized_route": optimized_route,
        "initial_distance": initial_distance,
        "optimized_distance": optimized_distance
    }
