"""script: project1Employees.py
   action: a. define class Person
           b. define class Employee
           c. define Class Student
           d. define get employees()
           e. define create_menu()
           f. define display_employee_employment_information()
           g. define display_employee_contact_info()
           h. define get_Students()
           i. define display_student_contact_information()
           j. define display_all_person_contact_information()
           k. define get_student_scores()
           l. define display_student_Scores()
           m, call get_employees()
           n. call get_students()
           o. call get_student_scores()
           p. call create_menu()
   author: Mat Bakarich
   date:   05/04/2025 
"""
###########################################################################################################
#    class_person.py
###########################################################################################################
"""
    script: class_person.py
    author: Mat Bakarich
"""

# import abc
from abc import ABC


# class definition
class Person(ABC):
    """
    A class representing a person.

    attributes:
        last_name (str): Last Name
        first_name (str): First Name
        id (4-digit intger): ID Number
        email_address (str): e-mail address
        phone_number (12-character str): Phone Number
    
    methods:
        first_name(): set the first name
        last_name(): set the last name
        email_address(): set the e-mail address
        phone_number(): set the phone number
        *note* the ID number cannot be changed
    
    """

    def __init__(self, last_name, first_name, id, email_address, phone_number):
        """
        Initializes an person object.

        arguments: 
            last_name (str): Last Name
            first_name (str): First Name
            id (4-digit intger): ID Number
            email_address (str): e-mail address
            phone_number (12-character str): Phone Number
        """
        # call ABC's init method
        super().__init__()
        
        # intialize last name
        self._last_name = last_name
        
        # initialize firt name
        self._first_name = first_name
        
        # convert id to integer
        id = int(id)
        # validate the number is 4-digits
        if not 1000 <= id <= 9999:
        # raise ValueError if ID out of range.
            raise ValueError("ID Number must be a 4-digit integer")
        # intialize id
        self._id = id
        
        # initialize e-mail address
        self._email_address = email_address

        # intialize phone number
        self._phone_number = phone_number

    
    
    def __repr__(self):
        """
            Returns a string representation of the Person object.

            action: returns a string
            input: none
            output: none
            return: string represenation of Person object
        
        """
        return (f"Name: {self._first_name} {self._last_name}\nID: {self._id}\nE-mail: {self._email_address}\nPhone Number: {self._phone_number}")
    
    def __str__(self):
       """
            Returns a string representation of the Person object.

            action: returns a string
            input: none
            output: none
            return: string represenation of Person object
        
        """
       return (f"Name: {self._first_name} {self._last_name}\nID: {self._id}\nE-mail: {self._email_address}\nPhone Number: {self._phone_number}")
    
    # first name getter and setter
    @property
    def first_name(self):
        """return the first name"""
        return self._first_name
    
    @first_name.setter
    def first_name(self,first_name):
        """Set first name."""
        self._first_name = first_name


    # last name getter and setter
    @property
    def last_name(self):
        """return the last name"""
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        """Set last name."""
        self._last_name = last_name
    

    # id getter
    @property
    def id(self):
        """return id number."""
        return self._id
     

    # e-mail getter and setter
    @property
    def email_address(self):
        """return the e-mail address."""
        return self._email_address
    
    @email_address.setter
    def email_address(self, email_address):
        """Set the e-mail address."""
        self._email_address = email_address
    


    # phone number getter and setter
    @property
    def phone_number(self):
        """return the phone number."""
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        """Set the phone number."""
        if len(phone_number) != 12:
            raise ValueError("Phone number must be 12 characters including spaces.")
        else:
            self._phone_number = phone_number


###################################################################################################################
## Class Student
###################################################################################################################


