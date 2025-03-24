import unittest
from PartA import Pet, Dog

# Test cases for the pet class
class TestPet(unittest.TestCase):
    def setUp(self):
        # Sets up a pet instance for testing
        self.pet = Pet("Rollo", 3, "Male", "P1234", "Joel George")

    def test_instance(self):
        # Tests if self.pet is an instance of Pet class
        self.assertIsInstance(self.pet, Pet)

    def test_not_instance(self):
        # Tests if self.pet is NOT an instance of Dog class
        self.assertNotIsInstance(self.pet, Dog)

    def test_update_name(self):
        # Tests if the pet's name is updated correctly
        self.pet.update_name("Max")
        self.assertEqual(self.pet.name, "Max")

# To run the unit tests
if __name__ == "__main__":
    unittest.main()