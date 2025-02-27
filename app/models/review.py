#!/user/bin/python3

from app.models.basemodel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)

    def validate_text(self, text):
        if not text:
            raise ValueError("Review text must be provided.")
        return text

    def validate_rating(self, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def validate_place(self, place):
        from app.models.place import Place
        if not isinstance(place, Place):
            raise ValueError("Place must be a valid Place instance.")
        return place

    def validate_user(self, user):
        from app.models.user import User
        if not isinstance(user, User):
            raise ValueError("User must be a valid User instance.")
        return user

    def __str__(self):
        return (f"Review({self.id}, {self.text[:30]}..., Rating: {self.rating}, "
                f"Place: {self.place.title}, User: {self.user.first_name} {self.user.last_name}, "
                f"Created at: {self.created_at}, Last updated: {self.updated_at})")
