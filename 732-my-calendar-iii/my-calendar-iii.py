from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        # Keeps track of delta changes at specific timestamps sorted dynamically
        self.timeline = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        # Mark the start of a booking
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        # Mark the end of a booking
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1
        
        max_k = 0
        ongoing_bookings = 0
        
        # Sweep across the chronological timeline
        for delta in self.timeline.values():
            ongoing_bookings += delta
            if ongoing_bookings > max_k:
                max_k = ongoing_bookings
                
        return max_k
