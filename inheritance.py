class Vehicle:
	def __init__(self, name):
		self.name=name
	def speed(self):
		print(f" {self.name} ... speed is 70km/h")

class Car(Vehicle):
	def __init__(self, name, model):
		super().__init__(name)
		self.model=model
	def speed(self):
		print(f"{self.name} ...model=>{self.model}... speed is 80km/h")

class Bike(Vehicle):
	def __init__(self, name):
		super().__init__(name)

	def speed(self):
		print(f"{self.name} ... speed is 60km/h")

car_name=input("Enter the name of the car=")
car_model=input("Enter the name of the car=")
bike_name=input("Enter the name of the bike=")
car=Car(car_name,car_model)
bike=Bike(bike_name)
car.speed()
bike.speed()
