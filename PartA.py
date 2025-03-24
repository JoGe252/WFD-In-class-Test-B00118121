# Parent class
# Class representing a general pet
class Pet:
    def __init__(self, name, age, sex, petID, owner_name):
        # Initializes the pet attributes
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID  # A unique identifier for the pet
        self.owner_name = owner_name  # Name of the pet's owner

    def display_info(self):
        # Displays the pet's details
        print(f"Name: {self.name}, Age: {self.age}, Sex: {self.sex}, PetID: {self.petID}, Owner: {self.owner_name}")

    def update_name(self, new_name):
        # Updates the pet's name if the new name is a string
        if isinstance(new_name, str):
            self.name = new_name
    
    def update_age(self, new_age):
        # Updates the pet's age if the new age is an integer
        if isinstance(new_age, int):
            self.age = new_age

# Child class inheriting from Pet, specifically for dogs
class Dog(Pet):
    def __init__(self, name, age, sex, petID, owner_name, breed):
        # Calls the parent class constructor and initializes additional breed attribute
        super().__init__(name, age, sex, petID, owner_name)
        self.breed = breed

    def display_info(self):
        # Displays pet details along with breed information
        super().display_info()
        print(f"Breed: {self.breed}")
