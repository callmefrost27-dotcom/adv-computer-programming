from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric = ElectricCar("Tesla", "Model 3", "2CD567", 75)
bike = Motorbike("Honda", "CBR", "3EF890", 500)

# Create a renter
renter = Renter("John", 12345)

# Print vehicles
print(car)
print(electric)
print(bike)

# Rent the car
car.rent()
print("After renting:")
print(car)

# Return the car
car.return_vehicle()
print("After returning:")
print(car)

# Test invalid renter name
try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("Error:", e)

# Test invalid license number
try:
    bad_renter = Renter("John", 0)
except ValueError as e:
    print("Error:", e)

# Test polymorphism
vehicles = [car, electric, bike]

print("All vehicles:")
for vehicle in vehicles:
    print(vehicle)