class Student(Person):
    """
    A class representing a person.

    attributes:
        last_name (str): Last Name
        first_name (str): First Name
        id (4-digit intger): ID Number
        email_address (str): e-mail address
        phone_number (12-character str): Phone Number
    
    methods:
        first_name(): set the first name
        last_name(): set the last name
        email_address(): set the e-mail address
        phone_number(): set the phone number
        *note* the ID number cannot be changed
    
    """

    # class variable
    course_name_list =  ['Art', 'Latin', 'Greek', 'Mathematics', 'Science', 'Painting', 'Sculpting'] 
     
    


    # init method
    def __init__(self, last_name, first_name, id, email_address, phone_number,):
        super().__init__(last_name, first_name, id, email_address, phone_number)
    
        
       
        self._courses_student_dict =  {'Art':'0', 'Greek':'0', 'Latin':'0', 'Science':'0', 'Mathematics':'0'}

        # Has a instance variable coursesStudentDict  {courseName: Score} 
        # (CourseName must be in the CourseNameList and scores are integers greater than zero and less than 100), editable.



    # repr method
    def __repr__(self):
        """
            Returns a string representation of the Student object.

            action: returns a string
            input: none
            output: none
            return: string represenation of Student object
        
        """
        return super().__repr__()
    
    # str method
    def __str__(self):
        """
            Returns a string representation of the Student object.

            action: returns a string
            input: none
            output: none
            return: string represenation of Student object
        
        """
        return super().__str__()

    #@property
    #def course_name_list(self):
    #    """return the student course list"""
    #    return self._course_name_list
    
    #@course_name_list.setter
    #def course_name_list(self, courses):
    #    """update the course list with an iterable"""
    #    new_course_list = list(courses)
    #    self._course_name_list = new_course_list



    @property
    def courses_student_dict(self):
        """return the student courses dictionary"""
        return self._courses_student_dict
    
    @courses_student_dict.setter
    def courses_student_dict(self, course_name, score):
        """update the student courses dictionary"""
        if course_name in self.course_name_list and 0 < score < 100:
            
            self.courses_student_dict[course_name] = score


    @property
    def last_name(self):
        """return the last name"""
        return self._last_name
    
    #@last_name.setter
    #def last_name(self, last_name):
    #    """set the last name"""
    #    self._last_name = last_name


    @property
    def first_name(self):
        """return the first name"""
        return self._first_name
    
    #@first_name.setter
    #def first_name(self, first_name):
    #    """set the fist name"""
    #    self._first_name = first_name


    @property
    def id(self):
        """return the id"""
        return self._id
    


    @property
    def email_address(self):
        """return the e-mail address"""
        return self._email_address
    
    @email_address.setter
    def email_address(self, email_address):
        """set the e-mail address"""
        self._email_address = email_address

    @classmethod
    def get_student_academics(self,student):
        """return the academic string."""
        
        
        last_name = student.last_name
        first_name = student.first_name
        id = student.id
        for key, value in student.courses_student_dict.items():
            key = str(key)
            if key == 'Art':
                score_1 = value
            elif key == 'Greek':
                score_2 = value
            elif key == 'Latin':
                score_3 = value
            elif key == 'Science':
                score_4 = value
            elif key == 'Mathematics':
                score_5 = value
        
        #????
        academic_string = f"{last_name : <15}{first_name : <15}{id : <6}{score_1 : <10}{score_2 : <10}{score_3 : <10}{score_4 : <10}{score_5 : <12}"
        unformatted_academic_string = last_name, first_name, id, score_1, score_2, score_3, score_4, score_5

        # print student scores
        return unformatted_academic_string

###########################################################################################################
#    class_employee.py
###########################################################################################################
"""
    script: class_employee.py
    author: Mat Bakarich
"""

# import datetime
import datetime

