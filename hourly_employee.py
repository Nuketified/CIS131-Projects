from class_employee import Employee

class Employee_hourly(Employee):

    def __init__(self, first_name, last_name, ssn, hours, wages):
        super().__init__(first_name, last_name, ssn)
        self._hours = hours
        self._wages = wages

    def earnings(self):
        if self._hours <= 40:
            earnings = self._wages * self._hours
        if self._hours > 40:
                       # regular wages      OT wages
            earnings = (self._wages * 40) + ((self._hours - 40) * self._wages * 1.5)
        
        return earnings
   
    @property
    def hour(self):
        return self._hours

    @property
    def wage(self):
        return self._wages   
    
    @hour.setter
    def hour(self, hours):
        if not 0 <= hours <= 168:
            raise ValueError("Hours must be between 0 and 168.")
        self._hours = hours
    
    @wage.setter
    def wage(self, wages):
        if wages < 0:
            raise ValueError("Wage cannot be negative.")
        self._wages = wages

    def __repr__(self):
        return (f"Hourly Employee: {super().__repr__()}Hours: {self._hours}\nHourly wage: ${self._wages:.2f}\nPay this week: ${self.earnings():.2f} ")
