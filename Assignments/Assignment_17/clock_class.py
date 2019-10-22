class Clock():
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def str_update(self, time_str):
        new_hours, new_minutes, new_seconds = time_str.split(":")
        self.hours = int(new_hours)
        self.minutes = int(new_minutes)
        self.seconds = int(new_seconds)

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)

    def add_clocks(self, another_clock):
        divmod_secs = divmod((self.seconds + another_clock.seconds), 60)
        divmod_mins = divmod((self.minutes + another_clock.minutes + divmod_secs[0]), 60)
        divmod_hours = divmod((self.hours + another_clock.hours + divmod_mins[0]), 24)
        return Clock(divmod_hours[1], divmod_mins[1], divmod_secs[1])

    
clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)

print("----test2-----")
clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)