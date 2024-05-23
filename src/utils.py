class Booking:
    """Represents a single booking made by a teacher for a study room."""

    AVAILABLE_PERIODS = {
        "Period 1",
        "Period 2",
        "Period 3",
        "Period 4",
        "Period 5",
        "Period 6",
        "Period 7",
        "Period 8",
        "Lunch"
    }

    def __init__(self, periods_free: list):
        self.periods_free = periods_free
        self.periods_unavailable = list(self.AVAILABLE_PERIODS.difference(periods_free))
        self._period_summary = [
            (period, idx < len(periods_free))
            for idx, period in enumerate(periods_free + self.periods_unavailable)
        ]
        self.windowed_period_summary = [self._period_summary[i:i+3] for i in range(0, 9, 3)]
        self.availability = int(
            (len(self.AVAILABLE_PERIODS) - len(self.periods_free)) / len(self.AVAILABLE_PERIODS) * 100
        )

    @classmethod
    def timings_for_period(cls) -> dict[str, tuple[str, str]]:
        return {
            "Period 1": ("7:45 AM", "8:35 AM"),
            "Period 2": ("8:40 AM", "9:25 AM"),
            "Period 3": ("9:30 AM", "10:15 AM"),
            "Period 4": ("10:20 AM", "11:05 AM"),
            "Lunch": ("11:05 AM", "12:00 PM"),
            "Period 5": ("12:05 PM", "12:50 PM"),
            "Period 6": ("12:55 PM", "1:40 PM"),
            "Period 7": ("1:45 PM", "2:30 PM"),
            "Period 8": ("2:37 PM", "3:25 PM")
        }


class Room:
    """Represents a room's booking for a certain day, with an assigned ID."""

    def __init__(self, booking_list: Booking, id: int):
        self.bookings = booking_list
        self.id_ = id