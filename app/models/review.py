#!/user/bin/python3


from datetime import datetime
from app.models.place import Place
from app.models.user import User

class Review:
    def __init__(self, id, text, rating, place, user):
        self.id = id
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def validate_text(self, text):
        if not text:
            raise ValueError("Review text must be provided.")
        return text

    def validate_rating(self, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def validate_place(self, place):
        if not isinstance(place, Place):
            raise ValueError("Place must be a valid Place instance.")
        return place

    def validate_user(self, user):
        if not isinstance(user, User):
            raise ValueError("User must be a valid User instance.")
        return user

    def update(self, text=None, rating=None):
        if text:
            self.text = self.validate_text(text)
        if rating is not None:
            self.rating = self.validate_rating(rating)
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"Review({self.id}, {self.text[:30]}..., Rating: {self.rating}, "
                f"Place: {self.place.title}, User: {self.user.first_name} {self.user.last_name}, "
                f"Created at: {self.created_at}, Last updated: {self.updated_at})")

# Example usage
try:
    user = User(id="1", first_name="John", last_name="Doe", email="john.doe@example.com")
    place = Place(
        id="p1",
        title="Cozy Cottage",
        description="A small, cozy cottage by the lake.",
        price=100.0,
        latitude=45.0,
        longitude=-93.0,
        owner=user
    )

    # Create a review
    review = Review(
        id="r1",
        text="A wonderful place to stay! Highly recommend it to anyone looking for a peaceful getaway.",
        rating=5,
        place=place,
        user=user
    )
    print(review)

    # Update review
    review.update(text="An even better place now! Still highly recommend.", rating=4)
    print(review)

except ValueError as e:
    print(f"Error: {e}")