# class definition
class Employee(Person):
    """
    A class representing an Employee(Person)

    attributes:
        last_name (str): Last Name
        first_name (str): First Name
        id (4-digit intger): ID Number
        email_address (str): e-mail address
        phone_number (12-character str): Phone Number
        hire_date (str): hire date date object
        classification_person (str): full-time or part-time classification
        role_pereson (str): staff or faculty role
        annual_salary (float): annual salary, must be positive float to 2 decimal places 
    
    methods:
        first_name(): set the first name
        last_name(): set the last name
        email_address(): set the e-mail address
        phone_number(): set the phone number
        *note* the ID number cannot be changed
    
    """

    # class variables
    role_dictionary = {'001': 'Staff', '002': 'Faculty'}  
    classification_dictionary =	{'001': 'Full-time', '002': 'Part-time'}  

    # init method
    def __init__(self, last_name, first_name, id, email_address, phone_number, hire_date, classification_person, role_person, annual_salary ):
        super().__init__(last_name, first_name, id, email_address, phone_number)
         
        # store hire date in a local variable
        hire_string = hire_date
        # strip backslashes from hire date and intialize date object
        try:
            hire_date = datetime.datetime.strptime(hire_string, "%m/%d/%Y").date()
        except ValueError:
            print("Hire date must be a valid string in 'MM/DD/YYYY' format.")
        # set hire date
        self._hire_date = hire_date
        
                    
        # intialize role_person        
        self._role_person = role_person

        # initalize classification_person   
        self._classification_person = classification_person 
        
        # set annual salary
        self._annual_salary = annual_salary
    
    # def repr() method
    def __repr__(self):
        classification = self._classification_person
        for key, value in Employee.classification_dictionary.items():
            if classification == key:
                classification = value
        role = self._role_person
        for key, value in Employee.role_dictionary.items():
            if role == key:
                role = value
        return (f"{super().__repr__()} \nHire date: {self._hire_date} \nRole: {role} \nClassification: {classification} \nAnnual Salary: ${self._annual_salary}")
    
    # def str() method
    def __str__(self):
        classification = self._classification_person
        for key, value in Employee.classification_dictionary.items():
            if classification == key:
                classification = value
        role = self._role_person
        for key, value in Employee.role_dictionary.items():
            if role == key:
                role = value
        return (f"{super().__str__()} \nHire date: {self._hire_date} \nRole: {role} \nClassification: {classification} \nAnnual Salary: ${self._annual_salary}")
                     
    # hite date getter
    @property
    def hire_date(self):
        """return the hire date"""
        return self._hire_date
    
    #@hire_date.setter
    # hire date may not be changed once initialized.
    
    # classification_person getter and setter
    @property
    def classification_person(self):
        """return the  employee classification"""
        return self._classification_person
    
    @classification_person.setter
    def classification_person(self,classification_person):
        """set the employee classification"""
        # adjust classification strings to match format
        classification_person = classification_person.lower()
        if classification_person == 'full':
                classification_person = 'Full-time'
        elif classification_person == 'part':
                classification_person = 'Part-time'
        else:
            raise ValueError("classification_person must be 'Full' or 'Part'.")
        
        # iterate over classification dictionary
        for key, value in Employee.classification_dictionary.items():          
            # check for classification in values
            if classification_person == value:
                # store the dictionary key in local variable 
                classification_person = key
        # set classification person
        self._classification_person = classification_person


    # role_person getter and setter
    @property
    def role_person(self):
        """return the employee role"""
        return self._role_person
    
    @role_person.setter
    def role_person(self,role_person):
        """set the employee role"""
        # check if employee role is in role_dictionary
        for key, value in Employee.role_dictionary.items():
            if role_person == value:
                # store the dictionary key in local variable 
                role_person = key 
                self._role_person = role_person
        if role_person not in Employee.role_dictionary.keys():    
                raise ValueError("Employee role not found.")
     

    # annual_salary getter and setter
    @property
    def annual_salary(self):
        """return the annual salary"""
        return self._annual_salary
    
    @annual_salary.setter
    def annual_salary(self, annual_salary):
        """validate and set the annual salary"""
        try:
            annual_salary = float(annual_salary)

        except ValueError:
            print("Annual Salary must be a float.")
        
        if annual_salary <= 0:
            raise ValueError("Annual salary can't be negative.")     
        else:
            annual_salary = f"{annual_salary:.2f}"
            self._annual_salary = annual_salary


###########################################################################################################
## Get Employees
###########################################################################################################

# intialize list
employee_list = []

def get_employees():
    """opens the employees.txt file
       reads the file line by line
       for each line, creates and Employee object and adds it to the Employee list.
    """
    
    print("Starting Application...\n")

    # open 'employees.txt'
    with open('employees.txt', mode='r') as employees:
        for line in employees:
            # Strip whitespace and split the line into parts (adjust delimiter as needed)
            data = line.split()
            classifications = ('full', 'part',)
            roles = ('staff', 'faculty')
            classification = data[6].lower()
            role_current = data[7].lower()
            
            #check for header line
            if len(data) == 9  and (data[6]).lower() in classifications and data[7].lower() in roles and not 'ID' in data:
            
                # create a class instance    
                obj = Employee(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],)
                # add employee object to employee list
                employee_list.append(obj)
                # concatenate firstname and lastname strings
                name = obj.first_name + " " + obj.last_name
                # print a line confirming the Employee was initialized
                print(f"Added employee {name}...")
            # skip the header line of the text file
            elif len(data) == 0:
               print("Skipping blank line.")
            elif 'ID' in data:
                print("Skipping header line.")
            # skip lines with incorrect numbers of attributes
            elif classification not in classifications or role_current not in roles:
                print(f"Skipping entry: {data} due to invalid role or classification.")
            else:
                print(f"Skipping line: {line.strip()} - Incorrect number of attributes")
    print("\n")


