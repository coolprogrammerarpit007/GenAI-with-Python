
# Property Decorators

class Employee:
    def __init__(self,name,employee_code,department,salary):
        self.name = name
        self.employee_code = employee_code,
        self.department = department
        self._salary = salary # _ means attribute is protected and should not be accessed directly outside the class
        
    
    def introduce_employee(self):
        return f"Employee: {self.name} of employee code {self.employee_code} works in the {self.department} department!"
    
    @property
    def salary(self):
        return f"Employee {self.name} salary is {self._salary}"
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Amount can not be negative!")
        
        self._salary += value
        
        
employee1 = Employee("Arpit Mishra","LWP1078","Sales",25000)
print(employee1)
print(employee1.salary)
employee1.salary = 7500
print(employee1.salary)
