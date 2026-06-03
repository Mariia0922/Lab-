class Sweet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Candy(Sweet):
    pass


class Chocolate(Sweet):
    pass


class Cookie(Sweet):
    pass


class Node:
    def __init__(self, sweet):
        self.sweet = sweet
        self.next = None
        self.prev = None


class SweetCollection:
    def __init__(self):
        self.head = None

    def add(self, sweet):
        new_node = Node(sweet)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def remove(self, name):
        current = self.head

        while current is not None:
            if current.sweet.name == name:

                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev

                return

            current = current.next

    def print_collection(self):
        current = self.head

        while current is not None:
            print(
                current.sweet.name,
                current.sweet.weight
            )
            current = current.next


try:
    collection = SweetCollection()

    collection.add(Candy("Барбарис", 20))
    collection.add(Chocolate("Молочний шоколад", 90))
    collection.add(Cookie("Печиво", 50))

    print("Початкова колекція:")
    collection.print_collection()

    collection.remove("Барбарис")

    print("\nПісля видалення:")
    collection.print_collection()

except Exception as e:
    print("Помилка:", e)
