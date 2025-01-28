class Car:
    def __init__(self, make, model, year, color, currentSpeed=0, maxSpeed=180, fuelLevel=50):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self, increment):
        if self.fuelLevel > 0:
            self.currentSpeed += increment
            self.fuelLevel -= increment
            if self.currentSpeed > self.maxSpeed:
                self.currentSpeed = self.maxSpeed
            if self.fuelLevel < 0:
                self.fuelLevel = 0
        else:
            self.currentSpeed = 0

    def brake(self, decrement):
        self.currentSpeed -= decrement
        if self.currentSpeed < 0:
            self.currentSpeed = 0

    def refuel(self, amount):
        self.fuelLevel += amount
        if self.fuelLevel > 100:
            self.fuelLevel = 100
