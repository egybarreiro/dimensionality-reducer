# Represents the automotive repair shop management system.
# Acts as the central manager for customers, vehicles,
# and repair orders using dictionaries and sets.


class Workshop:


    def __init__(self):

        # Dictionary that stores customers.
        # Key: customer_id
        # Value: Customer object

        self.customers = {}



        # Set that stores customer emails.
        # Used to prevent duplicate customers.

        self.registered_emails = set()



        # Dictionary that stores vehicles.
        # Key: VIN
        # Value: Vehicle object

        self.vehicles = {}



        # Set that stores registered license plates.
        # Used to prevent duplicate plates.

        self.registered_plates = set()



        # Dictionary that stores repair orders.
        # Key: repair_order_number
        # Value: RepairOrder object

        self.repair_orders = {}




    # Registers a customer in the workshop system.

    def register_customer(self, customer):

        if customer is None:

            raise ValueError(
                "A valid customer is required."
            )


        if customer.customer_id in self.customers:

            raise ValueError(
                "Customer is already registered."
            )


        if customer.email in self.registered_emails:

            raise ValueError(
                "Customer email is already registered."
            )


        self.customers[
            customer.customer_id
        ] = customer


        self.registered_emails.add(
            customer.email
        )


        return "Customer successfully registered."




    # Registers a vehicle in the workshop system.

    def register_vehicle(self, vehicle):

        if vehicle is None:

            raise ValueError(
                "A valid vehicle is required."
            )


        if vehicle.vin in self.vehicles:

            raise ValueError(
                "Vehicle is already registered."
            )


        if vehicle.license_plate:

            if vehicle.license_plate in self.registered_plates:

                raise ValueError(
                    "License plate is already registered."
                )



        self.vehicles[
            vehicle.vin
        ] = vehicle



        if vehicle.license_plate:

            self.registered_plates.add(
                vehicle.license_plate
            )


        return "Vehicle successfully registered."




    # Registers a repair order in the workshop system.

    def register_repair_order(self, repair_order):

        if repair_order is None:

            raise ValueError(
                "A valid repair order is required."
            )


        if repair_order.repair_order_number in self.repair_orders:

            raise ValueError(
                "Repair order is already registered."
            )


        self.repair_orders[
            repair_order.repair_order_number
        ] = repair_order


        return "Repair order successfully registered."




    # Searches for a customer by ID.

    def find_customer(self, customer_id):

        return self.customers.get(
            customer_id
        )




    # Searches for a vehicle by VIN.

    def find_vehicle(self, vin):

        return self.vehicles.get(
            vin
        )




    # Searches for a vehicle by license plate.

    def find_vehicle_by_license_plate(
        self,
        license_plate
    ):

        if not license_plate:

            raise ValueError(
                "License plate information is required."
            )


        for vehicle in self.vehicles.values():

            if vehicle.license_plate == license_plate:

                return vehicle


        return None




    # Searches for a repair order by number.

    def find_repair_order(
        self,
        repair_order_number
    ):

        return self.repair_orders.get(
            repair_order_number
        )




    # Returns all vehicles associated
    # with a specific customer.

    def find_customer_vehicles(
        self,
        customer_id
    ):

        customer = self.find_customer(
            customer_id
        )


        if customer is None:

            raise ValueError(
                "Customer not found."
            )


        return customer.current_vehicles




    # Returns all repair orders associated
    # with a specific customer.

    def find_customer_repair_orders(
        self,
        customer_id
    ):

        customer = self.find_customer(
            customer_id
        )


        if customer is None:

            raise ValueError(
                "Customer not found."
            )


        customer_vehicles = customer.current_vehicles


        customer_orders = []


        for vehicle in customer_vehicles:

            customer_orders.extend(
                vehicle.get_repair_history()
            )


        return customer_orders