from Celestial_object  import CelestialObject

class Asteroid(CelestialObject):

    def __init__(self, image_path, distance, orbit_speed, mass):
        super().__init__(image_path=image_path, distance=distance, orbit_speed=orbit_speed, mass=mass)