###################################################################################################################
## Get Students
###################################################################################################################

# intialize list
student_list = []

def get_students():
    """opens the students.txt file
       reads the file line by line
       for each line, creates and Employee object and adds it to the Employee list.
    """

    with open('students.txt', mode='r') as students:
        for line in students:
            # Strip whitespace and split the line into parts 
            data = line.split()
            
    
            # check for header line
            if len(data) == 5 and not 'ID' in data:
            
                # create a class instance    
                obj = Student(data[0], data[1], data[2], data[3], data[4])
                # add Student object to student list
                student_list.append(obj)
                # concatenate firstname and lastname strings
                name = obj.first_name + " " + obj.last_name
                # print a line confirming the Student was initialized
                print(f"Added student {name}...")
            # skip the header line of the text file
            elif len(data) == 0:
               print("Skipping blank line.")
            elif 'ID' in data:
                print("Skipping header line.")
            elif len(data) != 5:
                print("Skipping line, not enough entries.")
        print('\n')



###########################################################################################################
## Get Scores
###########################################################################################################

def get_student_scores():
    
    with open('scores.txt', mode='r') as scores:
        for line in scores:
            # Strip whitespace and split the line into parts 
            data = line.split()
            
           

            id = data[0]
            art = data[1]
            greek = data[2]
            latin = data[3]
            science = data[4]
            mathematics = data[5]  

            grades_dict = {'Art': art, 'Greek': greek, 'Latin': latin, 'Science': science, 'Mathematics': mathematics}        
            
            #iteralte over student_list
            for student in student_list:
                this_student = student
                student_id = str(this_student.id)
                # match to student id
                if id == student_id:
                        for key, value in grades_dict.items():
                            # check if course in course list
                            if key in Student.course_name_list:
                                # update dictionary of student courses for this student
                                this_student.courses_student_dict.update(grades_dict)
                                
                                # format string for student name first + last
                                student_name = this_student.first_name + ' ' + this_student.last_name
                                
             
                        # print a line confirming the scores were added.
                        print(f"Added scores for {student_name}.")
                           
       

###########################################################################################################
## MENU
###########################################################################################################

def create_menu():
    
    # add menu options here, use this format
    menu_options = ('1. Quit', 
                    '2. Display Employee Employment Information', 
                    '3. Display Employee Contact Information',
                    '4. Display Student Contact Information',
                    '5. Display All Person Contact Information',
                    '6. Display Full Student Academic report',
                    '7. Look Up Student Academic Record', 
                    '8. Get Honor Roll',
                    '9. Display Full Academic Report Sorted by Last Name',
                   '10. Display Full Academic Report Sorted by Student ID',
                   
                  # 'X. Enter a new menu option followed by a comma here'
                    )
    
    # sentinel variable for loop
    keep_going = 0

    while keep_going != 1:
        print("\nPlease select an option below.\n")
        for item in menu_options:
            print(item)
        



        # get user input
        while True:
            try:
                user_selection = int(input())
                if not user_selection in range(len(menu_options) + 1) or user_selection == 0 :
                    raise ValueError(f"Please choose an option between 1 and {len(menu_options)}")
                break
            except ValueError:
                print(f"Please choose an option between 1 and {len(menu_options)}.")


    
    # add new menu selection code here
        
        if user_selection == 1:
            print('\nThank you for using the system. \nNow exiting the program…')
            # terminate the menu loop using the sentinel value
            keep_going = 1
        
        if user_selection == 2:
            display_employee_employment_information() 
       
        if user_selection == 3:
            display_employee_contact_information() 
        
        if user_selection == 4:
            display_student_contact_information()
        
        if user_selection == 5:
            display_all_person_contact_information()
        
        if user_selection == 6:
            display_full_student_academic_report()

        if user_selection == 7:
            look_up_student_academic_record()

        if user_selection == 8:
            get_honor_roll()

        if user_selection == 9:
            display_full_academic_report_sorted_by_last_name()

        if user_selection == 10:
            display_full_academic_report_sorted_by_student_id()


