from car import Car

def display_car_status(car):
    print(f"Car: {car.year} {car.make} {car.model} ({car.color})")
    print(f"Current Speed: {car.currentSpeed} km/h")
    print(f"Fuel Level: {car.fuelLevel}%\n")

car1 = Car(make="Toyota", model="Camry", year=2022, color="Blue", currentSpeed=50, maxSpeed=180, fuelLevel=80)
car2 = Car(make="Honda", model="Civic", year=2021, color="Red", currentSpeed=40, maxSpeed=160, fuelLevel=30)

print("Initial Car Status:")
display_car_status(car1)
display_car_status(car2)

print("Manipulating Cars...\n")

car1.accelerate(20)
car2.accelerate(10)

car1.brake(10)
car2.brake(5)

car1.refuel(15)
car2.refuel(20)

print("Updated Car Status:")
display_car_status(car1)
display_car_status(car2)

print("Testing Further Adjustments...\n")

car2.fuelLevel = 0
car2.accelerate(20)

car1.brake(200)

car1.refuel(50)
car2.refuel(40)

print("Final Car Status:")
display_car_status(car1)
display_car_status(car2)
