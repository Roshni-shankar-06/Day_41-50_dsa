class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_days(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month]) + day

        arrive_a = to_days(arriveAlice)
        leave_a = to_days(leaveAlice)
        arrive_b = to_days(arriveBob)
        leave_b = to_days(leaveBob)

        start = max(arrive_a, arrive_b)
        end = min(leave_a, leave_b)

        return max(0, end - start + 1)
