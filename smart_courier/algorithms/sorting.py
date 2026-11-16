
def sort_parcels(parcels):

    sorted_parcels = sorted(
        parcels,
        key=lambda p: (
            -p.priority,
            -p.value,
            p.weight
        )
    )

    return sorted_parcels
