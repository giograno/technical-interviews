from collections import defaultdict


class MyCalendarTwo:

    def __init__(self):
        self.availability = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        for hour in range(start, end):
            if self.availability[hour] >= 2:
                return False
        self.complete_booking(start, end)
        return True

    def complete_booking(self, start, end):
        for hour in range(start, end):
            self.availability[hour] += 1


if __name__ == '__main__':
    calendar = MyCalendarTwo()
    calendar.book(10, 20)
    calendar.book(50, 60)
    calendar.book(10, 40)
    calendar.book(5, 15)
    calendar.book(5, 10)
    calendar.book(25, 55)