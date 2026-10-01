# Represents a repair line created during vehicle check-in.
# Stores a customer concern documented by the service advisor.
# Repair lines preserve the original customer request
# and should not be modified after creation.
class RepairLine:


    def __init__(self, description):

        # Validate repair line description.

        if not description or not description.strip():

            raise ValueError(
                "Repair line description is required."
            )


        # Protected customer concern information.
        # The description should only be assigned during creation.

        self._description = description.strip()



    # Returns the repair line description.
    def get_description(self):

        return self._description



    # Returns a string representation of the repair line.

    def __str__(self):

        return (
            f"Repair Line\n"
            f"------------\n"
            f"Description: {self._description}"
        )