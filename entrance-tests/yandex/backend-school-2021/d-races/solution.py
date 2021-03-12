import enum


class TransportType(enum.Enum):
    Car = 1
    Motocycle = 2
    Cartage = 3


class AbstractTransport:
    def __init__(self, number, speed):
        self.number = number
        self.speed = speed

    @property
    def actual_speed(self):
        return self.speed


class Cartage(AbstractTransport):
    def __init__(self, number, speed):
        super().__init__(number, speed)
    
    @property
    def actual_speed(self):
        return self.speed


class Car(AbstractTransport):
    def __init__(self, number, speed, fuel):
        super().__init__(number, speed)
        self.fuel = fuel

    @property
    def actual_speed(self):
        affect = 1

        if self.fuel == 95:
            affect = 0.9
        elif self.fuel == 92:
            affect = 0.8

        return int(self.speed * affect)


class Motocycle(AbstractTransport):
    def __init__(self, number, speed, fuel):
        super().__init__(number, speed)
        self.fuel = fuel
    
    @property
    def actual_speed(self):
        affect = 1

        if self.fuel == 95:
            affect = 0.8
        elif self.fuel == 92:
            affect = 0.6

        return int(self.speed * affect)


class Race:
    def __init__(self, track_len, time):
        self.track_len = track_len
        self.time = time

        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def get_closest_to_finish(self):
        best_distance = 0
        winner = 0

        for participant in self.participants:
            distance = (participant.actual_speed * self.time) % self.track_len

            if distance > best_distance:
                best_distance = distance
                winner = participant.number
            elif distance == best_distance and participant.number < winner:
                best_distance = distance
                winner = participant.number

        return winner


if __name__ == "__main__":
    N, M, t = map(int, input().split())
    race = Race(M, t)

    for i in range(N):
        transport_info = [int(x) for x in input().split()]

        transport_type = TransportType(transport_info[1])
        if transport_type == TransportType.Car:
            race.add_participant(Car(transport_info[0], transport_info[2], transport_info[3]))
        elif transport_type == TransportType.Motocycle:
            race.add_participant(Motocycle(transport_info[0], transport_info[2], transport_info[3]))
        else:
            race.add_participant(Cartage(transport_info[0], transport_info[2]))
    
    print(race.get_closest_to_finish())
