
from abc import ABC, abstractmethod

class Employee(ABC):
    
    # abstract method for subclasses to inherit
    @abstractmethod
    def earnings(self):
        raise NotImplementedError("This should be used by classes that inherit from this one only.")

    
    def __init__(self, first_name, last_name, ssn):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn 


    # read-only properties for first name, last name, ssn.
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name  
    @property
    def ssn(self):
        return self._ssn
    
    # return a string representation of the Employee object
    def __repr__(self):
        return (f"{self.first_name} {self.last_name}\nSSN: {self.ssn}\n")
        