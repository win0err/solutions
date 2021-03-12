class PearsBasket:
    def __init__(self, count=0):
        self.count = count

    def __add__(self, other):
        return PearsBasket(self.count + other.count)

    def __sub__(self, n):
        self.count = self.count - n if self.count > n else 0

    def __mod__(self, n) -> int:
        return self.count % n

    def __floordiv__(self, n) -> list:
        pears_per_basket = self.count // n
        excess = self.count % n
        
        baskets = [PearsBasket(pears_per_basket) for _ in range(pears_per_basket)]
        
        if excess > 0:
            baskets.append(PearsBasket(excess))

        return baskets

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.count})"

    def __str__(self) -> str:
        return str(self.count)
