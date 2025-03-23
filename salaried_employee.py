from class_employee import Employee  


class Employee_salaried(Employee):
    
    
    def __init__(self, first_name, last_name, ssn, weekly_salary):
        super().__init__(first_name, last_name, ssn)
        self._weekly_salary = weekly_salary
   
    
    def earnings(self):
        return self._weekly_salary
    
    
    
    
    @property
    def weekly_salary(self):
        return self._weekly_salary
    
    @weekly_salary.setter
    def weekly_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._weekly_salary = value
    
    

    
    def __repr__(self):
        return (f"Salaried Employee: {super().__repr__()}Weekly Salary = ${self._weekly_salary}")

        

