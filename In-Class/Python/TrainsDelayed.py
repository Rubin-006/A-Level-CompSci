
class Train:

    def __init__(self,destinations,end_time):
        self.path = destinations
        self.expected_time = end_time


    def manage_delays(self,destination, delay):
        if destination in self.path:
            self. expected_time = list(map(int,self.expected_time.split(":")))
            self.expected_time[0] += (delay // 60)
            self.expected_time[1] += (delay % 60)
            self.expected_time = f"{self.expected_time[0]}:{self.expected_time[1]}"



trains = [
  Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
  Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
  Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
]

for t in trains:
    t.manage_delays("Lakeside Valley", 60)

print(f"{trains[0].expected_time}\t{trains[1].expected_time}\t{trains[2].expected_time}")