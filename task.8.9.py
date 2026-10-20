# Chapter 8 & 9 - Animal Task

class Animal:
    def __init__(self, name, species, age, habitat):
        self.name = name
        self.species = species
        self.age = age
        self.habitat = habitat

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")

    def show_info(self):
        print("Name:", self.name)
        print("Species:", self.species)
        print("Age:", self.age)
        print("Habitat:", self.habitat)


class Cheetah(Animal):
    def __init__(self, name, age, habitat, speed):
        super().__init__(name, "Cheetah", age, habitat)
        self.speed = speed

    def run(self):
        print(self.name, "is running at", self.speed, "km/h.")

    def make_sound(self):
        print(self.name, "makes a chirping sound.")


def introduce_animal(animal):
    print("\n--- Animal Information ---")
    animal.show_info()


def animal_actions(animal):
    animal.eat()
    animal.sleep()
    animal.run()
    animal.make_sound()


# Creating a Cheetah object
cheetah = Cheetah("Flash", 4, "Grasslands", 100)
cheetah2 = Cheetah("Spot", 3, "Savannah", 95)
# Calling functions
introduce_animal(cheetah)
animal_actions(cheetah)
introduce_animal(cheetah2)
animal_actions(cheetah2)