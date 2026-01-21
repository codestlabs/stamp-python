import datetime
class Fetch:
    millennia = None
    century = None
    @staticmethod
    def update(dt_obj):
        """Updates the class attributes with values from the given datetime object."""
        year = dt_obj.year
        Fetch.millennia = year // 1000
        Fetch.century = (year - 1) // 100 + 1
        two_digit_year = year % 100
        Fetch.sub_year_tens = two_digit_year // 10
        Fetch.sub_year_ones = two_digit_year % 10
        Fetch.month = f"{dt_obj.month:02d}"
        Fetch.day = f"{dt_obj.day:02d}"
        Fetch.hour = dt_obj.strftime("%I")
        Fetch.minute = f"{dt_obj.minute:02d}"
        Fetch.second = f"{dt_obj.second:02d}"
        Fetch.am_pm = dt_obj.strftime("%p")
