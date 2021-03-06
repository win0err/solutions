class Robot:
    def __init__(self, start = (0, 0)):
        self._path = [start]
    
    @property
    def position(self):
        return self._path[-1]

    def move(self, path):
        for direction in path.upper():
            (x, y) = self.position

            if direction == 'N' and y != 100:
                y += 1
            elif direction == 'S' and y != 0:
                y -= 1
            elif direction == 'E' and x != 100:
                x += 1
            elif direction == 'W' and x != 0:
                x -= 1

            if self.position != (x, y):
                self._path.append((x, y))

        return self.position

    def path(self):
        return self._path