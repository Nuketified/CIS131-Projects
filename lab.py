from class_employee import Employee
from salaried_employee import Employee_salaried
from hourly_employee import Employee_hourly


# try and fail to initialize an Employee
try:
    mat = Employee('Mat', 'Bakarich', 12345678)

except TypeError:
    print("Can't initialize object of abstract class.")




sam = Employee_salaried('Samsonite', 'Bakarich', 12345678, 1000)
print("\n",sam,"\n")
sam.weekly_salary = 5000
#print(sam,"\n") 

mat = Employee_hourly('Mat', 'Bakarich',12345678 , 45, 10.50)
print(mat,"\n")

mat.wage = 20
mat.hour = 50

print(f"Samsonite's Pay:",sam.earnings(),"\nMat's Pay:",mat.earnings(),"\n")



# initialize and iterate the list
employees = [sam, mat]

for employee in employees:
    earnings = employee.earnings()
    print(f"{employee}\nEarnings: ${earnings:.2f}\n\n")

