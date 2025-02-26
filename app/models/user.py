#!/user/bin/python3
'''create class user'''


import re
from datetime import datetime

class User:
    def __init__(self, id, first_name, last_name, email, is_admin=False):
        self.id = id
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def validate_first_name(self, first_name):
        if not first_name or len(first_name) > 50:
            raise ValueError("First name must be non-empty and less than or equal to 50 characters.")
        return first_name

    def validate_last_name(self, last_name):
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name must be non-empty and less than or equal to 50 characters.")
        return last_name

    def validate_email(self, email):
        # Basic email validation using a regular expression
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Email must be in a valid format.")
        # Assuming we would check for email uniqueness in a larger system
        return email

    def update(self, first_name=None, last_name=None, email=None, is_admin=None):
        if first_name:
            self.first_name = self.validate_first_name(first_name)
        if last_name:
            self.last_name = self.validate_last_name(last_name)
        if email:
            self.email = self.validate_email(email)
        if is_admin is not None:
            self.is_admin = is_admin
        self.updated_at = datetime.now()

    def __str__(self):
        return f"User({self.id}, {self.first_name} {self.last_name}, {self.email}, Admin: {self.is_admin}, Created at: {self.created_at}, Last updated: {self.updated_at})"

# Example Usage
try:
    user = User(id="12345", first_name="John", last_name="Doe", email="john.doe@example.com")
    print(user)

    # Update user information
    user.update(first_name="Jane", email="jane.doe@example.com", is_admin=True)
    print(user)
except ValueError as e:
    print(f"Error: {e}")



