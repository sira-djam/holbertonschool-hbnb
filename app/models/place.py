#!/user/bin/python3
'''creat class place'''

from datetime import datetime

from app.models.user import User


class Place:
    def __init__(self, id, title, description, price, latitude, longitude, owner):
        self.id = id
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def validate_title(self, title):
        if not title or len(title) > 100:
            raise ValueError("Title must be non-empty and less than or equal to 100 characters.")
        return title

    def validate_price(self, price):
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        return price

    def validate_latitude(self, latitude):
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        return latitude

    def validate_longitude(self, longitude):
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        return longitude

    def validate_owner(self, owner):
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance.")
        return owner

    def update(self, title=None, description=None, price=None, latitude=None, longitude=None):
        if title:
            self.title = self.validate_title(title)
        if description:
            self.description = description
        if price is not None:
            self.price = self.validate_price(price)
        if latitude is not None:
            self.latitude = self.validate_latitude(latitude)
        if longitude is not None:
            self.longitude = self.validate_longitude(longitude)
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"Place({self.id}, {self.title}, {self.price}, "
                f"Latitude: {self.latitude}, Longitude: {self.longitude}, "
                f"Owner: {self.owner.first_name} {self.owner.last_name}, "
                f"Created at: {self.created_at}, Last updated: {self.updated_at})")