###########################################################################################################
## employee employment info
###########################################################################################################
def display_employee_employment_information():
    """iterate over employee_list and store information in variables
       use dictionaries to convert classification and role
       display the employee employment information for each employee in formatted rows.
    """
    
    # print a header line
    print(f"\nEmployee Employment Information:\n\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'E-mail' : <33}{'Phone Number ' : <12}{'Hire Date' : <12}{'Classification' : <15}{'Role' : <12}{'Salary' : <15}")
    
    # iterate over employee list and assign atttributes to variables
    for item in employee_list:
        
        employee = item
        last_name = employee.last_name
        first_name = employee.first_name
        id = employee.id
        email = employee.email_address
        phone_number = str(employee.phone_number)
        hire_date = str(employee._hire_date)
        
        # convert stored value back to classification
        classification = employee._classification_person
        for key, value in Employee.classification_dictionary.items():
            if classification == key:
                classification = value
        # convert stored value back to role
        role = employee._role_person
        for key, value in Employee.role_dictionary.items():
            if role == key:
                role = value  
        salary = float(employee._annual_salary)
        salary = f"{salary:.2f}"
        salary = str(salary)
        
        # print the employee employment info
        print(f"{last_name : <15}{first_name : <15}{id : <6}{email : <30}   {phone_number : <12} {hire_date : <12}{classification : <15}{role : <12}${salary : <15}")
         



###########################################################################################################
## employee contact info
###########################################################################################################

def display_employee_contact_information():
    """iterate over employee_list and store information in variables
       display the employee contact information for each employee in formatted rows.
    """
    # print a header line
    print(f"\nEmployee Contact Information:\n\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Email' : <30}{'Phone' : <12}")

    # iterate over employee_list, assign attributes to variables
    for item in employee_list:
        employee = item
        last_name = employee.last_name
        first_name = employee.first_name
        id = employee.id
        email = employee.email_address
        phone_number = str(employee.phone_number)
        
        # print Employee contact info attributes
        print(f"{last_name : <15}{first_name : <15}{id : <6}{email : <30}{phone_number : <12}")



###########################################################################################################
## student contact info
###########################################################################################################

def display_student_contact_information():
    """iterate over student_list and store information in variables
       display the student contact information for each student in formatted rows.
    """
    # print a header line
    print(f"\nStudent Contact Information:\n\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Email' : <30}{'Phone' : <12}")

    # iterate over student_list, assign attributes to variables and print them
    for item in student_list:
        student = item
        last_name = student.last_name
        first_name = student.first_name
        id = student.id
        email = student.email_address
        phone_number = str(student.phone_number)
        
        # print the object attributes
        print(f"{last_name : <15}{first_name : <15}{id : <6}{email : <30}{phone_number : <12}")




###########################################################################################################
## all contact info
###########################################################################################################

def display_all_person_contact_information():
    """add student_list and employee_list to create person_list
       iterate over person_list and store information in variables
       display the person contact information for each student in formatted rows.
    """

    # print a header line
    print(f"\nAll Person Contact Information:\n\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Email' : <30}{'Phone' : <12}")
    
    # combine employee_list and student_list into one list
    person_list = employee_list + student_list 

    # iterate over list, assign employee or student object to person, assign attributes to variables
    for item in person_list:
        person = item
        last_name = person.last_name
        first_name = person.first_name
        id = person.id
        email = person.email_address
        phone_number = str(person.phone_number)
       
        # print person information
        print(f"{last_name : <15}{first_name : <15}{id : <6}{email : <30}{phone_number : <12}")
    
  
###########################################################################################################
## display student scores
###########################################################################################################

def display_student_scores():
    """iterate over student list and call get students academics method for each student and print the results"""
    # print header lines
    print("\nStudent Scores:")
    print(f"\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Art' : <10}{'Greek' : <10}{'Latin' : <10}{'Science' : <10}{'Mathematics' : <12}")
 
    
    # iterate over student_list print the string
    for item in student_list:
        # call get_student_academics method
        student_string = Student.get_student_academics(item)
        # print the string
        print(student_string)



