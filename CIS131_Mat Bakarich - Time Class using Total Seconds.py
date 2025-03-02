# Module 5 Lab
# Mat Bakarich 
# Feb 27, 2025

"""Class Time using _total_seconds"""

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        #hour # 0-23
        #minute # 0-59
        #second # 0-59
        self._total_seconds = (hour * 3600) + (minute * 60) + second

    @property
    def hour(self):
        """Return the hour."""
        return self._total_seconds//3600 

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._total_seconds = (hour * 3600) + (self._total_seconds % 3600)

    @property
    def minute(self):
        """Return the minute."""
        return (self._total_seconds % 3600) // 60

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._total_seconds =((self._total_seconds // 3600) * 3600) + (minute * 60) + (self._total_seconds % 60)
    
    @property
    def second(self):
        """Return the second."""
        return self._total_seconds % 60

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds = (self._total_seconds // 60) * 60 + second

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self._total_seconds = (hour * 3600) + (minute * 60) + second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
                f'second={self.second})')

    def __str__(self):
        """Print Time in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))
    

  