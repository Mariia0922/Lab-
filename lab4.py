class Boat:
    def __init__(self, name, length, speed, crew, year):
        self.name = name
        self.length = length
        self.speed = speed
        self.crew = crew
        self.year = year

class BoatManager:
    def execute(self):
        try:
            boats = [
                Boat("Atlantic", 25, 30, 8, 2018),
                Boat("Sea Star", 18, 25, 5, 2020),
                Boat("Ocean Wind", 25, 22, 6, 2016),
                Boat("Neptune", 30, 35, 10, 2021),
                Boat("Wave Rider", 18, 28, 4, 2019)
            ]

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

            search_boat = Boat("Neptune", 30, 35, 10, 2021)
            found = False

            for boat in boats:
                if (
                    boat.name == search_boat.name and
                    boat.length == search_boat.length and
                    boat.speed == search_boat.speed and
                    boat.crew == search_boat.crew and
                    boat.year == search_boat.year
                ):
                    print("\nЗнайдений об'єкт:")
                    print(
                        boat.name,
                        boat.length,
                        boat.speed,
                        boat.crew,
                        boat.year
                    )
                    found = True
                    break

            if not found:
                print("\nОб'єкт не знайдено")

        except Exception as e:
            print("Помилка:", e)


if __name__ == "__main__":
    manager = BoatManager()
    manager.execute()
