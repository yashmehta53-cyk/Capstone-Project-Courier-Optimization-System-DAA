
def calculate_route_distance(route, matrix):

    total = 0

    for i in range(len(route) - 1):

        total += matrix[route[i]][route[i + 1]]

    return total


def nearest_neighbor(start, destinations, matrix):

    unvisited = set(destinations)

    route = [start]

    current = start

    while unvisited:

        next_stop = min(
            unvisited,
            key=lambda x: matrix[current][x]
        )

        route.append(next_stop)

        unvisited.remove(next_stop)

        current = next_stop

    route.append(start)

    return route


def two_opt(route, matrix):

    best = route[:]

    improved = True

    while improved:

        improved = False

        for i in range(1, len(best) - 2):

            for j in range(i + 1, len(best) - 1):

                new_route = (
                    best[:i] +
                    best[i:j + 1][::-1] +
                    best[j + 1:]
                )

                if (
                    calculate_route_distance(new_route, matrix)
                    < calculate_route_distance(best, matrix) - 1e-9
                ):

                    best = new_route

                    improved = True

    return best
