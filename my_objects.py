class ISS:
    def __init__(self, risetime, duration, city):
        self.risetime = risetime
        self.duration = duration
        self.city = city

    def __str__(self):
        return "today at {} for about {} minute(s)\n".format(self.risetime, self.duration)