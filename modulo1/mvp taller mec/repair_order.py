from datetime import datetime


# Represents a repair order created by the automotive repair shop.
# Stores customer, vehicle, service advisor, repair lines,
# and the repair process timeline.
class RepairOrder:


    # Class variable used to generate unique repair order numbers.
    order_counter = 1


    def __init__(self, customer, vehicle, service_advisor, repair_lines):

        # Validate required information.

        if customer is None:
            raise ValueError("Customer is required.")

        if vehicle is None:
            raise ValueError("Vehicle is required.")

        if service_advisor is None:
            raise ValueError("Service advisor is required.")

        if not repair_lines:
            raise ValueError(
                "At least one repair line is required."
            )


        # Generates a unique repair order number.
        self.repair_order_number = (
            f"RO-{RepairOrder.order_counter:04d}"
        )

        RepairOrder.order_counter += 1


        # Information associated with this repair order.
        self.customer = customer
        self.vehicle = vehicle
        self.service_advisor = service_advisor


        # Creates an independent list of repair lines.
        self.repair_lines = list(repair_lines)


        # Protected repair process information.
        # These attributes should only change through class methods.
        self._check_in_timestamp = datetime.now()
        self._completion_timestamp = None
        self._status = "Opened"


        # Registers repair order in vehicle history.
        self.vehicle.add_repair_order(self)



    # Adds a repair line to the repair order.
    def add_repair_line(self, repair_line):

        if repair_line is None:
            raise ValueError(
                "A valid repair line is required."
            )

        self.repair_lines.append(repair_line)

        return "Repair line successfully added."



    # Completes the repair order and records completion time.
    def complete_repair_order(self):

        # A repair order can only be completed
        # while it is in the opened state.
        if self._status != "Opened":

            raise ValueError(
                "Only opened repair orders can be completed."
            )


        self._status = "Completed"

        self._completion_timestamp = datetime.now()


        return "Repair order completed successfully."



    # Returns the current repair order status.
    def get_status(self):

        return self._status



    # Returns the check-in timestamp.
    def get_check_in_timestamp(self):

        return self._check_in_timestamp



    # Returns the completion timestamp.
    def get_completion_timestamp(self):

        return self._completion_timestamp



    # Formats timestamps for display.
    def format_timestamp(self, timestamp):

        if timestamp is None:
            return "Pending"

        return timestamp.strftime(
            "%m/%d/%Y %I:%M %p"
        )



    # Generates repair order information summary.
    def display_repair_order_summary(self):

        return (
            f"Repair Order Information\n"
            f"------------------------\n"
            f"Repair Order Number: {self.repair_order_number}\n"
            f"Customer: {self.customer.name}\n"
            f"Vehicle: {self.vehicle.make} {self.vehicle.model} ({self.vehicle.year})\n"
            f"Service Advisor: {self.service_advisor.name} {self.service_advisor.last_name}\n"
            f"Repair Lines: {len(self.repair_lines)}\n"
            f"Check In: {self.format_timestamp(self._check_in_timestamp)}\n"
            f"Completed: {self.format_timestamp(self._completion_timestamp)}\n"
            f"Status: {self._status}"
        )



    # Returns a string representation of the repair order.
    def __str__(self):

        return (
            f"Repair Order #{self.repair_order_number}\n"
            f"Vehicle: {self.vehicle.make} {self.vehicle.model}\n"
            f"Status: {self._status}"
        )