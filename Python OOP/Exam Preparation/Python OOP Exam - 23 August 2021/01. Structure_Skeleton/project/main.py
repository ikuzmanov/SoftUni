from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Gosho"))
print(space_station.add_astronaut("Geodesist", "Pesho"))
print(space_station.add_astronaut("Meteorologist", "Ivan"))
print(space_station.add_astronaut("Biologist", "Gosho"))
print(space_station.add_astronaut("Geodesist", "Svetlin"))
print(space_station.add_astronaut("Meteorologist", "Tanya"))
print(space_station.add_astronaut("Geodesist", "Ivaylo"))
print(space_station.add_planet("Saturn",
                               "sad, adas, das, dasa, hfg, jgh, uyt, try, dsadsa"))
print(space_station.retire_astronaut("Gosho"))
print(space_station.recharge_oxygen())
print(space_station.add_planet("Uran",
                               "sad, adas, das, dasa, hfg, as, asd, sda, dsa, dsa, sda, sad, sda"))
print(space_station.add_astronaut("Biologist", "Jorj"))
print(space_station.add_astronaut("Biologist", "Jorj"))
print(space_station.add_planet("Saturn", "32, 52 , 543"))
print(space_station.send_on_mission("Saturn"))
print(space_station.send_on_mission("Uran"))
print(space_station.report())