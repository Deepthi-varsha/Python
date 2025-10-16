class Car:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year

    def start(self):
        print(f"{self.make} {self.model} started.")

    def stop(self):
        print(f"{self.make} {self.model} stopped.")


car = Car("Honda", "Civic", 2021)
car.start()
car.stop()
