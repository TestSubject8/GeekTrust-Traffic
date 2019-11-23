class Orbit:
    weatherEffect = {
        "Sunny": 0.9,
        "Rainy": 1.2,
        "Windy": 1
    }

    def __init__(self,s,c,d):
        self.crater_count = c
        self.traffic_speed = s
        self.distance = d

    def get_craters(self,weather):
        return self.crater_count * self.weatherEffect[weather]
