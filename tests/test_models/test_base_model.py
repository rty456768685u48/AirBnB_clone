#!/usr/bin/env python3
"""
This is a test module for the class BaseModel
"""
import unittest
from unittest.mock import patch
from uuid import UUID
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest. TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_init_with_kwargs(self):
        """
        Test if  attributes are correctly initialized from the
        provided dictionary representation.
        """
        data = {
            "id": "bef73aec-64d9-442c-9fee-09f3fdfdc7e6",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-02T12:00:00.000000",
            "some_attr": "some_value"
        }

        base_model = BaseModel(**data)

        self.assertEqual(base_model.id, data["id"])
        self.assertEqual(base_model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(base_model.updated_at, datetime(2023, 1, 2, 12, 0, 0))
        self.assertEqual(base_model.some_attr, "some_value")

    def test_init_with_empty_kwargs(self):
        """Tests if attributes are properly generated."""
        self.assertIsInstance(UUID(self.base_model.id), UUID)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_created_at_equals_updated_at_initially(self):
        """
        Test if 'created_at' and 'updated_at' attributes
        are equal upon instantiation.
        """
        self.assertEqual(self.base_model.created_at,
                         self.base_model.updated_at)

    @patch('models.base_model.datetime')
    def test_save_updates_updated_at(self, mock_datetime):
        """Test if 'save' method updates the 'updated_at' attribute."""
        test_time = datetime(2023, 8, 8, 12, 0, 0)
        mock_datetime.now.return_value = test_time

        self.base_model.save()

        self.assertEqual(self.base_model.updated_at, test_time)

    def test_to_dict(self):
        """Test if 'to_dict' method returns a dictionary containing
        the '__class__' key
        the 'created_at' key
        the 'updated_at' key
        """
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_str_representation(self):
        """Test the string representation of the BaseModel instance."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)
