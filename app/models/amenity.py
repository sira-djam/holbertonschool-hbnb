#!/user/bin/python3


from datetime import datetime

class Amenity:
    def __init__(self, id, name):
        self.id = id
        self.name = self.validate_name(name)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def validate_name(self, name):
        if not name:
            raise ValueError("Amenity name must be provided.")
        if len(name) > 50:
            raise ValueError("Amenity name must be less than or equal to 50 characters.")
        return name

    def update(self, name=None):
        if name:
            self.name = self.validate_name(name)
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"Amenity({self.id}, {self.name}, "
                f"Created at: {self.created_at}, Last updated: {self.updated_at})")

# Example usage
try:
    # Create an amenity
    amenity = Amenity(id="a1", name="Wi-Fi")
    print(amenity)

    # Update the amenity name
    amenity.update(name="Free Wi-Fi")
    print(amenity)

except ValueError as e:
    print(f"Error: {e}")
