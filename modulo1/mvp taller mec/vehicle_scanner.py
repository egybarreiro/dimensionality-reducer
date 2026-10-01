# Represents a vehicle barcode scanner used during vehicle check-in.
# Simulates scanning a vehicle barcode to obtain VIN information.


class VehicleScanner:



    # Simulates scanning a vehicle barcode
    # and returning the VIN information.

    def scan_barcode(
        self,
        barcode
    ):


        if not barcode or not barcode.strip():

            raise ValueError(
                "Barcode information is required."
            )



        return barcode.strip()