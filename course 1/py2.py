class Meeting:
    def __init__(self, day, hour, minute, duration, memb_count, *names):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.memb_count = memb_count
        self.names = names

    def found(self, day, name):
        for i in self.names:
            for n in i:
                if name == n:
                    return day and self.day
        return False

    def timestamp(self):
        return (self.day * 24 + self.hour) * 60 + self.minute

    def __eq__(self, other):
        self_time = self.timestamp()
        other_time = other.timestamp()
        if self_time == other_time:
            return True
        return self_time < other_time < self_time + self.duration \
               or self_time < other_time + other.duration < self_time + self.duration

    def __str__(self):
        names = ''
        minute = str(self.minute)
        if 0 <= self.minute <= 9:
            minute = f'0{self.minute}'
        for i in self.names:
            for name in i:
                names = f'{names} {name}'
        return f'{self.hour}:{minute} {self.duration} {names}'


rec_count = int(input())
meets = []
for i in range(rec_count):
    tmp = input().split(' ')
    if tmp[0] == 'APPOINT':
        fail = False
        day = int(tmp[1])
        hour, mins = tmp[2].split(':')
        dur = int(tmp[3])
        mems = int(tmp[4])
        new_meet = Meeting(day, int(hour), int(mins), dur, mems, tmp[5:])
        for meet in meets:
            if meet == new_meet:
                fail = True
                print('FAIL')
                break
        if not fail:
            meets.append(new_meet)
            print('OK')

    elif tmp[0] == 'PRINT':
        day = int(tmp[1])
        name = tmp[2]
        for meet in meets:
            if meet.found(day, name):
                print(str(meet))
                break