###########################################################################################################
## display full student report
###########################################################################################################
def display_full_student_academic_report():
    # print header lines
    print("\nFull Academic Report:")
    print(f"\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Art' : <10}{'Greek' : <10}{'Latin' : <10}{'Science' : <10}{'Mathematics' : <12}{'High' : <6}{'Low' : <6}{'Average' : <8}{'Grade' : <6}")
    
    # initialize empty lists to store student grades for each class
    art_grades= []
    greek_grades = []
    latin_grades = []
    science_grades = []
    math_grades = []

    # iterate over student_list print the string
    for item in student_list:
        student = item
        
        # call get_student_academics method
        student_string = get_student_academic_report(student)
        # assign elements of student string to variables
        last_name = student_string[0]
        first_name = student_string[1]
        id = student_string[2]
        
        art = int(student_string[3])
        greek = int(student_string[4])
        latin = int(student_string[5])
        science = int(student_string[6])
        math = int(student_string[7])
        
        scores = (art, greek, latin, science, math)
        
        art_grades.append(art)
        greek_grades.append(greek)
        latin_grades.append(latin)
        science_grades.append(science)
        math_grades.append(math)
        
        high = max(scores)
        low = min(scores)
        average = sum(scores) / len(scores)
        
        if average >=90:
            grade = 'A'
        if 80 <= average < 90:
            grade = 'B'
        if 70 <= average < 80:
            grade = 'C'
        if 60 <= average < 70:
            grade = 'D'
        if 0 <= average < 60:
            grade = 'F'

        new_student_string = f"{last_name : <15}{first_name : <15}{id : <6}{art : <10}{greek : <10}{latin : <10}{science : <10}{math : <12}{high : <6}{low : <6}{average : <8}{grade : <6}"
        
        # print the string
        print(new_student_string)
    
    art_high = max(art_grades) 
    greek_high = max(greek_grades)
    latin_high = max(latin_grades)
    science_high = max(science_grades)
    math_high = max(math_grades)
    
    art_low = min(art_grades)
    greek_low = min(greek_grades)
    latin_low = min(latin_grades)
    science_low = min(science_grades)
    math_low = min(math_grades)

    art_average = sum(art_grades) / len(art_grades)
    greek_average = sum(greek_grades) / len(greek_grades)
    latin_average = sum(latin_grades) / len(latin_grades)
    science_average = sum(science_grades) / len(science_grades)
    math_average = sum(math_grades) / len(math_grades)

    print(f"\n{'High' : <36}{art_high : <10}{greek_high : <10}{latin_high : <10}{science_high : <10}{math_high : <10}")
    print(f"{'Low' : <36}{art_low : <10}{greek_low : <10}{latin_low : <10}{science_low : <10}{math_low : <10}")  
    print(f"{'Average' : <36}{art_average : <10}{greek_average : <10}{latin_average : <10}{science_average : <10}{math_average : <10}")      

#displayFullStudentAcademicReport() will 
#Print a header line to print the headings of the report
#call getStudentAcademicReport for each Student object in studentList 
#print the values returned by getStudentAcademicReport

#For each course, we will:

#Find its lowest score.
#Find its highest score.
#Find its average score.
#Display the highest scores
#Display the lowest scores
#Display the average scores
#It is left up to the student to come up with a solution for this


###########################################################################################################
## get student academic report
###########################################################################################################
def get_student_academic_report(student):
        
    
        student = student
        #print(student)
        # call get_student_academics method
        student_string = Student.get_student_academics(student)
        #print(student_string)
        last_name = student_string[0]
        first_name = student_string[1]
        id = student_string[2]
        
        art = int(student_string[3])
        greek = int(student_string[4])
        latin = int(student_string[5])
        science = int(student_string[6])
        math = int(student_string[7])
        
        scores = (art, greek, latin, science, math)
        
        
        
        high = max(scores)
        low = min(scores)
        average = sum(scores) / len(scores)
        
        if average >=90:
            grade = 'A'
        if 80 <= average < 90:
            grade = 'B'
        if 70 <= average < 80:
            grade = 'C'
        if 60 <= average < 70:
            grade = 'D'
        if 0 <= average < 60:
            grade = 'F'

        student_string = last_name, first_name, id, art, greek, latin, science, math, high, low, average, grade
        new_student_string = f"{last_name : <15}{first_name : <15}{id : <6}{art : <10}{greek : <10}{latin : <10}{science : <10}{math : <12}{high : <6}{low : <6}{average : <8}{grade : <6}"
        
        
        
        #report = Student.get_student_academics(student)
            # high low average grade

        return student_string


###########################################################################################################
## look up student academic record
###########################################################################################################
def look_up_student_academic_record():
    # initialize list to store student IDs for validation
    id_list = []
    # add student IDs to the list
    for item in student_list:
        id_list.append(item.id)

   
