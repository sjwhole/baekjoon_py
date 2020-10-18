def little(start, end, planets):
    case = 0
    for planet in planets:
        start_distance = ((int(start[0]) - int(planet[0])) ** 2 + (int(start[1]) - int(planet[1])) ** 2) ** 0.5
        end_distance = ((int(end[0]) - int(planet[0])) ** 2 + (int(end[1]) - int(planet[1])) ** 2) ** 0.5
        if start_distance < int(planet[2]):
            case += 1
        if end_distance < int(planet[2]):
            case += 1
        if start_distance < int(planet[2]) and end_distance < int(planet[2]):
            case -= 2
    return case

tries = int(input())
for i in range(tries):
    start_end = input().split()
    start_point = [start_end[0], start_end[1]]
    end_point = [start_end[2], start_end[3]]
    numbers_of_planet = int(input())
    planet_list = []
    for j in range(numbers_of_planet):
        info = input().split()
        planet_list.append(info)
    print(little(start_point, end_point, planet_list))