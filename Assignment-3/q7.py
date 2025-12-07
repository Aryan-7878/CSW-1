import random

# Define the generator function
def sensor_data_stream():
    while True:  # infinite generator to simulate continuous data
        temperature = round(random.uniform(20.0, 30.0), 2)  # generate a random temperature
        yield temperature  # send it out to whoever is reading it
        
        

# Demonstrate using the generator to get first 10 readings
stream = sensor_data_stream()  # create the generator object

print("Sensor Data Stream (First 10 Readings):")
for i in range(10):
    reading = next(stream)  # get the next temperature value
    print(f"Reading {i+1}: {reading}°C")