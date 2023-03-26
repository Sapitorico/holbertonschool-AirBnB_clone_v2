#!/usr/bin/python3
"""Unittest for DBStorage"""
import unittest
from models import storage
from models.user import User
from os import getenv


class TestDBStorage(unittest.TestCase):
    """Defines the TestDBStorage class"""

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'only testing db storage')
    def test_all(self):
        """Test the all() method"""
        # Create a new user and save it
        user = User(email="test@test.com", password="testpass")
        user.save()
        # Test if the user is in the database
        objs = storage.all(User)
        self.assertIn(user, objs.values())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'only testing db storage')
    def test_new(self):
        """Test the new() method"""
        # Create a new user and save it
        user = User(email="test@test.com", password="testpass")
        storage.new(user)
        # Test if the user is in the database
        objs = storage.all(User)
        self.assertIn(user, objs.values())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'only testing db storage')
    def test_save(self):
        """Test the save() method"""
        # Create a new user and save it
        user = User(email="test@test.com", password="testpass")
        storage.new(user)
        storage.save()
        # Test if the user is in the database
        objs = storage.all(User)
        self.assertIn(user, objs.values())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'only testing db storage')
    def test_delete(self):
        """Test the delete() method"""
        # Create a new user and save it
        user = User(email="test@test.com", password="testpass")
        storage.new(user)
        storage.save()
        # Delete the user
        storage.delete(user)
        # Test if the user was removed from the database
        objs = storage.all(User)
        self.assertNotIn(user, objs.values())
