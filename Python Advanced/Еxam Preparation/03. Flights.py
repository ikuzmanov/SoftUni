def flights(*args):
    flights_db = {}
    for element in args:
        if element == "Finish":
            break
        elif type(element) == str and element not in flights_db:
            flights_db[element] = 0
        elif type(element) == int:
            flights_db[args[args.index(element) - 1]] += element
    return flights_db


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
