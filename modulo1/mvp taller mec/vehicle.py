# Represents a vehicle registered in the automotive repair shop.
# Stores vehicle identification information, usage type,
# and related repair history.


class Vehicle:


    def __init__(
        self,
        make,
        model,
        year,
        color,
        mileage,
        vin,
        license_plate=None,
        usage_type=None
    ):


        # Validate vehicle information.

        if not make or not make.strip():

            raise ValueError(
                "Vehicle make is required."
            )


        if not any(char.isalpha() for char in make):

            raise ValueError(
                "Vehicle make must contain letters."
            )



        if not model or not model.strip():

            raise ValueError(
                "Vehicle model is required."
            )


        if not any(char.isalpha() for char in model):

            raise ValueError(
                "Vehicle model must contain letters."
            )



        if not isinstance(year, int):

            raise ValueError(
                "Vehicle year must be a number."
            )


        if year < 1886:

            raise ValueError(
                "Invalid vehicle year."
            )



        if not color or not color.strip():

            raise ValueError(
                "Vehicle color is required."
            )


        if not any(char.isalpha() for char in color):

            raise ValueError(
                "Vehicle color must contain letters."
            )



        if not isinstance(mileage, (int, float)):

            raise ValueError(
                "Vehicle mileage must be numeric."
            )


        if mileage < 0:

            raise ValueError(
                "Vehicle mileage cannot be negative."
            )



        if not vin or not vin.strip():

            raise ValueError(
                "Vehicle VIN is required."
            )



        if not usage_type or not usage_type.strip():

            raise ValueError(
                "Vehicle usage type is required."
            )



        allowed_usage_types = [

            "Personal",
            "Commercial",
            "Fleet",
            "PDI"

        ]



        if usage_type not in allowed_usage_types:

            raise ValueError(
                "Invalid vehicle usage type."
            )



        # Vehicle identification information.
        # Data is cleaned before storage.

        self.make = make.strip()

        self.model = model.strip()

        self.year = year

        self.color = color.strip()

        self.mileage = mileage

        self.vin = vin.strip()


        self.license_plate = (

            license_plate.strip()

            if license_plate

            else None

        )


        # Defines the purpose of the vehicle.
        # Examples:
        # Personal vehicle
        # Commercial vehicle
        # Fleet vehicle
        # Dealer PDI vehicle

        self.usage_type = usage_type



        # Stores repair orders related
        # to this vehicle.

        self._repair_history = []



    # Adds a repair order to vehicle history.

    def add_repair_order(
        self,
        repair_order
    ):


        if repair_order is None:

            raise ValueError(
                "A valid repair order is required."
            )


        self._repair_history.append(
            repair_order
        )


        return "Repair order successfully added."



    # Returns vehicle repair history.

    def get_repair_history(self):

        return self._repair_history



    # Generates vehicle information summary.

    def display_vehicle_summary(self):


        repair_order_count = len(
            self._repair_history
        )


        return (

            f"Vehicle Information\n"

            f"--------------------\n"

            f"Make: {self.make}\n"

            f"Model: {self.model}\n"

            f"Year: {self.year}\n"

            f"Color: {self.color}\n"

            f"Mileage: {self.mileage}\n"

            f"VIN: {self.vin}\n"

            f"License Plate: "
            f"{self.license_plate if self.license_plate else 'Not Assigned'}\n"

            f"Usage Type: {self.usage_type}\n"

            f"Repair Orders: {repair_order_count}"

        )



    # Returns string representation of vehicle.

    def __str__(self):

        return self.display_vehicle_summary()