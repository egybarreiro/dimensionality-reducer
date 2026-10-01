# Represents a customer of the automotive repair shop.
# Stores customer contact information, customer type,
# and vehicles currently associated with the customer.


class Customer:


    def __init__(
        self,
        customer_id,
        name,
        phone,
        email,
        customer_type
    ):


        # Validate required customer information.

        if not customer_id:

            raise ValueError(
                "Customer ID is required."
            )


        if not name or not name.strip():

            raise ValueError(
                "Customer name is required."
            )


        if not phone or not phone.strip():

            raise ValueError(
                "Customer phone number is required."
            )


        if not email or not email.strip():

            raise ValueError(
                "Customer email is required."
            )


        if not customer_type or not customer_type.strip():

            raise ValueError(
                "Customer type is required."
            )


        allowed_types = [
            "Individual",
            "Commercial",
            "Dealer"
        ]


        if customer_type not in allowed_types:

            raise ValueError(
                "Invalid customer type."
            )



        # Stores customer identification information.
        # Data is cleaned before storage.

        self.customer_id = customer_id

        self.name = name.strip()

        self.phone = phone.strip()

        self.email = email.strip()

        self.customer_type = customer_type



        # Stores vehicles associated
        # with this customer.

        self.current_vehicles = []



    # Registers a vehicle under this customer.

    def register_vehicle(
        self,
        vehicle
    ):


        if vehicle is None:

            raise ValueError(
                "A valid vehicle is required."
            )


        if vehicle in self.current_vehicles:

            raise ValueError(
                "Vehicle is already registered."
            )


        self.current_vehicles.append(
            vehicle
        )


        return "Vehicle successfully registered."



    # Removes a vehicle from customer records.

    def remove_vehicle(
        self,
        vehicle
    ):


        if vehicle in self.current_vehicles:

            self.current_vehicles.remove(
                vehicle
            )

            return "Vehicle successfully removed."


        return "Vehicle not found."



    # Returns vehicles by usage type.

    def get_vehicles_by_usage(
        self,
        usage_type
    ):


        return [

            vehicle

            for vehicle in self.current_vehicles

            if vehicle.usage_type == usage_type

        ]



    # Updates customer contact information.

    def update_contact_information(
        self,
        name=None,
        phone=None,
        email=None
    ):


        if name is not None:

            if not name.strip():

                raise ValueError(
                    "Customer name cannot be empty."
                )


            self.name = name.strip()



        if phone is not None:

            if not phone.strip():

                raise ValueError(
                    "Customer phone cannot be empty."
                )


            self.phone = phone.strip()



        if email is not None:

            if not email.strip():

                raise ValueError(
                    "Customer email cannot be empty."
                )


            self.email = email.strip()



        return "Customer information successfully updated."



    # Generates customer information summary.

    def display_customer_summary(self):


        vehicle_count = len(
            self.current_vehicles
        )


        return (

            f"Customer Information\n"

            f"--------------------\n"

            f"Customer ID: {self.customer_id}\n"

            f"Name: {self.name}\n"

            f"Phone: {self.phone}\n"

            f"Email: {self.email}\n"

            f"Customer Type: {self.customer_type}\n"

            f"Registered Vehicles: {vehicle_count}"

        )



    # Returns string representation.

    def __str__(self):

        return self.display_customer_summary()