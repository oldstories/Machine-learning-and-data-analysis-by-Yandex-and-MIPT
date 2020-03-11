class Meeting:
    def __init__(self, day, hour, minute, duration, memb_count, names*):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.member = member
        self.memb_count = memb_count
        self.names = names

    def __eq__(self, other):
        self_time = self.hour * 60 + self.minute
        other_time = other.hour * 60 + other.minute
        return self_time + self.duration > other_time

rec_count = int(input())
for i in range(rec_count):
    tmp = input().split(' ')
    
