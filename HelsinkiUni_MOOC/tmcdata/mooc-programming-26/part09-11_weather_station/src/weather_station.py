# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str):
        self.name = name
        self.observations = []
    
    def add_observation(self, observation: str):
        self.observations.append(observation)

    def latest_observation(self):
        if self.observations:
            return self.observations[-1]
        return ''
    
    def number_of_observations(self):
        if self.observations:
            return len(self.observations)
        return 0
    
    def __str__(self):
        return f'{self.name}, {self.number_of_observations()} observations'
    

if __name__ == '__main__':
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)


