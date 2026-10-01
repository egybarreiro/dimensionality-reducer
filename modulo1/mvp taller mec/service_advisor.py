from class_repair_lines import RepairLine
from class_repair_order import RepairOrder



# Represents a service advisor working at the automotive repair shop.
# Handles customer check-in process, documents customer concerns,
# and creates repair orders after vehicle arrival.

class ServiceAdvisor:



    def __init__(
        self,
        advisor_id,
        name,
        last_name
    ):


        # Validate advisor information.

        if not advisor_id:

            raise ValueError(
                "Advisor ID is required."
            )


        if not name or not name.strip():

            raise ValueError(
                "Advisor name is required."
            )


        if not last_name or not last_name.strip():

            raise ValueError(
                "Advisor last name is required."
            )



        # Stores advisor identification information.

        self.advisor_id = advisor_id

        self.name = name.strip()

        self.last_name = last_name.strip()




    # Checks in a customer's appointment.

    def check_in_vehicle(
        self,
        appointment
    ):


        if appointment is None:

            raise ValueError(
                "Appointment is required."
            )


        return appointment.check_in()




    # Creates a repair line based on a customer concern.

    def add_repair_line(
        self,
        description
    ):


        repair_line = RepairLine(
            description
        )


        return repair_line




    # Creates a repair order after vehicle check-in.

    def create_repair_order(
        self,
        appointment,
        repair_lines
    ):


        if appointment is None:

            raise ValueError(
                "Appointment is required."
            )


        if not repair_lines:

            raise ValueError(
                "At least one repair line is required."
            )



        # Repair orders can only be created
        # after the vehicle has been checked in.

        if appointment.get_status() != "Checked In":

            raise ValueError(
                "Vehicle must be checked in before creating a repair order."
            )



        repair_order = RepairOrder(

            appointment.customer,

            appointment.vehicle,

            self,

            repair_lines

        )



        return repair_order




    # Returns a string representation
    # of the service advisor.

    def __str__(self):


        return (

            f"Service Advisor Information\n"

            f"---------------------------\n"

            f"Advisor ID: {self.advisor_id}\n"

            f"Name: {self.name} {self.last_name}"

        )