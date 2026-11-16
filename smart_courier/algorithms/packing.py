

def optimize_packing(parcels, max_weight, max_volume):

    n = len(parcels)

    dp = [
        [
            [0 for _ in range(max_volume + 1)]
            for _ in range(max_weight + 1)
        ]
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        p = parcels[i - 1]

        for w in range(max_weight + 1):
            for v in range(max_volume + 1):

                dp[i][w][v] = dp[i - 1][w][v]

                if p.weight <= w and p.volume <= v:

                    value = (
                        dp[i - 1][w - p.weight]
                        [v - p.volume] + p.value
                    )

                    dp[i][w][v] = max(
                        dp[i][w][v],
                        value
                    )

    selected = []

    w = max_weight
    v = max_volume

    for i in range(n, 0, -1):

        if dp[i][w][v] != dp[i - 1][w][v]:

            p = parcels[i - 1]

            selected.append(p)

            w -= p.weight
            v -= p.volume

    selected.reverse()

    return selected, dp[n][max_weight][max_volume]
