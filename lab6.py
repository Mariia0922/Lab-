class Sweet:
    def __init__(self, name, weight, sugar, chocolate):
        self.name = name
        self.weight = weight
        self.sugar = sugar
        self.chocolate = chocolate


class Candy(Sweet):
    pass


class Chocolate(Sweet):
    pass


class Cookie(Sweet):
    pass


try:
    sweets = [
        Candy("Барбарис", 20, 15, 0),
        Candy("Іриска", 25, 18, 5),
        Chocolate("Молочний шоколад", 90, 45, 60),
        Chocolate("Чорний шоколад", 80, 25, 85),
        Cookie("Печиво", 50, 20, 10)
    ]

    total_weight = 0

    for sweet in sweets:
        total_weight += sweet.weight

    print("Загальна вага подарунка:", total_weight, "г")

    sweets.sort(key=lambda sweet: sweet.sugar)

    print("\nСолодощі після сортування:")

    for sweet in sweets:
        print(sweet.name, sweet.sugar)

    print("\nПошук за вмістом шоколаду:")

    for sweet in sweets:
        if 10 <= sweet.chocolate <= 70:
            print(sweet.name, sweet.chocolate)

except Exception as e:
    print("Помилка:", e)
