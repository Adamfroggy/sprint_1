'''
This tests the vehicle.py file for errors
'''

import unittest
from vehicle import Vehicle, Convertible


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle('Toyota', 'Camry', 'gray', 2015, 60000)

    def test_honk(self):
        self.assertEqual(self.vehicle.honk(), "HOOOOOOONK!")

    def test_drive(self):
        self.assertEqual(self.vehicle.drive(1234), 61234)

    def test_repr(self):
        expected_repr = "A gray 2015 Toyota Camry with 60000 miles."
        self.assertEqual(repr(self.vehicle), expected_repr)


class TestConvertible(unittest.TestCase):

    def setUp(self):
        self.convertible = Convertible('Toyota', 'Camry', 'gray', 2015, 60000)

    def test_change_top_status(self):
        self.assertEqual(self.convertible.top_down, True)
        self.assertEqual(self.convertible.change_top_status(), "Top is now up!"
                         )
        self.assertEqual(self.convertible.top_down, False)
        self.assertEqual(
            self.convertible.change_top_status(), "Top is now down!")
        self.assertEqual(self.convertible.top_down, True)

    def test_repr(self):
        expected_repr = "A gray 2015 Toyota Camry"
        "convertible with 60000 miles."
        self.assertEqual(repr(self.convertible), expected_repr)


if __name__ == '__main__':
    unittest.main()
