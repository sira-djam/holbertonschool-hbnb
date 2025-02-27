#!/user/bin/python3


from app.models.basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        self.name = self.validate_name(name)

    def validate_name(self, name):
        if not name:
            raise ValueError("Amenity name must be provided.")
        if len(name) > 50:
            raise ValueError("Amenity name must be less than or equal to 50 characters.")
        return name

    def __str__(self):
        return (f"Amenity({self.id}, {self.name}, "
                f"Created at: {self.created_at}, Last updated: {self.updated_at})")
