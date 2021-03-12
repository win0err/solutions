class Robot:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    def __init__(self, start=(0, 0)):
        if not self._is_valid_coordinates(*start):
            raise ValueError("coordinates are out of allowed range")
        self._path = [start]

    @property
    def position(self):
        return self._path[-1]

    def _is_valid_coordinates(self, x, y):
        return self.MIN_COORDINATE <= x <= self.MAX_COORDINATE \
               and self.MIN_COORDINATE <= y <= self.MAX_COORDINATE

    def move(self, path):
        for direction in path.upper():
            (x, y) = self.position

            if direction == 'N' and y != self.MAX_COORDINATE:
                y += 1
            elif direction == 'S' and y != self.MIN_COORDINATE:
                y -= 1
            elif direction == 'E' and x != self.MAX_COORDINATE:
                x += 1
            elif direction == 'W' and x != self.MIN_COORDINATE:
                x -= 1

            if self.position != (x, y):
                self._path.append((x, y))

        return self.position

    def path(self):
        return self._path.copy()
