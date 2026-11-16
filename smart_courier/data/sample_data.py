
from dataclasses import dataclass


@dataclass
class Parcel:
    parcel_id: str
    destination: str
    weight: int
    volume: int
    priority: int
    value: int


@dataclass
class Location:
    name: str
    x: float
    y: float


def get_sample_data():

    parcels = [
        Parcel("P1", "A", 4, 3, 5, 100),
        Parcel("P2", "B", 3, 2, 4, 80),
        Parcel("P3", "C", 5, 4, 3, 90),
        Parcel("P4", "D", 2, 2, 5, 120),
        Parcel("P5", "A", 3, 3, 2, 60),
        Parcel("P6", "E", 4, 2, 4, 110),
        Parcel("P7", "C", 2, 1, 5, 70),
    ]

    locations = {
        "DEPOT": Location("DEPOT", 0, 0),
        "A": Location("A", 2, 3),
        "B": Location("B", 5, 4),
        "C": Location("C", 6, 1),
        "D": Location("D", 1, 6),
        "E": Location("E", 8, 5),
    }

    max_weight = 15
    max_volume = 12

    return parcels, locations, max_weight, max_volume


def get_user_data():

    print("\n========== ENTER CUSTOM DATA ==========")

    max_weight = int(input("Enter maximum vehicle weight: "))
    max_volume = int(input("Enter maximum vehicle volume: "))

    if max_weight <= 0 or max_volume <= 0:
        raise ValueError("Vehicle capacities must be positive.")

    n = int(input("\nEnter number of delivery locations: "))

    if n < 1:
        raise ValueError("Enter at least one location.")

    locations = {
        "DEPOT": Location("DEPOT", 0, 0)
    }

    for i in range(n):

        print(f"\nLocation {i + 1}")

        name = input("Enter location name: ").strip()

        if not name or name in locations:
            raise ValueError("Location names must be unique and non-empty.")

        x = float(input("Enter X coordinate: "))
        y = float(input("Enter Y coordinate: "))

        locations[name] = Location(name, x, y)

    parcel_count = int(input("\nEnter number of parcels: "))

    if parcel_count < 1:
        raise ValueError("Enter at least one parcel.")

    parcels = []

    for i in range(parcel_count):

        print(f"\nParcel {i + 1}")

        parcel_id = input("Enter parcel ID: ").strip()

        if not parcel_id or any(
            p.parcel_id == parcel_id for p in parcels
        ):
            raise ValueError("Parcel IDs must be unique and non-empty.")

        destination = input("Enter destination: ").strip()

        if destination not in locations or destination == "DEPOT":
            raise ValueError("Destination does not exist.")

        weight = int(input("Enter weight: "))
        volume = int(input("Enter volume: "))
        priority = int(input("Enter priority (1-5): "))
        value = int(input("Enter parcel value: "))

        if weight <= 0 or volume <= 0 or value < 0:
            raise ValueError("Weight and volume must be positive; value cannot be negative.")

        if not 1 <= priority <= 5:
            raise ValueError("Priority must be between 1 and 5.")

        parcels.append(
            Parcel(
                parcel_id,
                destination,
                weight,
                volume,
                priority,
                value
            )
        )

    return parcels, locations, max_weight, max_volume


def get_data():

    print("\n======================================")
    print("     SMART COURIER OPTIMIZATION")
    print("======================================")

    print("\n1. Use Sample Data")
    print("2. Enter Custom Data")

    choice = input("\nSelect an option (1/2): ").strip()

    if choice == "1":

        print("\nSample data selected!")

        return get_sample_data()

    elif choice == "2":

        return get_user_data()

    else:

        raise ValueError("Invalid choice! Please select 1 or 2.")
