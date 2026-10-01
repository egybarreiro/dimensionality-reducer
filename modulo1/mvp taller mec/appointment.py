# Represents a service appointment created by a customer.
# Stores appointment information, associated customer,
# vehicle, customer concern, and appointment status.
class Appointment:


    # Class variable used to generate unique appointment numbers.
    appointment_counter = 1001


    def __init__(
        self,
        customer,
        vehicle,
        appointment_date,
        customer_concern
    ):

        # Validate required information.

        if customer is None:
            raise ValueError(
                "Customer is required."
            )

        if vehicle is None:
            raise ValueError(
                "Vehicle is required."
            )

        if not appointment_date or not appointment_date.strip():
            raise ValueError(
                "Appointment date is required."
            )

        if not customer_concern or not customer_concern.strip():
            raise ValueError(
                "Customer concern is required."
            )


        # Generates a unique appointment number.

        self.appointment_id = (
            f"APT-{Appointment.appointment_counter:04d}"
        )

        Appointment.appointment_counter += 1



        # Customer and vehicle associated with this appointment.

        self.customer = customer
        self.vehicle = vehicle



        # Scheduled appointment information.

        self.appointment_date = appointment_date



        # Customer description of the vehicle concern.

        self.customer_concern = customer_concern.strip()



        # Appointment status is controlled internally.
        # Changes should occur through class methods only.

        self._status = "Scheduled"



    # Changes appointment status when vehicle arrives.
    def check_in(self):

        # Only scheduled appointments can be checked in.

        if self._status != "Scheduled":

            raise ValueError(
                "Only scheduled appointments can be checked in."
            )


        self._status = "Checked In"


        return "Appointment successfully checked in."



    # Cancels the appointment.
    def cancel_appointment(self):

        # Prevents cancelling an already cancelled appointment.

        if self._status == "Cancelled":

            raise ValueError(
                "Appointment is already cancelled."
            )


        self._status = "Cancelled"


        return "Appointment successfully cancelled."



    # Returns the current appointment status.

    def get_status(self):

        return self._status



    # Generates appointment information summary.

    def display_appointment_summary(self):

        return (
            f"Appointment Information\n"
            f"-----------------------\n"
            f"Appointment ID: {self.appointment_id}\n"
            f"Customer: {self.customer.name}\n"
            f"Vehicle: {self.vehicle.make} {self.vehicle.model} ({self.vehicle.year})\n"
            f"Date: {self.appointment_date}\n"
            f"Customer Concern: {self.customer_concern}\n"
            f"Status: {self._status}"
        )



    # Returns a string representation of the appointment.

    def __str__(self):

        return (
            f"{self.appointment_id} - "
            f"{self.vehicle.make} {self.vehicle.model} - "
            f"Status: {self._status}"
        )