class Boat:
    def __init__(self, name, length, speed, crew, year):
        self.name = name
        self.length = length
        self.speed = speed
        self.crew = crew
        self.year = year


boats = [
    Boat("Atlantic", 25, 30, 8, 2018),
    Boat("Sea Star", 18, 25, 5, 2020),
    Boat("Ocean Wind", 25, 22, 6, 2016),
    Boat("Neptune", 30, 35, 10, 2021),
    Boat("Wave Rider", 18, 28, 4, 2019)
]

try:
    boats.sort(key=lambda boat: (boat.length, -boat.speed))

    print("Відсортований масив:\n")

    for boat in boats:
        print(
            boat.name,
            boat.length,
            boat.speed,
            boat.crew,
            boat.year
        )

    search_name = "Neptune"

    for boat in boats:
        if boat.name == search_name:
            print("\nЗнайдений об'єкт:")
            print(
                boat.name,
                boat.length,
                boat.speed,
                boat.crew,
                boat.year
            )
            break

except Exception as e:
    print("Помилка:", e)