# ask the user to put in a student ID.
    while True:
        student_id = input("Please enter the student ID.\n")
        if len(student_id) == 4 and student_id.isdigit() and int(student_id) in id_list:
            student_id = int(student_id)
            break
        else:
            print("Error. Not a valid student ID.")

    # look up the student object based on that ID.
    for item in student_list:
        test_id = int(item.id)
        id_list.append(item.id)

        if str(test_id) == str(student_id):
            current_student = item
    

    # Call getStudentAcademicReport() to get the student’s record.
    student_string = list(get_student_academic_report(current_student))

    last_name = student_string[0]
    first_name = student_string[1]
    id = student_string[2]
        
    art = int(student_string[3])
    greek = int(student_string[4])
    latin = int(student_string[5])
    science = int(student_string[6])
    math = int(student_string[7])
    
    scores = (art, greek, latin, science, math)

    high = max(scores)
    low = min(scores)
    average = sum(scores) / len(scores)

    if average >=90:
        grade = 'A'
    if 80 <= average < 90:
        grade = 'B'
    if 70 <= average < 80:
        grade = 'C'
    if 60 <= average < 70:
        grade = 'D'
    if 0 <= average < 60:
        grade = 'F'

    new_student_string = f"{last_name : <15}{first_name : <15}{id : <6}{art : <10}{greek : <10}{latin : <10}{science : <10}{math : <12}{high : <6}{low : <6}{average : <8}{grade : <6}"


    full_name =  first_name + " " + last_name
    # print header line
    print(f"\nIndividual Record for {full_name}:")
    print(f"\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Art' : <10}{'Greek' : <10}{'Latin' : <10}{'Science' : <10}{'Mathematics' : <12}{'High' : <6}{'Low' : <6}{'Average' : <8}{'Grade' : <6}")
    # Display the student’s academic result.
    print(new_student_string)    

###########################################################################################################
## get honor roll
###########################################################################################################
def get_honor_roll():
    # print heasder lines 
    print("\nHonor Roll:")
    print(f"{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Art' : <10}{'Greek' : <10}{'Latin' : <10}{'Science' : <10}{'Mathematics' : <12}{'High' : <6}{'Low' : <6}{'Average' : <8}{'Grade' : <6}")
    for item in student_list:
        honor_student = list(get_student_academic_report(item))
        grade = honor_student[11]
        #student_string = last_name, first_name, id, art, greek, latin, science, math, high, low, average, grade
        last_name = honor_student[0]
        first_name = honor_student[1]
        id = honor_student[2]
        
        art = int(honor_student[3])
        greek = int(honor_student[4])
        latin = int(honor_student[5])
        science = int(honor_student[6])
        math = int(honor_student[7])
    
        scores = (art, greek, latin, science, math)

        high = max(scores)
        low = min(scores)
        average = sum(scores) / len(scores)

        if average >=90:
            grade = 'A'
        if 80 <= average < 90:
            grade = 'B'
        if 70 <= average < 80:
            grade = 'C'
        if 60 <= average < 70:
            grade = 'D'
        if 0 <= average < 60:
            grade = 'F'
        
        new_student_string = f"{last_name : <15}{first_name : <15}{id : <6}{art : <10}{greek : <10}{latin : <10}{science : <10}{math : <12}{high : <6}{low : <6}{average : <8}{grade : <6}"

        if grade == 'A':
            print(new_student_string)


###########################################################################################################
## Full Academic Report by Last Name
###########################################################################################################

def display_full_academic_report_sorted_by_last_name():
    
    sort_student_list_by_last_name()

    display_full_student_academic_report()



###########################################################################################################
## Sort Student List by Last name
###########################################################################################################

def sort_student_list_by_last_name():
    student_list.sort(key=get_last_name)


def get_last_name(student):
    last_name = student.last_name
    return last_name

###########################################################################################################
## Full Academic Report by ID
###########################################################################################################
def display_full_academic_report_sorted_by_student_id():
    
    sort_student_list_by_student_id()

    display_full_student_academic_report()





###########################################################################################################
## Sort Student List by Student ID
###########################################################################################################

def sort_student_list_by_student_id():
        student_list.sort(key=get_id)


def get_id(student):
    student_id = student.id
    return student_id





###########################################################################################################
## function calls to initialize program
###########################################################################################################

# call get employees
get_employees()
# call get students
get_students()
# call get student scores
get_student_scores()
# call create menu
create_menu()
        