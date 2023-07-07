import random

class Trailer:
    def __init__(self, id):
        self.id = id
        self.latitude = 0.0
        self.longitude = 0.0

    def update_position(self):
        # Simulate updating the trailer's position
        self.latitude += random.uniform(-0.1, 0.1)
        self.longitude += random.uniform(-0.1, 0.1)

    def get_position(self):
        return self.latitude, self.longitude


# Create trailer instances
trailers = [Trailer(1), Trailer(2), Trailer(3)]

# Simulate tracking the trailers
for _ in range(5):
    for trailer in trailers:
        trailer.update_position()
        position = trailer.get_position()
        print(f"Trailer {trailer.id}: Latitude={position[0]}, Longitude={position[1]}")

