class AbstractCat:
    def __init__(self):
        self._weight = 0
        self._rest_of_food = 0

    def eat(self, food):
        food += self._rest_of_food
        self._rest_of_food = 0

        self._weight += food // 10
        if self._weight > 100:
            self._weight = 100

        self._rest_of_food = food % 10

    def __str__(self):
        return f"{self.__class__.__name__} ({self._weight})"


class Kitten(AbstractCat):
    def __init__(self, weight=0):
        super().__init__()
        self._weight = weight

    def meow(self):
        return "meow..."

    def sleep(self):
        return "Snore" * (self._weight // 5)


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self._name = name

    def meow(self):
        return "MEOW..."

    def get_name(self):
        return self._name

    def catch_mice(self):
        return "Got it!"
