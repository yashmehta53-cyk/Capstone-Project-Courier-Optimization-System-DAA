
from data.sample_data import get_data

from services.courier_service import run_courier_system


def main():

    try:

        parcels, locations, max_weight, max_volume = get_data()

        run_courier_system(
            parcels,
            locations,
            max_weight,
            max_volume
        )

    except ValueError as error:

        print("\nInput Error:", error)

    except (EOFError, KeyboardInterrupt):

        print("\nProgram cancelled by user.")


if __name__ == "__main__":

    main()
