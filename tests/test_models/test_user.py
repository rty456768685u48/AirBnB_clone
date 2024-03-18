#!/usr/bin/python3
"""
Test suits for amenities
"""
import os
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """
    Each test method focuses on testing a specific attribute of the User model.
    """

    def test_email_attribute(self):
        """
        Test that the email attribute of User is set correctly.
        """
        user = User(email="user@example.com")
        self.assertEqual(user.email, "user@example.com")

    def test_password_attribute(self):
        """
        Test that the password attribute of User is set correctly.
        """
        user = User(password="securepassword")
        self.assertEqual(user.password, "securepassword")

    def test_first_name_attribute(self):
        """
        Test that the first_name attribute of User is set correctly.
        """
        user = User(first_name="John")
        self.assertEqual(user.first_name, "John")

    def test_last_name_attribute(self):
        """
        Test that the last_name attribute of User is set correctly.
        """
        user = User(last_name="Doe")
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
